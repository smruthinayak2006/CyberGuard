# CyberGuard Architecture

## Overview

CyberGuard is an endpoint security assessment system developed using Python. It gathers endpoint information, performs basic security checks, analyzes running processes, monitors selected files for integrity, calculates an overall security risk score, stores scan results in a SQLite database, and generates a PDF security report.

The application provides both a Command Line Interface (CLI) and a Streamlit dashboard for running assessments and viewing results.

---

# System Architecture

```
                       +----------------------+
                       |        User          |
                       +----------+-----------+
                                  |
                     Start Assessment / CLI
                                  |
                                  v
                     +----------------------+
                     |     Scan Runner      |
                     +----------+-----------+
                                |
       -----------------------------------------------------
       |                |                 |                |
       v                v                 v                v
+--------------+ +---------------+ +---------------+ +----------------+
| System        | | Windows       | | Process       | | File Integrity |
| Collector     | | Security      | | Analyzer      | | Monitor        |
|               | | Audit         | |               | |                |
+--------------+ +---------------+ +---------------+ +----------------+
       \                |                 |                /
        \               |                 |               /
         \              |                 |              /
          -----------------------------------------------
                              |
                              v
                    +----------------------+
                    |     Risk Engine      |
                    +----------+-----------+
                               |
             ----------------------------------------
             |                                      |
             v                                      v
     +-------------------+                 +------------------+
     | SQLite Database   |                 | PDF Report       |
     | Scan History      |                 | Generator        |
     | Findings          |                 +------------------+
     +-------------------+
                               |
                               v
                    +----------------------+
                    | Streamlit Dashboard  |
                    +----------------------+
```

---

# Components

## 1. Scan Runner

The Scan Runner is the central controller of CyberGuard. It coordinates every stage of the assessment by calling each module in sequence.

Responsibilities:

- Collect endpoint information
- Perform Windows security audit
- Analyze running processes
- Monitor file integrity
- Calculate security risk
- Store results
- Generate reports

---

## 2. System Collector

Collects basic endpoint information including:

- Hostname
- Username
- IP Address
- Operating System
- CPU Usage
- RAM Usage
- Disk Usage
- Boot Time

This information forms the basis of every assessment.

---

## 3. Windows Security Audit

Performs basic Windows security checks such as:

- Firewall status
- Local user accounts
- Installed Windows updates

These checks provide an overview of the endpoint's security configuration.

---

## 4. Process Analyzer

Inspects currently running processes.

Information collected includes:

- Process ID
- Process name
- CPU usage
- Memory usage
- Executable path

The analyzer also identifies processes that match simple detection rules and generates security findings.

---

## 5. File Integrity Monitor

Monitors selected files by calculating SHA-256 hashes.

Each scan compares the current hash with the previously stored baseline to determine whether a file has changed.

Possible results include:

- Unchanged
- Modified
- New file

---

## 6. Risk Engine

The Risk Engine combines findings from all modules and calculates an overall security score.

It determines:

- Risk Score
- Highest Severity
- Overall Risk Level
- Total Findings

The resulting assessment is displayed in both the CLI and dashboard.

---

## 7. SQLite Database

CyberGuard stores assessment results in a local SQLite database.

The database maintains:

- Scan history
- Security findings
- File integrity results

This allows previous assessments to be viewed from the dashboard.

---

## 8. PDF Report Generator

After each assessment, CyberGuard generates a PDF report containing:

- Endpoint information
- Risk assessment
- Security findings
- Recommendations

Reports can be downloaded directly from the dashboard.

---

## 9. Streamlit Dashboard

The dashboard provides a graphical interface for interacting with CyberGuard.

Features include:

- Start Assessment
- Risk metrics
- Endpoint overview
- Resource usage
- Recent findings
- Report download

---

# Scan Workflow

The complete assessment follows this sequence:

1. User starts an assessment.
2. Endpoint information is collected.
3. Windows security checks are performed.
4. Running processes are analyzed.
5. File integrity is verified.
6. Risk score is calculated.
7. Results are stored in SQLite.
8. PDF report is generated.
9. Dashboard is updated with the latest assessment.

---

# Design Goals

CyberGuard was designed with the following objectives:

- Modular architecture
- Easy maintenance
- Simple deployment
- Local data storage
- Clear reporting
- Beginner-friendly implementation

---

# Summary

CyberGuard follows a modular architecture in which independent components perform specific security assessment tasks. The Scan Runner coordinates each module, while the Risk Engine consolidates their outputs into a unified assessment. Results are stored locally, presented through the dashboard, and exported as PDF reports.