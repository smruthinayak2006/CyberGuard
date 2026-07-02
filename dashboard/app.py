import streamlit as st

from components.header import render_header
from components.metric_cards import render_metric_cards
from components.endpoint_card import render_endpoint
from components.findings_table import render_findings


st.set_page_config(

    page_title="CyberGuard Security Center",

    page_icon="🛡️",

    layout="wide"

)


render_header()

render_metric_cards()

st.divider()

render_endpoint()

st.divider()

render_findings()