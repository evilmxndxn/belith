from enum import Enum

from ..config.settings import settings


class OpsecMode(str, Enum):
    NORMAL = "normal"
    STEALTH = "stealth"
    LAB = "lab"


def get_opsec_mode() -> OpsecMode:
    try:
        return OpsecMode(settings.opsec_mode)
    except ValueError:
        return OpsecMode.NORMAL


def is_active_scanning_allowed() -> bool:
    mode = get_opsec_mode()
    return mode in {OpsecMode.NORMAL, OpsecMode.LAB}


def is_external_file_upload_allowed() -> bool:
    mode = get_opsec_mode()
    return mode == OpsecMode.LAB
