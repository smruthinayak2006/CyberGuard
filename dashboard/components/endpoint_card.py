import streamlit as st


def render_endpoint():

    st.subheader("🖥 Endpoint Overview")

    col1, col2 = st.columns(2)

    with col1:

        st.write("**Hostname**")

        st.write("Smriti")

        st.write("**Operating System**")

        st.write("Windows")

        st.write("**IP Address**")

        st.write("10.227.249.223")

    with col2:

        st.write("**CPU Usage**")

        st.write("22.9 %")

        st.write("**RAM Usage**")

        st.write("78.1 %")

        st.write("**Disk Usage**")

        st.write("17.3 %")