from core.finding_factory import FindingFactory


def calculate_risk(system_info, security_info, processes, file_results):

    findings = []

    # --------------------------------------------------
    # File Integrity
    # --------------------------------------------------

    for file in file_results:

        if file["status"] == "MODIFIED":

            findings.append(

                FindingFactory.create(

                    title="Modified File",

                    category="File Integrity",

                    severity="Medium",

                    raw_score=15,

                    description=f"{file['file']} has changed since the previous scan.",

                    recommendation="Verify the file modification.",

                    module="File Integrity"

                )

            )

    # --------------------------------------------------
    # Unknown Process
    # --------------------------------------------------

    for process in processes:

        if process["name"] == "Unknown":

            findings.append(

                FindingFactory.create(

                    title="Unknown Process",

                    category="Process Analysis",

                    severity="High",

                    raw_score=20,

                    description=f"Unknown process detected (PID {process['pid']}).",

                    recommendation="Investigate the process.",

                    module="Process Analyzer"

                )

            )

    # --------------------------------------------------
    # Firewall
    # --------------------------------------------------

    firewall_profiles = security_info.get(
        "Firewall Status",
        []
    )

    for profile in firewall_profiles:

        if not profile["Enabled"]:

            findings.append(

                FindingFactory.create(

                    title="Firewall Disabled",

                    category="Windows Security",

                    severity="Critical",

                    raw_score=40,

                    description=f"{profile['Name']} firewall profile is disabled.",

                    recommendation="Enable Windows Firewall immediately.",

                    module="Windows Audit"

                )

            )

    # --------------------------------------------------
    # Risk Calculation
    # --------------------------------------------------

    raw_score = sum(f.raw_score for f in findings)

    normalized_score = min(raw_score, 100)

    severity_order = {

        "LOW": 1,

        "MEDIUM": 2,

        "HIGH": 3,

        "CRITICAL": 4

    }

    highest = "LOW"

    for finding in findings:

        if severity_order[finding.severity] > severity_order[highest]:

            highest = finding.severity

    # --------------------------------------------------
    # Enterprise Risk Decision
    # --------------------------------------------------

    if highest == "CRITICAL":

        level = "CRITICAL"

    elif highest == "HIGH":

        level = "HIGH"

    elif normalized_score >= 40:

        level = "MEDIUM"

    else:

        level = "LOW"

    return {

        "raw_score": raw_score,

        "score": normalized_score,

        "highest_severity": highest,

        "level": level,

        "findings": findings,

        "finding_count": len(findings)

    }