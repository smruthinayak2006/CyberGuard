# Developer Guide

## Overview

This document provides instructions for setting up, running, and extending the CyberGuard project.

CyberGuard is built using Python and follows a modular architecture, allowing individual components to be maintained and extended independently.

---

# Project Requirements

- Python 3.x
- Windows Operating System
- SQLite
- Streamlit

---

# Project Setup

## Clone the Repository

```bash
git clone https://github.com/smruthinayak2006/CyberGuard.git

cd CyberGuard
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

---

## Activate Virtual Environment

Windows

```bash
venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Running the Project

## Command Line Interface

```bash
python cli.py
```

The CLI performs a complete endpoint assessment and displays the results in the terminal.

---

## Dashboard

```bash
streamlit run app.py
```

The Streamlit dashboard allows users to:

- Start a security assessment
- View endpoint information
- Monitor findings
- Download PDF reports

---

# Project Modules

| Folder | Purpose |
|---------|----------|
| analyzers | Security analysis modules |
| collectors | Endpoint data collection |
| dashboard | Streamlit user interface |
| database | SQLite database management |
| reports | PDF report generation |
| core | Main scan workflow |
| models | Data models |
| scanners | Scanner components |
| docs | Project documentation |

---

# Scan Flow

```
Start Assessment

↓

Collect Endpoint Information

↓

Windows Security Audit

↓

Process Analysis

↓

File Integrity Monitoring

↓

Risk Calculation

↓

Save Results

↓

Generate PDF Report

↓

Dashboard Update
```

---

# Database

CyberGuard stores scan results locally in:

```
database/cyberguard.db
```

The database stores:

- Scan history
- Security findings
- File integrity results

---

# Generated Reports

Reports are saved automatically inside:

```
reports/
```

Each report contains:

- Endpoint Information
- Risk Assessment
- Security Findings
- Recommendations

---

# Extending CyberGuard

Developers can enhance the project by adding:

- Additional Windows security checks
- Linux support
- New detection modules
- Dashboard enhancements
- Additional report formats

---

# Troubleshooting

## Dashboard does not start

Verify that Streamlit is installed.

```
pip install streamlit
```

---

## Database not created

Run a scan once using:

```
python cli.py
```

---

## Missing PDF report

Complete an assessment before downloading a report.

---

# Summary

CyberGuard follows a modular design, making it easy to understand, maintain, and extend. New modules can be added without affecting the overall project workflow.