import streamlit as st

from dashboard.components.header import render_header
from dashboard.components.metric_cards import render_metric_cards
from dashboard.components.endpoint_card import render_endpoint
from dashboard.components.findings_table import render_findings

from core.scan_runner import run_scan

from dashboard.dashboard_db import (
    get_latest_scan,
    get_latest_findings
)


def run_dashboard():

    st.set_page_config(
        page_title="CyberGuard Security Center",
        page_icon="🛡️",
        layout="wide"
    )

    st.sidebar.title("🛡 CyberGuard")

    st.sidebar.success("System Online")

    st.sidebar.markdown("---")

    st.sidebar.write("### Assessment")

    if st.sidebar.button(
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

    st.sidebar.markdown("---")

    st.sidebar.caption("Version 1.0")

    render_header()

    scan = get_latest_scan()

    findings = get_latest_findings()

    render_metric_cards(scan)

    st.divider()

    render_endpoint(scan)

    st.divider()

    render_findings(findings)

    st.divider()

    st.caption(
        f"Last Scan: {scan['scan_time']}"
    )

    st.caption(
        "CyberGuard • Endpoint Security Assessment Platform"
    )