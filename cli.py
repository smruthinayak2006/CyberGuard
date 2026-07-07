from core.logger import setup_logger
from core.config import load_config
from core.display import display_section, display_dictionary

from database.db_manager import initialize_database

from core.scan_runner import run_scan


initialize_database()


def start_cyberguard():

    logger = setup_logger()

    config = load_config()

    logger.info("CyberGuard application started")

    display_section(
        "CyberGuard Endpoint Security Assessment System"
    )

    print("Version:", config["version"])
    print("Scan Mode:", config["scan_mode"])

    # ----------------------------------------

    results = run_scan()

    system_info = results["system"]

    security_info = results["security"]

    processes = results["processes"]

    files = results["files"]

    risk = results["risk"]

    # ----------------------------------------

    display_section("Endpoint Information")

    display_dictionary(system_info)

    logger.info(
        "Endpoint information collected successfully"
    )

    # ----------------------------------------

    display_section("Windows Security Audit")

    display_dictionary(security_info)

    logger.info(
        "Windows security audit completed"
    )

    # ----------------------------------------

    display_section("Running Processes")

    for process in processes[:15]:

        print(f"PID: {process['pid']}")
        print(f"Name: {process['name']}")
        print(f"CPU: {process['cpu']}%")
        print(f"RAM: {process['memory']:.2f}%")
        print(f"Path: {process['path']}")
        print("-" * 50)

    # ----------------------------------------

    display_section("File Integrity Monitoring")

    for file in files:

        print(f"File   : {file['file']}")
        print(f"SHA256 : {file['sha256']}")
        print(f"Status : {file['status']}")
        print("-" * 60)

    # ----------------------------------------

    display_section("Overall Risk Assessment")

    print(f"Raw Score         : {risk['raw_score']}")
    print(f"Normalized Score  : {risk['score']} / 100")
    print(f"Highest Severity  : {risk['highest_severity']}")
    print(f"Overall Risk      : {risk['level']}")
    print(f"Total Findings    : {risk['finding_count']}")

    print("\nSecurity Findings")

    if risk["findings"]:

        for finding in risk["findings"]:

            print("-" * 60)
            print(f"ID              : {finding.finding_id}")
            print(f"Title           : {finding.title}")
            print(f"Severity        : {finding.severity}")
            print(f"Category        : {finding.category}")
            print(f"Raw Score       : {finding.raw_score}")
            print(f"Module          : {finding.module}")
            print(f"Recommendation  : {finding.recommendation}")

    else:

        print("No significant security findings.")


if __name__ == "__main__":

    start_cyberguard()