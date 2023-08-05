# Start writing uagents models from here
from uagents import Model


class WhatsAppMsg(Model):
    receiver: str
    msg: str


class SMS(Model):
    receiver: str
    msg: str
