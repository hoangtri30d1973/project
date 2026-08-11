import streamlit as st
from database import init_db
from auth import check_password
import hashlib

APP_PASSWORD_HASH = hashlib.sha256(
    "1236".encode()
).hexdigest()


def check_password():

    if st.session_state.get("authenticated"):
        return True

    st.title("🔒 Project Manager Login")

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Login"):

        password_hash = hashlib.sha256(
            password.encode()
        ).hexdigest()

        if password_hash == APP_PASSWORD_HASH:

            st.session_state["authenticated"] = True
            st.rerun()

        else:

            st.error(
                "Invalid password"
            )

    return False


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
