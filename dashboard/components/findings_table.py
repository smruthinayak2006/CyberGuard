import pandas as pd
import streamlit as st


def render_findings(findings, history):

    # ==========================================================
    # Recent Findings
    # ==========================================================

    st.subheader("🚨 Recent Security Findings")

    if findings:

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

        # ------------------------------------------------------
        # Explorer Filters
        # ------------------------------------------------------

        col1, col2, col3 = st.columns(3)

        with col1:

            search = st.text_input(
                "🔍 Search",
                placeholder="Finding title..."
            )

        with col2:

            severity = st.selectbox(

                "Severity",

                [

                    "ALL",

                    "CRITICAL",

                    "HIGH",

                    "MEDIUM",

                    "LOW"

                ]

            )

        with col3:

            modules = ["ALL"]

            modules.extend(

                sorted(df["Module"].unique())

            )

            module = st.selectbox(

                "Module",

                modules

            )

        # ------------------------------------------------------
        # Apply Filters
        # ------------------------------------------------------

        if search:

            df = df[

                df["Title"]

                .str.contains(

                    search,

                    case=False,

                    na=False

                )

            ]

        if severity != "ALL":

            df = df[

                df["Severity"] == severity

            ]

        if module != "ALL":

            df = df[

                df["Module"] == module

            ]

        # ------------------------------------------------------
        # Styling
        # ------------------------------------------------------

        def highlight(value):

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

            highlight,

            subset=["Severity"]

        )

        st.dataframe(

            styled,

            use_container_width=True,

            hide_index=True

        )

    else:

        st.success(

            "No findings available."

        )

    st.divider()

    # ==========================================================
    # Scan History
    # ==========================================================

    st.subheader("📜 Scan History")

    if history:

        rows = []

        for scan in history:

            rows.append({

                "Scan Time": scan[0],
                "Risk": scan[1],
                "Score": scan[2],
                "Findings": scan[3]

            })

        history_df = pd.DataFrame(rows)

        st.dataframe(

            history_df,

            use_container_width=True,

            hide_index=True

        )

    else:

        st.info(

            "No previous scans available."

        )