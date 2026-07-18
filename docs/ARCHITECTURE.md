# CyberGuard Architecture

## Overview

CyberGuard is a modular endpoint security assessment platform for Windows systems. It performs endpoint analysis by collecting system information, auditing security configurations, analyzing processes and startup programs, monitoring file integrity, calculating a security risk score, storing assessment history, and generating PDF reports.

The application can be executed through either the Command Line Interface (CLI) or the Streamlit Dashboard.

---

# High-Level Architecture

```text
                          +----------------------+
                          |        User          |
                          +----------+-----------+
                                     |
                          CLI / Streamlit Dashboard
                                     |
                                     ▼
                          +----------------------+
                          |     Scan Runner      |
                          +----------+-----------+
                                     |
      ---------------------------------------------------------------
      |                |                 |                |
      ▼                ▼                 ▼                ▼
+-------------+ +--------------+ +---------------+ +----------------+
| Collectors  | | Analyzers    | | Risk Engine   | | File Integrity |
+-------------+ +--------------+ +---------------+ +----------------+
      |                |                 |                |
      +----------------+-----------------+----------------+
                                     |
                                     ▼
                          +----------------------+
                          |    SQLite Database   |
                          +----------+-----------+
                                     |
                    +----------------+----------------+
                    |                                 |
                    ▼                                 ▼
         Streamlit Dashboard              PDF Report Generator
```

---

# Assessment Workflow

```text
Start Assessment
        │
        ▼
Collect Endpoint Information
        │
        ▼
Audit Windows Security
        │
        ▼
Analyze Processes
        │
        ▼
Analyze Startup Programs
        │
        ▼
Verify File Integrity
        │
        ▼
Calculate Risk Score
        │
        ▼
Store Assessment Results
        │
     ┌──┴───────────────┐
     ▼                  ▼
Dashboard          PDF Report
```

---

# Module Responsibilities

| Module | Responsibility |
|--------|----------------|
| **Scan Runner** | Coordinates the complete assessment workflow. |
| **Collectors** | Collect endpoint information, Windows security configuration, and startup programs. |
| **Analyzers** | Detect suspicious processes, startup entries, and file integrity changes. |
| **Risk Engine** | Aggregates findings and calculates the overall security posture. |
| **Database** | Stores scan history, findings, authentication logs, and file integrity records. |
| **Dashboard** | Displays security metrics, analytics, scan history, findings, and recommendations. |
| **Report Generator** | Produces a professional PDF assessment report after every scan. |

---

# Project Architecture

```text
User
 │
 ▼
Dashboard / CLI
 │
 ▼
Scan Runner
 │
 ├── System Collector
 ├── Windows Audit
 ├── Startup Collector
 ├── Process Analyzer
 ├── Startup Analyzer
 ├── File Integrity Analyzer
 │
 ▼
Risk Engine
 │
 ▼
SQLite Database
 ├── Scan History
 ├── Findings
 ├── Authentication Logs
 └── File Integrity Records
 │
 ├── Dashboard
 └── PDF Report
```

---

# Architecture Principles

- Modular design
- Separation of concerns
- Rule-based risk assessment
- Local-first data storage
- Reusable analysis components
- Clear workflow orchestration

---

## Summary

CyberGuard follows a layered modular architecture where each component has a dedicated responsibility. The Scan Runner orchestrates the assessment pipeline, analyzers evaluate endpoint security, the Risk Engine computes the final risk score, SQLite persists assessment data, and the dashboard and PDF generator present the results in an accessible format.