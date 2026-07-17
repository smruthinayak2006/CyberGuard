import sqlite3
from datetime import datetime

DATABASE = "database/cyberguard.db"


def get_connection():
    return sqlite3.connect(DATABASE)


def initialize_database():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS file_integrity(

            id INTEGER PRIMARY KEY AUTOINCREMENT,
            file_path TEXT,
            sha256 TEXT,
            status TEXT,
            scan_time TEXT

        )
    """)

    cursor.execute("""

    CREATE TABLE IF NOT EXISTS findings(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        scan_id INTEGER,

        finding_id TEXT,

        title TEXT,

        severity TEXT,

        category TEXT,

        module TEXT,

        description TEXT,

        recommendation TEXT,

        raw_score INTEGER,

        status TEXT,

        timestamp TEXT,

        FOREIGN KEY(scan_id)
            REFERENCES scan_history(id)

    )

    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS scan_history(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            hostname TEXT,
            ip_address TEXT,
            operating_system TEXT,

            cpu_usage REAL,
            ram_usage REAL,
            disk_usage REAL,

            raw_score INTEGER,
            normalized_score INTEGER,

            highest_severity TEXT,
            risk_level TEXT,

            finding_count INTEGER,

            scan_time TEXT

        )
    """)

    conn.commit()
    conn.close()


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


def save_findings(scan_id, findings):

    conn = get_connection()
    cursor = conn.cursor()

    for finding in findings:

        cursor.execute("""

            INSERT INTO findings(
                       
                scan_id,
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

            VALUES(?,?,?,?,?,?,?,?,?,?,?)

        """, (

            scan_id,
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


def save_scan(system_info, risk):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""

        INSERT INTO scan_history(

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

        )

        VALUES(?,?,?,?,?,?,?,?,?,?,?,?)

    """, (

        system_info["hostname"],
        system_info["ip_address"],
        system_info["operating_system"],

        system_info["cpu_usage"],
        system_info["ram_usage"],
        system_info["disk_usage"],

        risk["raw_score"],
        risk["score"],

        risk["highest_severity"],
        risk["level"],

        risk["finding_count"],

        datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    ))

    scan_id = cursor.lastrowid

    conn.commit()
    conn.close()

    return scan_id


def get_latest_scan():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""

        SELECT *

        FROM scan_history

        ORDER BY id DESC

        LIMIT 1

    """)

    row = cursor.fetchone()

    conn.close()

    return row


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