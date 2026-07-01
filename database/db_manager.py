import sqlite3
from datetime import datetime

DATABASE = "database/cyberguard.db"


def get_connection():
    return sqlite3.connect(DATABASE)


def initialize_database():

    conn = get_connection()
    cursor = conn.cursor()

    # ----------------------------
    # File Integrity Table
    # ----------------------------

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS file_integrity(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            file_path TEXT,

            sha256 TEXT,

            status TEXT,

            scan_time TEXT

        )
    """)

    # ----------------------------
    # Findings Table
    # ----------------------------

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS findings(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            finding_id TEXT,

            title TEXT,

            category TEXT,

            severity TEXT,

            raw_score INTEGER,

            description TEXT,

            recommendation TEXT,

            module TEXT,

            status TEXT,

            timestamp TEXT

        )
    """)

    conn.commit()

    conn.close()


# -------------------------------------------------

def save_file_results(file_results):

    conn = get_connection()

    cursor = conn.cursor()

    scan_time = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    for file in file_results:

        cursor.execute("""

            INSERT INTO file_integrity(

                file_path,

                sha256,

                status,

                scan_time

            )

            VALUES(?,?,?,?)

        """, (

            file["file"],

            file["sha256"],

            file["status"],

            scan_time

        ))

    conn.commit()

    conn.close()


# -------------------------------------------------

def save_findings(findings):

    conn = get_connection()

    cursor = conn.cursor()

    for finding in findings:

        cursor.execute("""

            INSERT INTO findings(

                finding_id,

                title,

                category,

                severity,

                raw_score,

                description,

                recommendation,

                module,

                status,

                timestamp

            )

            VALUES(?,?,?,?,?,?,?,?,?,?)

        """, (

            finding.finding_id,

            finding.title,

            finding.category,

            finding.severity,

            finding.raw_score,

            finding.description,

            finding.recommendation,

            finding.module,

            finding.status,

            finding.timestamp

        ))

    conn.commit()

    conn.close()


# -------------------------------------------------

def get_file_history():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""

        SELECT *

        FROM file_integrity

    """)

    data = cursor.fetchall()

    conn.close()

    return data


# -------------------------------------------------

def get_findings():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""

        SELECT *

        FROM findings

        ORDER BY id DESC

    """)

    data = cursor.fetchall()

    conn.close()

    return data