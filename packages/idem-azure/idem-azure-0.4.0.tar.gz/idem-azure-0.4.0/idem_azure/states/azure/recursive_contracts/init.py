RESOURCES_WITH_PRESENT_WRAPPER = [
    "azure.sql_database.databases",
]


async def call_present(hub, ctx):
    r"""Wrapper for present function."""

    name = ctx.kwargs.get("name", None)
    state_ctx = ctx.kwargs.get("ctx") or ctx.args[1]
    assert state_ctx, f"state context is missing: {state_ctx}"

    azure_service_resource_type = state_ctx.get("tag").split("_|")[0]

    # TODO: This needs to be removed once all resources follow the contract
    if azure_service_resource_type not in RESOURCES_WITH_PRESENT_WRAPPER:
        return await ctx.func(*ctx.args, **ctx.kwargs)

    result = {
        "result": True,
        "old_state": None,
        "new_state": None,
        "name": name,
        "comment": [],
    }

    ctx.kwargs[
        "subscription_id"
    ] = hub.tool.azure.resource_utils.get_subscription_id_from_account(
        state_ctx, ctx.kwargs.get("subscription_id")
    )

    service_resource_type = azure_service_resource_type.replace("azure.", "")

    hub_ref_exec = hub.exec.azure
    for resource_path_segment in service_resource_type.split("."):
        hub_ref_exec = hub_ref_exec[resource_path_segment]

    resource_id = ctx.kwargs.get("resource_id")
    local_params = {**ctx.kwargs}

    get_resource_only_with_resource_id = hub.OPT.idem.get(
        "get_resource_only_with_resource_id", False
    )

    if resource_id:
        response_get = await hub_ref_exec.get(state_ctx, resource_id=resource_id)

        if not response_get["result"] or (
            not response_get["ret"] and get_resource_only_with_resource_id
        ):
            result["result"] = False
            result["comment"] += response_get["comment"]
            return result

        result["old_state"] = response_get["ret"]
    elif not get_resource_only_with_resource_id:
        resource_id = hub.tool.azure.resource_utils.construct_resource_id(
            service_resource_type, local_params
        )

        if not resource_id:
            result["result"] = False
            result["comment"].append(
                f"Could not construct resource ID of {azure_service_resource_type} from input arguments."
            )
            return result

        response_get = await hub_ref_exec.get(state_ctx, resource_id=resource_id)

        if not response_get["result"]:
            result["result"] = False
            result["comment"] += response_get["comment"]
            return result

        if response_get["ret"]:
            result["old_state"] = response_get["ret"]

    state_ctx["wrapper_result"] = result
    state_ctx["computed"] = {
        "resource_url": hub.tool.azure.resource_utils.construct_resource_url(
            state_ctx, service_resource_type, local_params
        ),
    }
    return await ctx.func(*ctx.args, **{**ctx.kwargs, "resource_id": resource_id})
