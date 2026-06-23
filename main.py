from core.logger import setup_logger
from core.config import load_config

from collectors.system_collector import collect_system_info



def start_cyberguard():


    logger = setup_logger()

    config = load_config()


    logger.info("CyberGuard application started")


    print("=" * 50)

    print("CyberGuard Endpoint Security Assessment System")

    print("=" * 50)


    print("Version:", config["version"])

    print("Scan Mode:", config["scan_mode"])



    print("\nCollecting Endpoint Information...\n")


    system_info = collect_system_info()


    for key, value in system_info.items():

        print(key, ":", value)



    logger.info(
        "Endpoint information collected successfully"
    )



if __name__ == "__main__":

    start_cyberguard()