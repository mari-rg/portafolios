from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="mi escena · Interfaces multimodales",
    page_icon="💖",
    layout="wide",
)

# Quita el margen y el encabezado de Streamlit para que se vea la página completa
st.markdown(
    """
    <style>
    header, footer, #MainMenu {visibility: hidden;}
    .block-container {padding: 0 !important; max-width: 100% !important;}
    </style>
    """,
    unsafe_allow_html=True,
)

html = Path(__file__).with_name("index.html").read_text(encoding="utf-8")
components.html(html, height=1400, scrolling=True)
