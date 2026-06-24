from core.logger import setup_logger
from core.config import load_config
from core.display import display_section, display_dictionary

from collectors.system_collector import collect_system_info



def start_cyberguard():

    logger = setup_logger()

    config = load_config()


    logger.info("CyberGuard application started")


    display_section(
        "CyberGuard Endpoint Security Assessment System"
    )


    print("Version:", config["version"])

    print("Scan Mode:", config["scan_mode"])


    display_section(
        "Endpoint Information"
    )


    system_info = collect_system_info()


    display_dictionary(system_info)


    logger.info(
        "Endpoint information collected successfully"
    )



if __name__ == "__main__":

    start_cyberguard()