import streamlit as st
from database import get_conn

st.set_page_config(
    page_title="Dashboard",
    layout="wide"
)

conn = get_conn()

projects = conn.execute(
    "SELECT COUNT(*) FROM projects"
).fetchone()[0]

tasks = conn.execute(
    "SELECT COUNT(*) FROM tasks"
).fetchone()[0]

todo = conn.execute(
    """
    SELECT COUNT(*)
    FROM tasks
    WHERE status='TODO'
    """
).fetchone()[0]

doing = conn.execute(
    """
    SELECT COUNT(*)
    FROM tasks
    WHERE status='IN_PROGRESS'
    """
).fetchone()[0]

done = conn.execute(
    """
    SELECT COUNT(*)
    FROM tasks
    WHERE status='DONE'
    """
).fetchone()[0]

conn.close()

st.title("ℹ️ Dashboard")

c1, c2, c3, c4, c5 = st.columns(5)

c1.metric("Projects", projects)
c2.metric("Tasks", tasks)
c3.metric("TODO", todo)
c4.metric("Doing", doing)
c5.metric("Done", done)
