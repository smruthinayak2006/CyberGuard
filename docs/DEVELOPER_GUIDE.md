# Developer Guide

## Overview

This guide explains how to set up, run, and understand the CyberGuard project. CyberGuard is a modular Python application for Windows endpoint security assessment with both a Command Line Interface (CLI) and a Streamlit Dashboard.

---

# Requirements

- Windows Operating System
- Python 3.13 or later
- SQLite
- Streamlit

---

# Installation

## Clone the Repository

```bash
git clone https://github.com/smruthinayak2006/CyberGuard.git

cd CyberGuard
```

## Create a Virtual Environment

```bash
python -m venv venv
```

## Activate the Environment

```bash
venv\Scripts\activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Running CyberGuard

## Command-Line Assessment

```bash
python cli.py
```

Runs a complete endpoint assessment and displays the results in the terminal.

---

## Streamlit Dashboard

```bash
streamlit run app.py
```

The dashboard provides:

- Secure authentication
- Endpoint assessment
- Executive security summary
- Security analytics
- Findings explorer
- Assessment history
- Authentication logs
- PDF report download

---

# Project Structure

| Folder | Responsibility |
|---------|----------------|
| analyzers | Security analysis modules |
| collectors | Endpoint information collection |
| core | Assessment workflow |
| dashboard | Streamlit dashboard |
| database | SQLite database and authentication |
| docs | Project documentation |
| reports | PDF report generation |
| test_files | File integrity monitoring data |

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
Store Results
        │
        ├── Dashboard
        └── PDF Report
```

---

# Database

CyberGuard stores assessment data in:

```text
database/cyberguard.db
```

The database maintains:

- Assessment history
- Security findings
- File integrity records
- Authentication logs

---

# Generated Reports

Assessment reports are automatically generated in:

```text
reports/
```

Each report includes:

- Executive Summary
- Endpoint Information
- Risk Assessment
- Security Findings
- Recommendations

---

# Troubleshooting

### Dashboard does not start

Verify that Streamlit is installed.

```bash
pip install streamlit
```

---

### Database not created

Run the CLI assessment once.

```bash
python cli.py
```

---

### PDF report not generated

Complete an assessment before attempting to download the report.

---

## Summary

CyberGuard follows a modular architecture where data collection, security analysis, risk assessment, persistence, reporting, and visualization are separated into independent components. This organization keeps the project structured, maintainable, and easy to understand.