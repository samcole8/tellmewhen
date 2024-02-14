#!/bin/python3

from sys import argv
import toml
import requests

CONFIG = "me.toml"

def load(config):
    """Open TOML file and return dictionary"""
    with open(config, "r") as toml_file:
        toml_dict = toml.load(toml_file)
    return toml_dict

def post(tell, settings):
    calls = list(tell[1])
    if "s" in calls:
        # Send SMS
        sms = settings["sms"]
    if "e" in calls:
        # Send email
        email = settings["email"]
    if "t" in calls:
        # Send Telegram message
        tele = settings["tele"]
        post = requests.post(f"https://api.telegram.org/bot{tele['bot_token']}/sendMessage", params={"chat_id": tele["chat_id"], "text": tell[0]},)

def tellme(tell, config):
    # Get tell data from config
    config = load("me.toml")
    tell = config["tells"][tell]
    # Post tell data
    post(tell, config["settings"])

if __name__ == "__main__":
    tellme(argv[1], CONFIG)