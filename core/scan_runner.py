from collectors.system_collector import collect_system_info
from collectors.windows_audit import collect_windows_security

from analyzers.process_analyzer import collect_processes
from analyzers.file_integrity import scan_directory
from analyzers.risk_engine import calculate_risk

from database.db_manager import (
    save_file_results,
    save_findings
)


def run_scan():

    system_info = collect_system_info()

    security_info = collect_windows_security()

    processes = collect_processes()

    files = scan_directory("test_files")

    save_file_results(files)

    risk = calculate_risk(

        system_info,

        security_info,

        processes,

        files

    )

    save_findings(

        risk["findings"]

    )

    return {

        "system": system_info,

        "security": security_info,

        "processes": processes,

        "files": files,

        "risk": risk

    }