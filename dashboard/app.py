from pathlib import Path

import streamlit as st

from core.scan_runner import run_scan
from dashboard.auth import login, logout
from dashboard.components import auth_logs
from dashboard.components.auth_logs import render_auth_logs

from dashboard.dashboard_db import (
    get_latest_scan,
    get_latest_findings,
    get_scan_history,
    get_auth_logs
)

from dashboard.components.header import render_header
from dashboard.components.metric_cards import render_metric_cards
from dashboard.components.endpoint_card import render_endpoint
from dashboard.components.analytics import render_analytics
from dashboard.components.findings_table import render_findings
from dashboard.components.recommendations import render_recommendations
from dashboard.components.security_scorecard import render_security_scorecard
from dashboard.components.executive_summary import render_executive_summary


REPORTS_DIR = Path("reports")


def get_latest_report():

    reports = sorted(
        REPORTS_DIR.glob("CyberGuard_Report_*.pdf"),
        key=lambda file: file.stat().st_mtime,
        reverse=True
    )

    if reports:
        return reports[0]

    return None


def run_dashboard():

    st.set_page_config(
        page_title="CyberGuard Security Center",
        page_icon="🛡",
        layout="wide"
    )

    if not login():
        return

    logout()
    render_header()

    # ----------------------------------------------------
    # Session State
    # ----------------------------------------------------

    if "latest_scan" not in st.session_state:

        st.session_state.latest_scan = None

    # ----------------------------------------------------
    # Action Buttons
    # ----------------------------------------------------

    left, right = st.columns([3, 1])

    with left:

        if st.button(
            "▶ Start Assessment",
            use_container_width=True
        ):

            with st.spinner(
                "Running endpoint assessment..."
            ):

                st.session_state.latest_scan = run_scan()

            st.success(
                "Assessment completed successfully."
            )

            st.rerun()

    with right:

        latest_report = get_latest_report()

        if latest_report:

            with open(latest_report, "rb") as pdf:

                st.download_button(
                    "📄 Download Report",
                    pdf,
                    file_name=latest_report.name,
                    mime="application/pdf",
                    use_container_width=True
                )

    # ----------------------------------------------------
    # Database Data
    # ----------------------------------------------------

    scan = get_latest_scan()
    if scan:
        st.session_state.scan_time = scan["scan_time"]
    
    findings = get_latest_findings()

    history = get_scan_history()
    auth_logs = get_auth_logs()

    # ----------------------------------------------------
    # Endpoint Security Scorecard
    # ----------------------------------------------------

    if st.session_state.latest_scan is not None:

        render_security_scorecard(

            st.session_state.latest_scan,

            findings

        )

        st.divider()

    # ----------------------------------------------------
    # Executive Security Summary
    # ----------------------------------------------------

    render_executive_summary(

        scan,

        findings

    )

    st.divider()

    # ----------------------------------------------------
    # Dashboard
    # ----------------------------------------------------

    render_metric_cards(

        scan

    )

    st.divider()

    render_endpoint(

        scan

    )

    st.divider()

    render_analytics(

        history

    )

    st.divider()

    render_findings(

        findings,

        history

    )

    st.divider()

    render_recommendations(

        findings

    )

    st.divider()

    render_auth_logs(

        auth_logs

    )

    st.caption(

        f"Last Scan : {scan['scan_time']}"

    )

    st.caption(

        "CyberGuard v1.0 | Internship Project"

    )


if __name__ == "__main__":

    run_dashboard()