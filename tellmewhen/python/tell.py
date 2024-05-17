#!/bin/python3

from sys import argv
import toml
import requests
import smtplib
import ssl
from email.mime.text import MIMEText
from twilio.rest import Client

DEV = False
CONFIG = "me.toml"

def load(config):
    """Open TOML file and return dictionary"""
    with open(config, "r") as toml_file:
        toml_dict = toml.load(toml_file)
    return toml_dict

def tele(tell, t):
    print(requests.post(f"https://api.telegram.org/bot{t['bot_token']}/sendMessage", params={"chat_id": t["chat_id"], "text": tell},))

def email(tell, e):
    # Set body
    msg = MIMEText(e["body"])
    msg["Subject"] = tell
    msg["From"] = e["from"]
    
    # Initiate SSL
    context = ssl.create_default_context()

    # Login and send email
    with smtplib.SMTP_SSL(e["server"], e["port"], context=context) as server:
        server.login(e["login"], e["secret"])
        server.sendmail(e["from"], e["to"], msg.as_string())

def sms(tell, s):
    # Set up SMS objects
    client = Client(s["account_sid"], s["auth_token"])
    message = client.messages \
                    .create(
                        body=tell,
                        from_=s["from"],
                        to=s["to"]
                    )
    # Send SMS
    print(message.sid)

def post(tell, settings):
    calls = list(tell[1])
    if "s" in calls:
        # Send SMS message
        sms(tell[0], settings["sms"])
    if "e" in calls:
        # Send email
        email(tell[0], settings["email"])
    if "t" in calls:
        # Send Telegram message
        tele(tell[0], settings["tele"])

def tellme(tell, config):
    # Get tell data from config
    if DEV is True:
        config = "dev.toml"
    else:
        config = CONFIG
    config = load(config)
    tell = config["tells"][tell]
    # Post tell data
    post(tell, config["settings"])

if __name__ == "__main__":
    tellme(argv[1], CONFIG)