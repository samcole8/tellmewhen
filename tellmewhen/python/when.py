import subprocess
import toml

def load(config):
    """Open TOML file and return dictionary"""
    with open(config, "r") as toml_file:
        toml_dict = toml.load(toml_file)
    return toml_dict

def when():
    """"""
    tells = load("tells.toml")["tells"]
    append = ""
    for tell_name, tell in tells.items():
        append += f"{tell[2]} /usr/bin/python3 /root/tellme.py {tell_name}\n"
    command = f"echo -e '{append}' | crontab -u root -"
    subprocess.run(command, shell=True, check=True)

if __name__ == "__main__":
    when()