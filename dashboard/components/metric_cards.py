import streamlit as st


def render_metric_cards():

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            "Overall Risk",
            "HIGH"
        )

    with col2:

        st.metric(
            "Findings",
            "1"
        )

    with col3:

        st.metric(
            "Endpoint",
            "Smriti"
        )

    with col4:

        st.metric(
            "Last Scan",
            "Today"
        )