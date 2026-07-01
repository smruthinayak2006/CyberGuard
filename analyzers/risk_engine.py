from core.finding_factory import FindingFactory


def calculate_risk(system_info, security_info, processes, file_results):

    findings = []

    # --------------------------------------------------
    # Modified Files
    # --------------------------------------------------

    for file in file_results:

        if file["status"] == "MODIFIED":

            findings.append(

                FindingFactory.create(

                    title="Modified File",

                    category="File Integrity",

                    severity="Medium",

                    raw_score=15,

                    description=(
                        f"{file['file']} has changed "
                        "since the previous scan."
                    ),

                    recommendation=(
                        "Verify that the file modification "
                        "was authorized."
                    ),

                    module="File Integrity"

                )

            )

    # --------------------------------------------------
    # Unknown Processes
    # --------------------------------------------------

    for process in processes:

        if process["name"] == "Unknown":

            findings.append(

                FindingFactory.create(

                    title="Unknown Process",

                    category="Process Analysis",

                    severity="High",

                    raw_score=20,

                    description=(
                        f"Unknown process detected "
                        f"(PID {process['pid']})."
                    ),

                    recommendation=(
                        "Investigate the process "
                        "before allowing execution."
                    ),

                    module="Process Analyzer"

                )

            )

    # --------------------------------------------------
    # Firewall Check
    # --------------------------------------------------

    firewall_profiles = security_info.get(
        "Firewall Status",
        []
    )

    for profile in firewall_profiles:

        if not profile.get("Enabled", True):

            findings.append(

                FindingFactory.create(

                    title="Firewall Disabled",

                    category="Windows Security",

                    severity="Critical",

                    raw_score=40,

                    description=(
                        f"{profile['Name']} firewall "
                        "profile is disabled."
                    ),

                    recommendation=(
                        "Enable the firewall "
                        "immediately."
                    ),

                    module="Windows Audit"

                )

            )

    # --------------------------------------------------
    # Score Calculation
    # --------------------------------------------------

    raw_score = sum(

        finding.raw_score

        for finding in findings

    )

    normalized_score = min(raw_score, 100)

    if normalized_score <= 20:

        level = "LOW"

    elif normalized_score <= 40:

        level = "MEDIUM"

    elif normalized_score <= 70:

        level = "HIGH"

    else:

        level = "CRITICAL"

    return {

        "raw_score": raw_score,

        "score": normalized_score,

        "level": level,

        "findings": findings,

        "finding_count": len(findings)

    }