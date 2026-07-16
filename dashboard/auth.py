import streamlit as st

USERNAME = "admin"
PASSWORD = "CyberGuard@123"


def login():

    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False

    if st.session_state.authenticated:
        return True

    st.title("🔐 CyberGuard Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login", use_container_width=True):

        if username == USERNAME and password == PASSWORD:

            st.session_state.authenticated = True
            st.success("Login successful.")
            st.rerun()

        else:

            st.error("Invalid username or password.")

    return False


def logout():

    st.sidebar.title("🛡 CyberGuard")

    st.sidebar.divider()

    st.sidebar.markdown("### 👤 User")
    st.sidebar.success("admin")

    st.sidebar.markdown("### 🟢 Status")
    st.sidebar.success("Authenticated")

    # -------------------------
    # Security Posture
    # -------------------------

    st.sidebar.markdown("### 🛡 Security Posture")

    if st.session_state.get("latest_scan"):

        risk = st.session_state.latest_scan["risk"]

        score = risk["score"]
        level = risk["level"]

        if level == "LOW":
            st.sidebar.success(f"🟢 LOW ({score}/100)")

        elif level == "MEDIUM":
            st.sidebar.warning(f"🟡 MEDIUM ({score}/100)")

        elif level == "HIGH":
            st.sidebar.error(f"🟠 HIGH ({score}/100)")

        else:
            st.sidebar.error(f"🔴 CRITICAL ({score}/100)")

    else:

        st.sidebar.info("No scan executed.")

    st.sidebar.divider()

    if st.session_state.get("latest_scan"):

        system = st.session_state.latest_scan["system"]

        st.sidebar.markdown("### 💻 Endpoint")
        st.sidebar.write(system["hostname"])

        st.sidebar.markdown("### 🕒 Last Scan")
        st.sidebar.write(
            st.session_state.get(
                "scan_time",
                "No scans yet"
            )
        )

        st.sidebar.divider()

    st.sidebar.caption("CyberGuard v1.0")

    if st.sidebar.button(
        "🚪 Logout",
        use_container_width=True
    ):

        st.session_state.authenticated = False
        st.rerun()

    