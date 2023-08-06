import asyncio
from typing import Any
from typing import Dict
from typing import Optional


async def await_operation(hub, ctx, initial_response, resource_url) -> Dict[str, Any]:
    """
    Awaits a long-running asynchronous Azure operation to complete. Performs an additional GET request when operation completes to fetch the resulting Azure resource.
    :param initial_response: initial HTTP response from Azure API call which initiated the operation
    :param resource_url: Azure API URL, used to GET the resource produced by the operation
    """
    poller = OperationPoller(hub, ctx, initial_response, resource_url)
    return await poller.await_operation()


class OperationFailed(Exception):
    pass


class OperationStatus:
    """Operation status class.

    Operation status is used to indicate the status of an operation. It can be one of the following values: Succeeded, Failed, Canceled, Running.
    """

    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    CANCELED = "Canceled"
    RUNNING = "Running"

    FINISHED_STATES = {SUCCEEDED.lower(), FAILED.lower(), CANCELED.lower()}
    FAILED_STATES = {FAILED.lower(), CANCELED.lower()}
    SUCCEEDED_STATES = {SUCCEEDED.lower()}

    @staticmethod
    def finished(status):
        return str(status).lower() in OperationStatus.FINISHED_STATES

    @staticmethod
    def failed(status):
        return str(status).lower() in OperationStatus.FAILED_STATES

    @staticmethod
    def succeeded(status):
        return str(status).lower() in OperationStatus.SUCCEEDED_STATES


class OperationPoller:
    def __init__(self, hub, ctx, initial_response, resource_url):
        self._hub = hub
        self._ctx = ctx
        self._initial_response = initial_response
        self._resource_url = resource_url
        self._status_url = self._get_status_url()
        self._status = None
        self._error = None

    async def await_operation(self) -> Dict[str, Any]:
        return await self._poll()

    def _get_status_url(self) -> Optional[str]:
        headers: Dict[str, Any] = self._initial_response.get("headers")

        if "Azure-AsyncOperation" in headers:
            return headers["Azure-AsyncOperation"]
        elif "Location" in headers:
            return headers["Location"]
        else:
            return None

    def _get_retry_after(self) -> int:
        headers = self._initial_response.get("headers")

        retry_after = headers.get("Retry-After")
        try:
            delay = int(retry_after)
        except ValueError:
            delay = 1

        return delay if delay > 1 else 1

    def _operation_finished(self) -> bool:
        return OperationStatus.finished(self._status)

    def _operation_succeeded(self) -> bool:
        return OperationStatus.succeeded(self._status)

    async def _update_status(self):
        get_response = await self._hub.exec.request.json.get(
            self._ctx,
            url=self._status_url,
            success_codes=[200],
        )
        if "status" in get_response["ret"]:
            self._status = get_response["ret"]["status"].lower()
        else:
            self._status = None
        if "error" in get_response["ret"]:
            self._error = get_response["ret"]["error"]
        else:
            self._error = None

    async def _delay(self):
        await asyncio.sleep(self._get_retry_after())

    async def _poll(self):
        if not self._operation_finished():
            await self._update_status()
        while not self._operation_finished():
            await self._delay()
            await self._update_status()

        if not self._operation_succeeded():
            raise OperationFailed(
                f"Operation failed or has been canceled: {self._error}"
            )
        else:
            get_response = await self._hub.exec.request.json.get(
                self._ctx,
                url=self._resource_url,
                success_codes=[200],
            )
            return get_response
