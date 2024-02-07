import subprocess

def load(config):
    """Open TOML file and return dictionary"""
    with open(config, "r") as toml_file:
        toml_dict = toml.load(toml_file)
    return toml_dict

def when():
    """"""
    tells = load("tells.toml")[tells]
    for tell_name, tell in tells:
        command = f"echo -e '{tell[2]} /root/tellme.py {tell_name}\n' | crontab -u root -"
        subprocess.run(command, shell=True, check=True)

if __name__ == "__main__":
    when()