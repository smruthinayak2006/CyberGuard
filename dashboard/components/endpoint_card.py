import streamlit as st


def render_endpoint(scan):

    st.subheader("🖥 Endpoint Overview")

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("#### System Information")

        st.write(f"**Hostname:** {scan['hostname']}")

        st.write(f"**Operating System:** {scan['operating_system']}")

        st.write(f"**IP Address:** {scan['ip_address']}")

        st.write(f"**Last Scan:** {scan['scan_time']}")

    with col2:

        st.markdown("#### Resource Usage")

        st.write("**CPU Usage**")

        st.progress(min(int(scan["cpu_usage"]), 100))

        st.caption(f"{scan['cpu_usage']} %")

        st.write("**RAM Usage**")

        st.progress(min(int(scan["ram_usage"]), 100))

        st.caption(f"{scan['ram_usage']} %")

        st.write("**Disk Usage**")

        st.progress(min(int(scan["disk_usage"]), 100))

        st.caption(f"{scan['disk_usage']} %")