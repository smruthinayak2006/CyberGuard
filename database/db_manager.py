import sqlite3

DATABASE = "database/cyberguard.db"


def get_connection():
    return sqlite3.connect(DATABASE)


def initialize_database():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS file_integrity (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            file_path TEXT,

            sha256 TEXT,

            status TEXT,

            scan_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    connection.commit()
    connection.close()


import sqlite3

DATABASE = "database/cyberguard.db"


def get_connection():
    return sqlite3.connect(DATABASE)


def initialize_database():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS file_integrity (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            file_path TEXT,

            sha256 TEXT,

            status TEXT,

            scan_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    connection.commit()
    connection.close()

def save_file_results(results):

    connection = get_connection()
    cursor = connection.cursor()

    for file in results:

        cursor.execute("""

            INSERT INTO file_integrity

            (
                file_path,
                sha256,
                status
            )

            VALUES (?, ?, ?)

        """, (

            file["file"],
            file["sha256"],
            file["status"]

        ))

    connection.commit()
    connection.close()