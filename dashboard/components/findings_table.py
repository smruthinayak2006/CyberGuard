import pandas as pd
import streamlit as st


def render_findings(findings):

    st.subheader("🚨 Recent Security Findings")

    if not findings:

        st.success("No findings available.")

        return

    data = []

    for finding in findings:

        data.append({

            "Finding ID": finding[0],

            "Title": finding[1],

            "Severity": finding[2],

            "Module": finding[3],

            "Status": finding[4],

            "Timestamp": finding[5]

        })

    df = pd.DataFrame(data)

    def highlight_severity(value):

        if value == "CRITICAL":

            return "background-color:#8B0000;color:white;font-weight:bold;"

        if value == "HIGH":

            return "background-color:#ff4b4b;color:white;font-weight:bold;"

        if value == "MEDIUM":

            return "background-color:#ffb000;color:black;font-weight:bold;"

        if value == "LOW":

            return "background-color:#00b050;color:white;font-weight:bold;"

        return ""

    styled = df.style.map(

        highlight_severity,

        subset=["Severity"]

    )

    st.dataframe(

        styled,

        use_container_width=True,

        hide_index=True

    )