import streamlit as st


def render_security_scorecard(scan, findings):

    st.subheader("🛡 Endpoint Security Scorecard")

    score = 100

    checks = []

    # -------------------------------------------------------
    # Firewall
    # -------------------------------------------------------

    firewall_ok = True

    firewall_profiles = scan["security"].get(
        "Firewall Status",
        []
    )

    for profile in firewall_profiles:

        if not profile["Enabled"]:

            firewall_ok = False

    if firewall_ok:

        checks.append(

            ("🟢", "Windows Firewall Enabled")

        )

    else:

        checks.append(

            ("🔴", "Windows Firewall Disabled")

        )

        score -= 30

    # -------------------------------------------------------
    # File Integrity
    # -------------------------------------------------------

    modified = False

    for file in scan["files"]:

        if file["status"] == "MODIFIED":

            modified = True

    if modified:

        checks.append(

            ("🟡", "Modified Files Detected")

        )

        score -= 15

    else:

        checks.append(

            ("🟢", "File Integrity Verified")

        )

    # -------------------------------------------------------
    # Unknown Process
    # -------------------------------------------------------

    unknown = False

    for process in scan["processes"]:

        if process["name"] == "Unknown":

            unknown = True

    if unknown:

        checks.append(

            ("🟡", "Unknown Process Detected")

        )

        score -= 20

    else:

        checks.append(

            ("🟢", "Running Processes Verified")

        )

    # -------------------------------------------------------
    # Windows Updates
    # -------------------------------------------------------

    updates = scan["security"].get(

        "Installed Updates",

        []

    )

    if len(updates) > 0:

        checks.append(

            ("🟢", "Windows Updates Installed")

        )

    else:

        checks.append(

            ("🔴", "No Windows Updates Found")

        )

        score -= 20

    # -------------------------------------------------------
    # Scan Status
    # -------------------------------------------------------

    checks.append(

        ("🟢", "Assessment Completed Successfully")

    )

    # -------------------------------------------------------
    # Overall Score
    # -------------------------------------------------------

    score = max(

        score,

        0

    )

    left, right = st.columns(

        [3, 1]

    )

    with left:

        for icon, text in checks:

            st.markdown(

                f"### {icon} {text}"

            )

    with right:

        if score >= 90:

            color = "🟢"

        elif score >= 70:

            color = "🟡"

        else:

            color = "🔴"

        st.metric(

            "Security Score",

            f"{score}/100"

        )

        st.markdown(

            f"## {color}"
        )