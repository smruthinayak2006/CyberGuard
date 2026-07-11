import streamlit as st


def render_header():

    left, right = st.columns([5, 1.5])

    with left:

        st.title("🛡 CyberGuard Security Center")

        st.caption(
            "Enterprise Endpoint Security Assessment Platform"
        )

    with right:

        st.markdown(
            """
            <div style="
                background:#123d24;
                color:#5cff8d;
                padding:18px;
                border-radius:10px;
                text-align:center;
                font-weight:700;
                font-size:20px;
            ">
                🟢 ONLINE
            </div>
            """,
            unsafe_allow_html=True
        )

    st.divider()