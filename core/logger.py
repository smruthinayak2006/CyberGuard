import logging
import os


def setup_logger():

    if not os.path.exists("logs"):
        os.makedirs("logs")


    logging.basicConfig(
        filename="logs/cyberguard.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )


    logger = logging.getLogger("CyberGuard")

    return logger