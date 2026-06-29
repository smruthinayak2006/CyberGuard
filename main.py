from importlib.resources import files

from core.logger import setup_logger
from core.config import load_config
from core.display import display_section, display_dictionary

from collectors.system_collector import collect_system_info
from collectors.windows_audit import collect_windows_security
from analyzers.process_analyzer import collect_processes
from analyzers.file_integrity import scan_directory

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

    display_section(
        "Windows Security Audit"
    )

    security_info = collect_windows_security()


    display_dictionary(security_info)


    logger.info(
        "Windows security audit completed"
    )


    logger.info(
        "Endpoint information collected successfully"
    )

    display_section("Running Processes")

    processes = collect_processes()

    for process in processes[:15]:

        print(
            f"PID: {process['pid']}\n"
            f"Name: {process['name']}\n"
            f"CPU: {process['cpu']}%\n"
            f"RAM: {process['memory']:.2f}%\n"
            f"Path: {process['path']}\n"
            + "-" * 50
        )

    display_section("File Integrity Monitoring")

    files = scan_directory("test_files")

    for file in files:

        print(f"File   : {file['file']}")
        print(f"SHA256 : {file['sha256']}")
        print(f"Status : {file['status']}")
        print("-" * 60)



if __name__ == "__main__":

    start_cyberguard()