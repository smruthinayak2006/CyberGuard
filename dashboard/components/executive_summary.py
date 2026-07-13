import streamlit as st


def render_executive_summary(scan, findings):

    st.subheader("📋 Executive Security Summary")

    critical = 0
    high = 0
    medium = 0
    low = 0

    modules = {}

    for finding in findings:

        severity = str(finding[2]).upper()

        if severity == "CRITICAL":
            critical += 1

        elif severity == "HIGH":
            high += 1

        elif severity == "MEDIUM":
            medium += 1

        elif severity == "LOW":
            low += 1

        module = finding[3]

        modules[module] = modules.get(module, 0) + 1

    if modules:

        top_module = max(
            modules,
            key=modules.get
        )

    else:

        top_module = "None"

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Critical Findings",
            critical
        )

        st.metric(
            "High Findings",
            high
        )

    with col2:

        st.metric(
            "Medium Findings",
            medium
        )

        st.metric(
            "Low Findings",
            low
        )

    with col3:

        st.metric(
            "Top Risk Module",
            top_module
        )

        st.metric(
            "Security Posture",
            scan["risk_level"]
        )

    st.caption(
        f"Latest Assessment : {scan['scan_time']}"
    )