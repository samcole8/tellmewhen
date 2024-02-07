#!/bin/python3

from sys import argv
import toml

def load(config):
    """Open TOML file and return dictionary"""
    with open(config, "r") as toml_file:
        toml_dict = toml.load(toml_file)
    return toml_dict

def post(tell, config):
    calls = list(tell[1])
    if "s" in calls:
        # Send SMS
        print("s")
        
    if "e" in calls:
        # Send email
        print("e")
    if "t" in calls:
        # Send Telegram message
        print("t")


def get_arg():
    tell = argv[1]
    return (tell)

def tellme():
    # Get tell
    tell_name = get_arg()
    # Get tell data from config
    config = load("tells.toml")
    tell = config["tells"][tell_name]
    # Post tell data
    post(tell, config)

if __name__ == "__main__":
    tellme()