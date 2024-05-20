import subprocess
import toml
import sys

DEV = False
CONFIG = "me.toml"

def load(config):
    """Open TOML file and return dictionary"""
    with open(config, "r") as toml_file:
        toml_dict = toml.load(toml_file)
    return toml_dict

def gen_crontab(tells):
    crontab = ""
    for tell_name, tell in tells.items():
        crontab += f"{tell[2]} /root/env/bin/python3 /root/tell.py {tell_name}\n"
    return crontab

def write_crontab(crontab):
    command = ['crontab', '-u', 'root', '-']
    subprocess.run(command, input=crontab, text=True, check=True)

def when():
    """Build and write crontab."""
    if DEV is True:
        config = "dev.toml"
    else:
        config = CONFIG
    # Load tells from config file
    try:
        config = load(config)
        print("tmw: load config success")
    except FileNotFoundError:
        sys.exit(f"when.py: Error opening {config}. Check the file exists and you have the correct permissions.")
    # Write and generate crontab
    try:
        write_crontab(gen_crontab(config["tells"]))
        print("tmw: write crontab success")
    except FileNotFoundError:
        sys.exit("when.py: Crontab could not be found.")
    except PermissionError:
        sys.exit("when.py: Script does not have permission to execute the crontab command as root.")

if __name__ == "__main__":
    when()
