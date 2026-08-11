import streamlit as st
import hashlib

APP_PASSWORD = "1236"


def check_password():

    if st.session_state.get("authenticated"):
        return True

    st.title("🔒 Login")

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Login"):

        password_hash = hashlib.sha256(
            password.encode()
        ).hexdigest()

        app_hash = hashlib.sha256(
            APP_PASSWORD.encode()
        ).hexdigest()

        if password_hash == app_hash:

            st.session_state["authenticated"] = True
            st.rerun()

        else:

            st.error(
                "Wrong password"
            )

    return False
