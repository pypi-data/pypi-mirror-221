def create_comment(hub, resource_type: str, name: str) -> str:
    return f"Created {resource_type} '{name}'"


def would_create_comment(hub, resource_type: str, name: str) -> str:
    return f"Would create {resource_type} '{name}'"


def could_not_create_comment(hub, resource_type: str, name: str) -> str:
    return f"Could not create {resource_type} '{name}'"


def no_property_to_be_updated_comment(hub, resource_type: str, name: str) -> str:
    return f"{resource_type} '{name}' has no property need to be updated."


def already_exists_comment(hub, resource_type: str, name: str) -> str:
    return f"{resource_type} '{name}' already exists."


def update_comment(hub, resource_type: str, name: str) -> str:
    return f"Updated {resource_type} '{name}'"


def would_update_comment(hub, resource_type: str, name: str) -> str:
    return f"Would update {resource_type} '{name}'"


def could_not_update_comment(hub, resource_type: str, name: str) -> str:
    return f"Could not update {resource_type} '{name}'"


def could_not_get_comment(hub, resource_type: str, name: str) -> str:
    return f"Could not get {resource_type} '{name}'"


def up_to_date_comment(hub, resource_type: str, name: str) -> str:
    return f"{resource_type} '{name}' is up to date."


def delete_comment(hub, resource_type: str, name: str) -> str:
    return f"Deleted {resource_type} '{name}'"


def would_delete_comment(hub, resource_type: str, name: str) -> str:
    return f"Would delete {resource_type} '{name}'"


def could_not_delete_comment(hub, resource_type: str, name: str) -> str:
    return f"Could not delete {resource_type} '{name}'"


def already_absent_comment(hub, resource_type: str, name: str) -> str:
    return f"{resource_type} '{name}' already absent"
