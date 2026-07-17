from core.finding_factory import FindingFactory


TRUSTED_KEYWORDS = {

    "microsoft",
    "windows",
    "google",
    "chrome",
    "edge",
    "mozilla",
    "firefox",
    "intel",
    "realtek",
    "amd",
    "nvidia",
    "docker",
    "python",
    "git",
    "github",
    "visual studio",
    "code.exe",
    "vscode",
    "onedrive",
    "teams",
    "discord",
    "spotify",
    "steam",
    "java",
    "oracle"

}


SYSTEM_PROCESSES = {

    "System",
    "System Idle Process",
    "Registry"

}


def calculate_risk(system_info, security_info, processes, file_results):

    findings = []

    # --------------------------------------------------
    # Process Analysis
    # --------------------------------------------------

    for process in processes:

        executable = process["path"].lower()

        trusted = any(

            keyword in executable

            for keyword in TRUSTED_KEYWORDS

        )

        if process["name"] == "Unknown":

            findings.append(

                FindingFactory.create(

                    title="Unknown Process",

                    category="Process Analysis",

                    severity="HIGH",

                    raw_score=30,

                    description=(
                        f"Unknown process detected (PID {process['pid']})."
                    ),

                    recommendation="Investigate the process.",

                    module="Process Analyzer"

                )

            )

            continue

        if process["is_temp"] and not trusted:

            findings.append(

                FindingFactory.create(

                    title="Process Running From Temp",

                    category="Process Analysis",

                    severity="HIGH",

                    raw_score=30,

                    description=(
                        f"{process['name']} is executing from {process['path']}"
                    ),

                    recommendation="Investigate the executable.",

                    module="Process Analyzer"

                )

            )

            continue

        if process["is_appdata"] and not trusted:

            findings.append(

                FindingFactory.create(

                    title="Process Running From AppData",

                    category="Process Analysis",

                    severity="MEDIUM",

                    raw_score=15,

                    description=(
                        f"{process['name']} is executing from an untrusted AppData location."
                    ),

                    recommendation="Verify whether this application is trusted.",

                    module="Process Analyzer"

                )

            )

            continue

        if (

            process["missing_path"]

            and process["name"] not in SYSTEM_PROCESSES

        ):

            findings.append(

                FindingFactory.create(

                    title="Process Path Unavailable",

                    category="Process Analysis",

                    severity="LOW",

                    raw_score=5,

                    description=(
                        f"Executable path for {process['name']} could not be determined."
                    ),

                    recommendation=(
                        "Review process permissions and executable location."
                    ),

                    module="Process Analyzer"

                )

            )

            continue

        if process["cpu"] > 80:

            findings.append(

                FindingFactory.create(

                    title="High CPU Usage",

                    category="Process Analysis",

                    severity="MEDIUM",

                    raw_score=15,

                    description=(
                        f"{process['name']} is consuming {process['cpu']}% CPU."
                    ),

                    recommendation="Investigate unusually high processor usage.",

                    module="Process Analyzer"

                )

            )

            continue

        if process["memory"] > 30:

            findings.append(

                FindingFactory.create(

                    title="High Memory Usage",

                    category="Process Analysis",

                    severity="LOW",

                    raw_score=5,

                    description=(
                        f"{process['name']} is consuming {process['memory']}% memory."
                    ),

                    recommendation="Review memory consumption for abnormal behavior.",

                    module="Process Analyzer"

                )

            )

    # --------------------------------------------------
    # File Integrity
    # --------------------------------------------------

    for file in file_results:

        if file["status"] == "MODIFIED":

            findings.append(

                FindingFactory.create(

                    title="Modified File",

                    category="File Integrity",

                    severity="MEDIUM",

                    raw_score=15,

                    description=(
                        f"{file['file']} has changed since the previous scan."
                    ),

                    recommendation="Verify the file modification.",

                    module="File Integrity"

                )

            )

    # --------------------------------------------------
    # Firewall
    # --------------------------------------------------

    firewall_profiles = security_info.get(

        "firewall_status",

        []

    )

    if isinstance(firewall_profiles, dict):

        firewall_profiles = [firewall_profiles]

    for profile in firewall_profiles:

        if not profile.get("Enabled", True):

            findings.append(

                FindingFactory.create(

                    title="Firewall Disabled",

                    category="Windows Security",

                    severity="CRITICAL",

                    raw_score=50,

                    description=(
                        f"{profile['Name']} firewall profile is disabled."
                    ),

                    recommendation="Enable Windows Firewall immediately.",

                    module="Windows Audit"

                )

            )

        # --------------------------------------------------
    # Risk Calculation
    # --------------------------------------------------

    raw_score = sum(

        finding.raw_score

        for finding in findings

    )

    normalized_score = min(

        raw_score,

        100

    )

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
    # Overall Endpoint Risk
    # --------------------------------------------------

    if normalized_score >= 75:

        level = "CRITICAL"

    elif normalized_score >= 50:

        level = "HIGH"

    elif normalized_score >= 25:

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