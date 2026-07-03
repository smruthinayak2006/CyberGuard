import streamlit as st
from dashboard.components.header import render_header
from dashboard.components.metric_cards import render_metric_cards
from dashboard.components.endpoint_card import render_endpoint
from dashboard.components.findings_table import render_findings

from core.scan_runner import run_scan

from dashboard.dashboard_db import (
    get_latest_findings,
    get_finding_count
)


def run_dashboard():

    st.set_page_config(
        page_title="CyberGuard Security Center",
        page_icon="🛡️",
        layout="wide"
    )

    render_header()

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

    findings = get_latest_findings()

    count = get_finding_count()

    risk = "LOW"

    for finding in findings:

        if finding[2] == "CRITICAL":

            risk = "CRITICAL"

            break

        elif finding[2] == "HIGH":

            risk = "HIGH"

    render_metric_cards(

        risk,

        count,

        "Smriti"

    )

    st.divider()

    render_endpoint()

    st.divider()

    render_findings()