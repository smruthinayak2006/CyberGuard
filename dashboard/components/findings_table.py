import pandas as pd
import streamlit as st


def render_findings():

    st.subheader("🚨 Recent Findings")

    df = pd.DataFrame(

        [

            {

                "Finding ID": "CG-0001",

                "Severity": "HIGH",

                "Module": "Process Analyzer",

                "Status": "OPEN"

            }

        ]

    )

    st.dataframe(

        df,

        use_container_width=True,

        hide_index=True

    )