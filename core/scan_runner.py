from collectors.system_collector import collect_system_info
from collectors.windows_audit import collect_windows_security

from analyzers.process_analyzer import collect_processes
from analyzers.file_integrity import scan_directory
from analyzers.risk_engine import calculate_risk

from collectors.startup_collector import collect_startup_programs
from analyzers.startup_analyzer import analyze_startup_programs

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
    # Startup Programs
    # ----------------------------------------

    startup_programs = collect_startup_programs()

    startup_findings = analyze_startup_programs(
        startup_programs
    )


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
    risk["findings"].extend(startup_findings)

    risk["raw_score"] += sum(
        finding.raw_score
        for finding in startup_findings
    )

    risk["score"] = min(
        risk["raw_score"],
        100
    )

    risk["finding_count"] = len(
        risk["findings"]
    )

    severity_order = {
        "LOW": 1,
        "MEDIUM": 2,
        "HIGH": 3,
        "CRITICAL": 4
    }

    for finding in startup_findings:

        if severity_order[finding.severity] > severity_order[risk["highest_severity"]]:

            risk["highest_severity"] = finding.severity
            risk["level"] = finding.severity


    # ----------------------------------------
    # Store Scan History
    # ----------------------------------------

    scan_id = save_scan(

        system_info,

        risk

    )

    # ----------------------------------------
    # Store Findings
    # ----------------------------------------

    save_findings(

        scan_id,

        risk["findings"]

    )

    # ----------------------------------------
    # Complete Scan Object
    # ----------------------------------------

    scan = {

        "system": system_info,

        "security": security_info,

        "processes": processes,

        "startup_programs": startup_programs,
        
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