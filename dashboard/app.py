from pathlib import Path

import streamlit as st

from dashboard.components.header import render_header
from dashboard.components.metric_cards import render_metric_cards
from dashboard.components.endpoint_card import render_endpoint
from dashboard.components.findings_table import render_findings

from core.scan_runner import run_scan

from dashboard.dashboard_db import (
    get_latest_scan,
    get_latest_findings,
    get_scan_history
)


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
        page_icon="🛡️",
        layout="wide"
    )

    render_header()

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

                run_scan()

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

    scan = get_latest_scan()

    findings = get_latest_findings()

    history = get_scan_history()

    render_metric_cards(scan)

    st.divider()

    render_endpoint(scan)

    st.divider()

    render_findings(
        findings,
        history
    )

    st.divider()

    st.caption(
        f"Last Scan : {scan['scan_time']}"
    )

    st.caption(
        "CyberGuard v1.0 | Internship Project"
    )


if __name__ == "__main__":

    run_dashboard()