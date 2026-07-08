from collectors.system_collector import collect_system_info
from collectors.windows_audit import collect_windows_security

from analyzers.process_analyzer import collect_processes
from analyzers.file_integrity import scan_directory
from analyzers.risk_engine import calculate_risk

from database.db_manager import (
    save_file_results,
    save_findings,
    save_scan
)

from reports.report_generator import generate_report


def run_scan():

    # ----------------------------------------
    # Collect Endpoint Information
    # ----------------------------------------

    system_info = collect_system_info()

    # ----------------------------------------
    # Windows Security Audit
    # ----------------------------------------

    security_info = collect_windows_security()

    # ----------------------------------------
    # Running Processes
    # ----------------------------------------

    processes = collect_processes()

    # ----------------------------------------
    # File Integrity Monitoring
    # ----------------------------------------

    files = scan_directory("test_files")

    save_file_results(files)

    # ----------------------------------------
    # Risk Analysis
    # ----------------------------------------

    risk = calculate_risk(

        system_info,

        security_info,

        processes,

        files

    )

    # ----------------------------------------
    # Store Findings
    # ----------------------------------------

    save_findings(

        risk["findings"]

    )

    # ----------------------------------------
    # Store Scan History
    # ----------------------------------------

    save_scan(

        system_info,

        risk

    )

    # ----------------------------------------
    # Complete Scan Object
    # ----------------------------------------

    scan = {

        "system": system_info,

        "security": security_info,

        "processes": processes,

        "files": files,

        "risk": risk

    }

    # ----------------------------------------
    # Generate PDF Report
    # ----------------------------------------

    report_path = generate_report(scan)

    scan["report_path"] = report_path

    # ----------------------------------------

    return scan