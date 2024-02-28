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
        crontab += f"{tell[2]} /usr/bin/python3 /root/tellme.py {tell_name}\n"
    return crontab

def write_crontab(crontab):
    command = f"echo -e '{crontab}' | crontab -u root -"
    subprocess.run(command, shell=True, check=True)

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
    except:
        sys.exit(f"when.py: One or more errors in {config} prevented the crontab from being built.")

if __name__ == "__main__":
    when()