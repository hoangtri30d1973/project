import sqlite3

DB_NAME = "project.db"


def get_conn():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():

    conn = get_conn()

    conn.execute("""
    CREATE TABLE IF NOT EXISTS projects(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.execute("""
    CREATE TABLE IF NOT EXISTS tasks(
        id INTEGER PRIMARY KEY AUTOINCREMENT,

        project_id INTEGER NOT NULL,

        title TEXT NOT NULL,
        description TEXT,

        priority TEXT DEFAULT 'MEDIUM',

        status TEXT DEFAULT 'TODO',

        due_date DATE,

        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

        FOREIGN KEY(project_id)
        REFERENCES projects(id)
    )
    """)

    conn.execute("""
    CREATE TABLE IF NOT EXISTS notes(
        id INTEGER PRIMARY KEY AUTOINCREMENT,

        task_id INTEGER NOT NULL,

        content TEXT NOT NULL,

        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

        FOREIGN KEY(task_id)
        REFERENCES tasks(id)
    )
    """)

    conn.commit()
    conn.close()