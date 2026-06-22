from core.logger import setup_logger
from core.config import load_config


def start_cyberguard():

    logger = setup_logger()

    config = load_config()

    logger.info("CyberGuard application started")

    print("=" * 50)

    print("CyberGuard Endpoint Security Assessment System")

    print("=" * 50)

    print("Version:", config["version"])

    print("Scan Mode:", config["scan_mode"])

    print("\nCyberGuard initialized successfully")


if __name__ == "__main__":

    start_cyberguard()