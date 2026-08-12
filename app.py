import streamlit as st

st.markdown(
    """
    <style>
    #MainMenu {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True
)

from database import init_db

init_db()

st.set_page_config(
    page_title="Project Manager",
    page_icon="✳️",
    layout="wide"
)

st.title("📁 Project Manager")

st.markdown("""
### Chào mừng đến với phần mềm tự quản lý dự án của bạn!

Chọn menu bên trái:

- Dashboard
- Projects
- Reports
""")
