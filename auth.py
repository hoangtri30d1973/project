import streamlit as st

PROJECT_PASSWORD = "hmt1236"


def check_project_password():

    if st.session_state.get("project_authenticated"):
        return True

    st.title("❌")

    password = st.text_input(
        "Enter password",
        type="password"
    )

    if st.button("Unlock"):

        if password == PROJECT_PASSWORD:

            st.session_state[
                "project_authenticated"
            ] = True

            st.rerun()

        else:

            st.error(
                "Wrong password"
            )

    return False
