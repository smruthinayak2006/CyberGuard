import pandas as pd
import streamlit as st


def render_auth_logs(logs):

    st.subheader("🔐 Authentication Audit Logs")

    if not logs:

        st.info("No authentication activity recorded.")

        return

    data = []

    for username, status, login_time in logs:

        if status == "SUCCESS":

            badge = "🟢 SUCCESS"

        else:

            badge = "🔴 FAILED"

        data.append({

            "User": username,

            "Status": badge,

            "Login Time": login_time

        })

    df = pd.DataFrame(data)

    st.dataframe(

        df,

        use_container_width=True,

        hide_index=True

    )