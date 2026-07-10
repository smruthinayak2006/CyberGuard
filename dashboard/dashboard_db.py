import sqlite3

DATABASE = "database/cyberguard.db"


def get_connection():
    return sqlite3.connect(DATABASE)


# ----------------------------------------------------------
# Latest Scan
# ----------------------------------------------------------

def get_latest_scan():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""

        SELECT

            hostname,
            ip_address,
            operating_system,
            cpu_usage,
            ram_usage,
            disk_usage,
            raw_score,
            normalized_score,
            highest_severity,
            risk_level,
            finding_count,
            scan_time

        FROM scan_history

        ORDER BY id DESC

        LIMIT 1

    """)

    row = cursor.fetchone()

    conn.close()

    if row is None:

        return {

            "hostname": "Unknown",
            "ip_address": "-",
            "operating_system": "-",
            "cpu_usage": 0,
            "ram_usage": 0,
            "disk_usage": 0,
            "raw_score": 0,
            "normalized_score": 0,
            "highest_severity": "LOW",
            "risk_level": "LOW",
            "finding_count": 0,
            "scan_time": "-"

        }

    return {

        "hostname": row[0],
        "ip_address": row[1],
        "operating_system": row[2],
        "cpu_usage": row[3],
        "ram_usage": row[4],
        "disk_usage": row[5],
        "raw_score": row[6],
        "normalized_score": row[7],
        "highest_severity": row[8],
        "risk_level": row[9],
        "finding_count": row[10],
        "scan_time": row[11]

    }


# ----------------------------------------------------------
# Latest Findings
# ----------------------------------------------------------

def get_latest_findings():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""

        SELECT

            finding_id,
            title,
            severity,
            module,
            status,
            timestamp

        FROM findings

        ORDER BY id DESC

        LIMIT 10

    """)

    findings = cursor.fetchall()

    conn.close()

    return findings


# ----------------------------------------------------------
# Scan History
# ----------------------------------------------------------

def get_scan_history(limit=20):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(

        """

        SELECT

            scan_time,
            risk_level,
            normalized_score,
            finding_count

        FROM scan_history

        ORDER BY id DESC

        LIMIT ?

        """,

        (limit,)

    )

    history = cursor.fetchall()

    conn.close()

    return history


# ----------------------------------------------------------
# Total Findings
# ----------------------------------------------------------

def get_finding_count():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(

        "SELECT COUNT(*) FROM findings"

    )

    count = cursor.fetchone()[0]

    conn.close()

    return count