from typing import Dict


def cleanup_none_values(hub, input_dict: Dict):
    return {k: v for (k, v) in input_dict.items() if v is not None}
