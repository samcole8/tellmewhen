#!/bin/python3

from sys import argv
import toml
import requests
import smtplib, ssl
from email.mime.text import MIMEText

DEV = False
CONFIG = "me.toml"

def load(config):
    """Open TOML file and return dictionary"""
    with open(config, "r") as toml_file:
        toml_dict = toml.load(toml_file)
    return toml_dict

def post(tell, settings):
    calls = list(tell[1])
    status = {}
    if "s" in calls:
        # Send SMS message
        sms = settings["sms"]
    if "e" in calls:
        # Send email
        
        email = settings["email"]

        # Set body
        msg = MIMEText(email["body"])
        msg["Subject"] = tell[0]
        msg["From"] = email["from"]
        
        # Initiate SSL
        context = ssl.create_default_context()

        # Login and send email
        with smtplib.SMTP_SSL(email["server"], email["port"], context=context) as server:
            server.login(email["login"], email["secret"])
            server.sendmail(email["from"], email["to"], msg.as_string())

    if "t" in calls:

        # Send Telegram message
        tele = settings["tele"]
        status["t"] = requests.post(f"https://api.telegram.org/bot{tele['bot_token']}/sendMessage", params={"chat_id": tele["chat_id"], "text": tell[0]},).status_code
    
    return status

def tellme(tell, config):
    # Get tell data from config
    if DEV is True:
        config = "dev.toml"
    else:
        config = "me.toml"
    config = load(config)
    tell = config["tells"][tell]
    # Post tell data
    post(tell, config["settings"])

if __name__ == "__main__":
    tellme(argv[1], CONFIG)