"""
CyberGuard Risk Scoring Engine
------------------------------
Calculates an overall endpoint risk score based on
security findings collected from different modules.
"""


def calculate_risk(system_info, security_info, processes, file_results):

    score = 0
    findings = []

    # --------------------------------------------------
    # Firewall Checks
    # --------------------------------------------------

    firewall_profiles = security_info.get("Firewall Status", [])

    for profile in firewall_profiles:

        if not profile.get("Enabled", False):

            score += 30

            findings.append(
                f"Firewall disabled ({profile.get('Name', 'Unknown')})"
            )

    # --------------------------------------------------
    # Guest Account
    # --------------------------------------------------

    users = security_info.get("Local Users", [])

    for user in users:

        if (
            user.get("Name") == "Guest"
            and user.get("Enabled") is True
        ):

            score += 20

            findings.append(
                "Guest account is enabled."
            )

    # --------------------------------------------------
    # Windows Updates
    # --------------------------------------------------

    updates = security_info.get("Installed Updates", [])

    if len(updates) < 3:

        score += 15

        findings.append(
            "Very few Windows updates detected."
        )

    # --------------------------------------------------
    # File Integrity
    # --------------------------------------------------

    for file in file_results:

        if file["status"] == "MODIFIED":

            score += 15

            findings.append(
                f"Modified file: {file['file']}"
            )

    # --------------------------------------------------
    # Unknown Processes
    # --------------------------------------------------

    for process in processes:

        if process["name"] == "Unknown":

            score += 10

            findings.append(
                f"Unknown process (PID {process['pid']})"
            )

    # --------------------------------------------------
    # Missing Executable Path
    # --------------------------------------------------

    for process in processes:

        if process["path"] in ("", "Unavailable"):

            score += 5

            findings.append(
                f"Executable path unavailable (PID {process['pid']})"
            )

    # --------------------------------------------------
    # High Memory Processes
    # --------------------------------------------------

    for process in processes:

        if process["memory"] > 10:

            score += 10

            findings.append(
                f"High memory usage process: {process['name']}"
            )

    # --------------------------------------------------
    # Suspicious Execution Locations
    # --------------------------------------------------

    suspicious_locations = [

        "downloads",
        "temp",
        "appdata",
        "roaming"

    ]

    for process in processes:

        path = process["path"].lower()

        if any(folder in path for folder in suspicious_locations):

            score += 20

            findings.append(
                f"Suspicious execution path: {process['name']}"
            )

    # --------------------------------------------------
    # System Resource Checks
    # --------------------------------------------------

    if system_info["cpu_usage"] > 90:

        score += 10

        findings.append(
            "High CPU usage detected."
        )

    if system_info["ram_usage"] > 85:

        score += 10

        findings.append(
            "High RAM usage detected."
        )

    # --------------------------------------------------
    # Cap Score
    # --------------------------------------------------

    score = min(score, 100)

    # --------------------------------------------------
    # Risk Level
    # --------------------------------------------------

    if score <= 20:

        level = "LOW"

    elif score <= 40:

        level = "MEDIUM"

    elif score <= 70:

        level = "HIGH"

    else:

        level = "CRITICAL"

    return {

        "score": score,

        "level": level,

        "findings": findings,

        "finding_count": len(findings)

    }