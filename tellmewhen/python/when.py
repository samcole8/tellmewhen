import subprocess
import toml

def load(config):
    """Open TOML file and return dictionary"""
    with open(config, "r") as toml_file:
        toml_dict = toml.load(toml_file)
    return toml_dict

def when():
    """"""
    tells = load("me.toml")["tells"]
    
    # Add tells to crontab
    crontab = ""
    for tell_name, tell in tells.items():
        crontab += f"{tell[2]} /usr/bin/python3 /root/tellme.py {tell_name}\n"
    # Write crontab
    command = f"echo -e '{crontab}' | crontab -u root -"
    subprocess.run(command, shell=True, check=True)

if __name__ == "__main__":
    when()