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

    col1, col2 = st.columns(2)

    # ----------------------------------------------------
    # Risk Score Trend
    # ----------------------------------------------------

    with col1:

        st.markdown("#### Risk Score Trend")

        chart = df[

            ["Scan Time", "Score"]

        ].copy()

        chart = chart.iloc[::-1]

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

    with col2:

        st.markdown("#### Findings Per Scan")

        findings = df[

            ["Scan Time", "Findings"]

        ].copy()

        findings = findings.iloc[::-1]

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

        df["Risk"]

        .value_counts()

        .sort_index()

    )

    st.bar_chart(

        risk_counts,

        use_container_width=True

    )
    