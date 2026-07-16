import sqlite3
import bcrypt

from datetime import datetime

DATABASE = "database/cyberguard.db"


def get_connection():
    return sqlite3.connect(DATABASE)


def initialize_users():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            username TEXT UNIQUE,

            password_hash TEXT

        )
    """)

    cursor.execute(
        "SELECT COUNT(*) FROM users"
    )

    count = cursor.fetchone()[0]

    if count == 0:

        password = bcrypt.hashpw(

            "CyberGuard@123".encode(),

            bcrypt.gensalt()

        ).decode()

        cursor.execute("""

            INSERT INTO users(

                username,

                password_hash

            )

            VALUES(?,?)

        """, (

            "admin",

            password

        ))

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS auth_logs(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            username TEXT,

            status TEXT,

            login_time TEXT

        )
    """)
    
    conn.commit()
    conn.close()


def verify_user(username, password):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(

        """

        SELECT password_hash

        FROM users

        WHERE username=?

        """,

        (username,)

    )

    row = cursor.fetchone()

    conn.close()

    if row is None:

        return False

    return bcrypt.checkpw(

        password.encode(),

        row[0].encode()

    )

def log_login(username, status):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""

        INSERT INTO auth_logs(

            username,

            status,

            login_time

        )

        VALUES(?,?,?)

    """, (

        username,

        status,

        datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    ))

    conn.commit()

    conn.close()