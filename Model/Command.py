from enum import Enum


class Command(Enum):
    """
    Command is an enumeration of commands that appears in WechatReminder
    Designed & programmed by Shenran Wang
    """
    NOTIFY = "notify"
    DELETE = "delete"
