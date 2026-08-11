import streamlit as st
import pandas as pd
from database import get_conn
   
st.title("📁 Project Management")

tab1, tab2 = st.tabs(
    [
        "Projects",
        "Create Project"
    ]
)

with tab2:

    name = st.text_input(
        "Project Name"
    )

    desc = st.text_area(
        "Description"
    )

    if st.button("Save Project"):

        conn = get_conn()

        conn.execute(
            """
            INSERT INTO projects
            (
                name,
                description
            )
            VALUES (?,?)
            """,
            (
                name,
                desc
            )
        )

        conn.commit()
        conn.close()

        st.success("Saved")
        st.rerun()

with tab1:

    conn = get_conn()

    projects = pd.read_sql_query(
        """
        SELECT *
        FROM projects
        ORDER BY id DESC
        """,
        conn
    )

    conn.close()

    st.dataframe(
        projects,
        use_container_width=True
    )

    if not projects.empty:

        projects["display"] = (
            projects["id"].astype(str)
            + " - "
            + projects["name"]
        )

        selected_project = st.selectbox(
            "Project",
            projects["display"]
        )
        project_id = int(
            selected_project.split(" - ")[0]
        )

        st.subheader("New Task")

        task_name = st.text_input(
            "Task Name"
        )

        task_desc = st.text_area(
            "Task Description"
        )

        col1, col2, col3 = st.columns(3)

        priority = col1.selectbox(
            "Priority",
            [
                "LOW",
                "MEDIUM",
                "HIGH",
                "CRITICAL"
            ]
        )

        status = col2.selectbox(
            "Status",
            [
                "TODO",
                "IN_PROGRESS",
                "WAITING",
                "DONE"
            ]
        )

        due_date = col3.date_input(
            "Due Date"
        )

        if st.button("Create Task"):

            conn = get_conn()

            conn.execute(
                """
                INSERT INTO tasks
                (
                    project_id,
                    title,
                    description,
                    priority,
                    status,
                    due_date
                )
                VALUES (?,?,?,?,?,?)
                """,
                (
                    int(project_id),
                    task_name,
                    task_desc,
                    priority,
                    status,
                    str(due_date)
                )
            )

            conn.commit()
            conn.close()

            st.success("Task created")
            st.rerun()

        search = st.text_input(
            "Search Task"
        )

        filter_status = st.selectbox(
            "Filter",
            [
                "ALL",
                "TODO",
                "IN_PROGRESS",
                "WAITING",
                "DONE"
            ]
        )

        conn = get_conn()

        tasks = pd.read_sql_query(
            """
            SELECT *
            FROM tasks
            WHERE project_id = ?
            ORDER BY id DESC
            """,
            conn,
            params=[int(project_id)]
        )

        conn.close()

        if filter_status != "ALL":

            tasks = tasks[
                tasks["status"]
                == filter_status
            ]

        for _, task in tasks.iterrows():

            with st.expander(
                f"{task['title']} | {task['status']}"
            ):

                st.write(
                    task["description"]
                )

                st.info(
                    f"""
Priority: {task['priority']}
Due Date: {task['due_date']}
"""
                )
                st.subheader("Update Status")

                new_status = st.selectbox(
                    "Status",
                    [
                        "TODO",
                        "IN_PROGRESS",
                        "WAITING",
                        "DONE"
                    ],
                    index=[
                        "TODO",
                        "IN_PROGRESS",
                        "WAITING",
                        "DONE"
                    ].index(task["status"]),
                    key=f"status_{task['id']}"
                )

                if st.button(
                    "Save Status",
                    key=f"save_status_{task['id']}"
                ):

                    conn = get_conn()

                    conn.execute(
                        """
                        UPDATE tasks
                        SET status = ?
                        WHERE id = ?
                        """,
                        (
                            new_status,
                            task["id"]
                        )
                    )

                    conn.commit()
                    conn.close()

                    st.success("Status updated")
                    st.rerun()

                if st.button(
                    "Delete Task",
                    key=f"delete_task_{task['id']}"
                ):
                    conn = get_conn()
                    conn.execute(
                        """
                        DELETE FROM notes
                        WHERE task_id=?
                        """,
                        (task["id"],)
                    )
                    conn.execute(
                        """
                        DELETE FROM tasks
                        WHERE id=?
                        """,
                        (task["id"],)
                    )
                    conn.commit()
                    conn.close()
                    st.success(
                        "Task deleted"
                    )
                    st.rerun()

                conn = get_conn()

                notes = pd.read_sql_query(
                    """
                    SELECT *
                    FROM notes
                    WHERE task_id=?
                    ORDER BY id DESC
                    """,
                    conn,
                    params=[task["id"]]
                )

                conn.close()

                st.subheader("Notes")

                for _, note in notes.iterrows():
                
                    col1, col2 = st.columns(
                        [10, 1]
                    )

                    with col1:
                    
                        st.markdown(
                            note["content"]
                        )

                        st.caption(
                            note["created_at"]
                        )

                    with col2:
                    
                        if st.button(
                            "🗑️",
                            key=f"delnote_{note['id']}"
                        ):

                            conn = get_conn()

                            conn.execute(
                                """
                                DELETE FROM notes
                                WHERE id=?
                                """,
                                (note["id"],)
                            )

                            conn.commit()
                            conn.close()

                            st.success(
                                "Note deleted"
                            )

                            st.rerun()

                    st.divider()

                col1, col2 = st.columns(2)

                with col1:

                    new_note = st.text_area(
                        "Markdown",
                        height=200,
                        key=f"note_{task['id']}"
                    )

                with col2:

                    st.markdown(
                        "### Preview"
                    )

                    st.markdown(
                        new_note
                    )

                if st.button(
                    "Add Note",
                    key=f"btn_{task['id']}"
                ):

                    conn = get_conn()

                    conn.execute(
                        """
                        INSERT INTO notes
                        (
                            task_id,
                            content
                        )
                        VALUES (?,?)
                        """,
                        (
                            task["id"],
                            new_note
                        )
                    )

                    conn.commit()
                    conn.close()

                    st.rerun()
