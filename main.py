from core.logger import setup_logger
from core.config import load_config
from core.display import display_section, display_dictionary

from collectors.system_collector import collect_system_info
from collectors.windows_audit import collect_windows_security

from analyzers.process_analyzer import collect_processes
from analyzers.file_integrity import scan_directory
from analyzers.risk_engine import calculate_risk

from database.db_manager import (
    initialize_database,
    save_file_results
)

initialize_database()


def start_cyberguard():

    logger = setup_logger()

    config = load_config()

    logger.info("CyberGuard application started")

    display_section("CyberGuard Endpoint Security Assessment System")

    print("Version:", config["version"])
    print("Scan Mode:", config["scan_mode"])

    # --------------------------------------------------

    display_section("Endpoint Information")

    system_info = collect_system_info()

    display_dictionary(system_info)

    logger.info("Endpoint information collected successfully")

    # --------------------------------------------------

    display_section("Windows Security Audit")

    security_info = collect_windows_security()

    display_dictionary(security_info)

    logger.info("Windows security audit completed")

    # --------------------------------------------------

    display_section("Running Processes")

    processes = collect_processes()

    for process in processes[:15]:

        print(f"PID: {process['pid']}")
        print(f"Name: {process['name']}")
        print(f"CPU: {process['cpu']}%")
        print(f"RAM: {process['memory']:.2f}%")
        print(f"Path: {process['path']}")
        print("-" * 50)

    # --------------------------------------------------

    display_section("File Integrity Monitoring")

    files = scan_directory("test_files")

    save_file_results(files)

    for file in files:

        print(f"File   : {file['file']}")
        print(f"SHA256 : {file['sha256']}")
        print(f"Status : {file['status']}")
        print("-" * 60)

    # --------------------------------------------------

    risk = calculate_risk(

        system_info,
        security_info,
        processes,
        files

    )

    display_section("Overall Risk Assessment")

    print(f"Risk Score : {risk['score']} / 100")
    print(f"Risk Level : {risk['level']}")
    print(f"Total Findings : {risk['finding_count']}")

    print("\nSecurity Findings")

    if risk["findings"]:

        for finding in risk["findings"]:

            print(f"- {finding}")

    else:

        print("No significant security findings.")


if __name__ == "__main__":

    start_cyberguard()