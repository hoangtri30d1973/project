import streamlit as st
from database import init_db

init_db()

st.set_page_config(
    page_title="Project Manager",
    page_icon="✳️",
    layout="wide"
)

st.title("📁 Project Manager")

st.markdown("""
### Chào mừng đến với phần mềm quản lý dự án cá nhân của ___H___M___T___!

Chọn các chức năng chính ở menu bên trái:

- Dashboard
- Projects
- Reports
""")
