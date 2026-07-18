# Database Design

## Overview

CyberGuard uses SQLite as a lightweight local database to store assessment results, security findings, authentication activity, and file integrity records. The database supports historical analysis, dashboard visualization, and PDF report generation without requiring a separate database server.

**Database File**

```text
database/cyberguard.db
```

---

# Database Schema

CyberGuard consists of four primary tables.

```text
                scan_history
                     │
          One Scan ──┼──────────────┐
                     │              │
                     ▼              ▼
               findings      file_integrity

                     ▲
                     │
                auth_logs
```

---

# Tables

## 1. scan_history

Stores a summary of every completed endpoint assessment.

| Column | Description |
|---------|-------------|
| id | Primary key |
| hostname | Endpoint hostname |
| ip_address | Endpoint IP address |
| operating_system | Operating system |
| cpu_usage | CPU usage (%) |
| ram_usage | RAM usage (%) |
| disk_usage | Disk usage (%) |
| raw_score | Calculated risk score |
| normalized_score | Risk score (0–100) |
| highest_severity | Highest detected severity |
| risk_level | Overall security posture |
| finding_count | Total findings |
| scan_time | Assessment timestamp |

---

## 2. findings

Stores every security finding generated during an assessment.

| Column | Description |
|---------|-------------|
| id | Primary key |
| scan_id | Associated assessment |
| finding_id | Finding identifier |
| title | Finding title |
| severity | Severity level |
| category | Finding category |
| module | Detection module |
| description | Finding details |
| recommendation | Suggested remediation |
| raw_score | Risk contribution |
| status | Finding status |
| timestamp | Detection timestamp |

---

## 3. file_integrity

Stores file integrity monitoring results.

| Column | Description |
|---------|-------------|
| id | Primary key |
| file_path | Monitored file |
| sha256 | SHA-256 hash |
| status | File status |
| scan_time | Scan timestamp |

---

## 4. auth_logs

Stores dashboard authentication events.

| Column | Description |
|---------|-------------|
| id | Primary key |
| username | User account |
| status | Login result |
| login_time | Authentication timestamp |

---

# Data Flow

```text
Start Assessment
        │
        ▼
Collect Endpoint Data
        │
        ▼
Analyze Security
        │
        ▼
Calculate Risk Score
        │
        ▼
Store Assessment Results
        │
        ├── scan_history
        ├── findings
        ├── file_integrity
        └── auth_logs
        │
        ▼
Dashboard & PDF Report
```

---

# Why SQLite?

SQLite was selected because it is:

- Lightweight
- Serverless
- Easy to deploy
- Portable
- Fast for local storage
- Well suited for a standalone endpoint security application

---

## Summary

CyberGuard uses SQLite to maintain assessment history, security findings, authentication activity, and file integrity records. This enables the dashboard and PDF reports to present both the latest assessment and historical security data while keeping the application simple, portable, and self-contained.