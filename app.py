import streamlit as st
from database import init_db
from auth import check_password

init_db()

st.set_page_config(
    page_title="Project Manager",
    page_icon="✳️",
    layout="wide"
)

if not check_password():
    st.stop()

st.title("📁 Project Manager")

st.markdown("""
### Chào mừng đến với phần mềm tự quản lý dự án của bạn!

Chọn menu bên trái:

- Dashboard
- Projects
- Reports
""")

if st.sidebar.button("🚪 Logout"):
    st.session_state.authenticated = False
    st.rerun()
