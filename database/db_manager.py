import sqlite3
from datetime import datetime

DATABASE = "database/cyberguard.db"


def get_connection():
    return sqlite3.connect(DATABASE)


def initialize_database():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS file_integrity (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            file_path TEXT NOT NULL,

            sha256 TEXT NOT NULL,

            status TEXT NOT NULL,

            scan_time TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


def save_file_results(file_results):

    conn = get_connection()
    cursor = conn.cursor()

    scan_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    for file in file_results:

        cursor.execute("""

            INSERT INTO file_integrity
            (
                file_path,
                sha256,
                status,
                scan_time
            )

            VALUES (?, ?, ?, ?)

        """, (

            file["file"],
            file["sha256"],
            file["status"],
            scan_time

        ))

    conn.commit()
    conn.close()


def get_file_history():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""

        SELECT
            file_path,
            sha256,
            status,
            scan_time

        FROM file_integrity

        ORDER BY id DESC

    """)

    data = cursor.fetchall()

    conn.close()

    return data