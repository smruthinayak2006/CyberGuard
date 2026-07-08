import streamlit as st


def render_metric_cards(scan):

    risk = scan["risk_level"]

    if risk == "CRITICAL":
        icon = "🔴"
    elif risk == "HIGH":
        icon = "🟠"
    elif risk == "MEDIUM":
        icon = "🟡"
    else:
        icon = "🟢"

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(

            "Overall Risk",

            f"{icon} {risk}"

        )

    with col2:

        st.metric(

            "Risk Score",

            f"{scan['normalized_score']} / 100"

        )

    with col3:

        st.metric(

            "Findings",

            scan["finding_count"]

        )

    with col4:

        st.metric(

            "Endpoint",

            scan["hostname"]

        )