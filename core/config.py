import json
import os


CONFIG_PATH = "config/settings.json"


def load_config():


    if not os.path.exists(CONFIG_PATH):

        default_settings = {

            "project_name": "CyberGuard",
            "version": "1.0",
            "scan_mode": "standard"

        }


        with open(CONFIG_PATH, "w") as file:

            json.dump(default_settings, file, indent=4)


    with open(CONFIG_PATH, "r") as file:

        settings = json.load(file)


    return settings