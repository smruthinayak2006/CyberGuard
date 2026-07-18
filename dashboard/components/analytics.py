import pandas as pd
import streamlit as st


def render_analytics(history):

    st.subheader("📊 Security Analytics")

    if not history:

        st.info("No scan history available.")

        return

    df = pd.DataFrame(

        history,

        columns=[
            "Scan Time",
            "Risk",
            "Score",
            "Findings"
        ]

    )

    history_df = df.iloc[::-1].reset_index(drop=True)

    # ----------------------------------------------------
    # Analytics Summary
    # ----------------------------------------------------

    total_scans = len(history_df)

    avg_score = round(history_df["Score"].mean(), 1)

    max_score = history_df["Score"].max()

    latest_risk = history_df.iloc[-1]["Risk"]

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Total Assessments",
        total_scans
    )

    c2.metric(
        "Average Risk Score",
        avg_score
    )

    c3.metric(
        "Highest Risk Score",
        max_score
    )

    c4.metric(
        "Latest Risk Level",
        latest_risk
    )

    st.divider()

    # ----------------------------------------------------
    # Risk Score Trend
    # ----------------------------------------------------

    left, right = st.columns(2)

    with left:

        st.markdown("#### Risk Score Trend")

        chart = history_df[
            ["Scan Time", "Score"]
        ].copy()

        chart.set_index(
            "Scan Time",
            inplace=True
        )

        st.line_chart(
            chart,
            use_container_width=True
        )

    # ----------------------------------------------------
    # Findings Trend
    # ----------------------------------------------------

    with right:

        st.markdown("#### Findings Per Assessment")

        findings = history_df[
            ["Scan Time", "Findings"]
        ].copy()

        findings.set_index(
            "Scan Time",
            inplace=True
        )

        st.bar_chart(
            findings,
            use_container_width=True
        )

    st.divider()

    # ----------------------------------------------------
    # Risk Distribution
    # ----------------------------------------------------

    st.markdown("#### Risk Level Distribution")

    risk_counts = (

        history_df["Risk"]
        .value_counts()
        .sort_index()

    )

    st.bar_chart(

        risk_counts,

        use_container_width=True

    )