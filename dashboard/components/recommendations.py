import streamlit as st


def render_recommendations(findings):

    st.subheader("💡 Security Recommendations")

    if not findings:
        st.success("No security recommendations available.")
        return

    shown = set()

    for finding in findings:

        title = finding[1]
        severity = finding[2]
        recommendation = finding[6]

        key = (title, recommendation)

        if key in shown:
            continue

        shown.add(key)

        if severity == "CRITICAL":
            st.error(
                f"**{title}**\n\n{recommendation}"
            )

        elif severity == "HIGH":
            st.warning(
                f"**{title}**\n\n{recommendation}"
            )

        elif severity == "MEDIUM":
            st.info(
                f"**{title}**\n\n{recommendation}"
            )

        else:
            st.success(
                f"**{title}**\n\n{recommendation}"
            )