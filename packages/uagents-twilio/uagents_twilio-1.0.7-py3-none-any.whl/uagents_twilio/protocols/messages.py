from decouple import config
from uagents import Context, Protocol

from uagents_twilio.models import Message, MessageType
from uagents_twilio.wrappers.messageWrapper import MessageClient

service_protocol = Protocol()
AGENT_ADDRESS = config("AGENT_ADDRESS")
ACCOUNT_SID = config("ACCOUNT_SID")
AUTH_TOKEN = config("AUTH_TOKEN")
FROM_NUMBER = config("FROM_NUMBER")
WP_FROM_NUMBER = config("WP_FROM_NUMBER")
TO_NUMBER = config("TO_NUMBER")


message_handler = MessageClient(
    agent=service_protocol,
    to_agent_address=AGENT_ADDRESS,
    account_sid=ACCOUNT_SID,
    auth_token=AUTH_TOKEN,
    from_number=FROM_NUMBER,
    to_number=TO_NUMBER,
)


@service_protocol.on_query(model=Message)
async def receive_wp_msg(ctx: Context, sender: str, message: Message):
    """Receive message from Twilio Webhook and send starting message on Whatsapp"""
    ctx.storage.set("message", message.msg)
    if message.type == MessageType.whatsapp:
        if not message.receiver.startswith("whatsapp:"):
            message.receiver = f"whatsapp:{message.receiver}"
        message_handler.from_number = WP_FROM_NUMBER
    message_handler.send_message(message.receiver, message.msg, message.type)


@service_protocol.on_message(model=Message)
async def send_wp_msg(ctx: Context, sender: str, message: Message):
    """Send Whatsapp Message or SMS using uagent"""
    ctx.storage.set("message", message.msg)
    if message.type == MessageType.whatsapp:
        if not message.receiver.startswith("whatsapp:"):
            message.receiver = f"whatsapp:{message.receiver}"
        message_handler.from_number = WP_FROM_NUMBER
    message_handler.send_message(message.receiver, message.msg, message.type)
