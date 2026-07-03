import sqlite3


DATABASE = "database/cyberguard.db"


def get_connection():
    return sqlite3.connect(DATABASE)


def get_latest_findings():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""

        SELECT
            finding_id,
            title,
            severity,
            module,
            timestamp

        FROM findings

        ORDER BY id DESC

        LIMIT 10

    """)

    findings = cursor.fetchall()

    conn.close()

    return findings


def get_finding_count():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(

        "SELECT COUNT(*) FROM findings"

    )

    count = cursor.fetchone()[0]

    conn.close()

    return count