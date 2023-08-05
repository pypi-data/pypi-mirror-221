# Start writing uagents models from here
from enum import Enum

from uagents import Model


class MessageType(Enum):
    sms = "sms"
    whatsapp = "whatsapp"


class Message(Model):
    receiver: str
    msg: str
    type: MessageType = MessageType.sms
