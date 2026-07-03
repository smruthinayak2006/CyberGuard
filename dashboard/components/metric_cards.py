import streamlit as st


def render_metric_cards(risk, findings, endpoint):

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            "Overall Risk",
            risk
        )

    with col2:

        st.metric(
            "Findings",
            findings
        )

    with col3:

        st.metric(
            "Endpoint",
            endpoint
        )

    with col4:

        st.metric(
            "Status",
            "ONLINE"
        )