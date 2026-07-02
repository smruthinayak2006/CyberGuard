import streamlit as st


def render_header():

    col1, col2 = st.columns([6, 1])

    with col1:

        st.title("🛡 CyberGuard Security Center")

        st.caption(
            "Enterprise Endpoint Security Assessment Platform"
        )

    with col2:

        st.success("🟢 ONLINE")

    st.divider()