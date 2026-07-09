# Database Design

## Overview

CyberGuard uses SQLite as its local database to store scan history, security findings, and file integrity monitoring results.

SQLite was selected because it is lightweight, requires no separate database server, and is suitable for standalone endpoint security applications.

Database file:

```
database/cyberguard.db
```

---

# Database Tables

CyberGuard currently uses three primary tables:

- scan_history
- findings
- file_integrity

---

# 1. scan_history

Stores a summary of every endpoint assessment.

Purpose:

- Maintain assessment history
- Display dashboard metrics
- Track overall risk over multiple scans

### Fields

| Column | Description |
|---------|-------------|
| id | Primary Key |
| hostname | Endpoint hostname |
| ip_address | IP address |
| operating_system | Operating system |
| cpu_usage | CPU usage (%) |
| ram_usage | RAM usage (%) |
| disk_usage | Disk usage (%) |
| raw_score | Calculated raw risk score |
| normalized_score | Risk score out of 100 |
| highest_severity | Highest detected severity |
| overall_risk | Overall risk level |
| total_findings | Number of findings |
| scan_time | Scan timestamp |

---

# 2. findings

Stores every security finding detected during an assessment.

Purpose:

- Display findings in the dashboard
- Generate PDF reports
- Maintain historical findings

### Fields

| Column | Description |
|---------|-------------|
| id | Primary Key |
| finding_id | Finding identifier |
| title | Finding title |
| severity | Severity level |
| category | Finding category |
| raw_score | Risk score contribution |
| module | Detection module |
| recommendation | Suggested action |
| timestamp | Detection time |

---

# 3. file_integrity

Stores information about monitored files.

Purpose:

- Maintain baseline hashes
- Detect file modifications
- Support file integrity monitoring

### Fields

| Column | Description |
|---------|-------------|
| id | Primary Key |
| file_path | File location |
| sha256 | SHA-256 hash |
| status | Current file status |
| scan_time | Scan timestamp |

---

# Database Relationships

```
                scan_history
                      │
                      │
      -------------------------------
      │                             │
      ▼                             ▼
 findings                  file_integrity
```

Each assessment stores:

- One scan history record
- Multiple findings
- Multiple monitored files

---

# Data Flow

```
Endpoint Scan
      │
      ▼
Collect Results
      │
      ▼
Risk Calculation
      │
      ▼
Save Scan History
      │
      ▼
Save Findings
      │
      ▼
Save File Integrity Results
      │
      ▼
Dashboard & PDF Report
```

---

# Why SQLite?

SQLite provides several advantages for CyberGuard:

- Lightweight
- No server installation
- Easy deployment
- Portable database file
- Fast local access
- Suitable for internship-scale projects

---

# Future Improvements

Potential future enhancements include:

- PostgreSQL support
- Remote database synchronization
- Multi-endpoint storage
- Historical trend analysis
- Finding search and filtering
- Scan retention policies

---

# Summary

CyberGuard stores assessment data locally using SQLite. The database maintains scan history, security findings, and file integrity information, allowing the dashboard and PDF report generator to present both current and historical assessment results.