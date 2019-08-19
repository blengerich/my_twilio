from twilio.rest import Client
from .config import config

account_sid = config["account_sid"]
auth_token = config["auth_token"]


def notify_me(message):
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=message,
        from_=config["from_number"],
        to=config["to_number"]
    )
