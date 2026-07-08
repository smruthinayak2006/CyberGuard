# 🛡 CyberGuard

A Python-based endpoint security assessment tool that collects system information, performs basic security checks, analyzes running processes, monitors file integrity, and presents the results through both a command-line interface and a Streamlit dashboard.

> **Project Type:** Internship Project  
> **Status:** In Development

---

## Features

- Collects endpoint information
- Performs Windows security audit
- Analyzes running processes
- Monitors file integrity using SHA-256 hashes
- Calculates an overall security risk score
- Stores findings in SQLite
- Maintains scan history
- Provides both CLI and Streamlit interfaces

---

## Technology Stack

| Component | Technology |
|----------|------------|
| Language | Python |
| Dashboard | Streamlit |
| Database | SQLite |
| Platform | Windows |
| Version Control | Git & GitHub |

---

## Project Structure

```text
CyberGuard/
│
├── analyzers/
├── collectors/
├── config/
├── core/
├── dashboard/
│   └── components/
├── database/
├── docs/
├── logs/
├── models/
├── reports/
├── scanners/
├── test_files/
│
├── app.py
├── cli.py
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Modules

### Endpoint Information

Collects:

- Hostname
- IP Address
- Operating System
- CPU Usage
- RAM Usage
- Disk Usage
- Boot Time

### Windows Security Audit

Collects:

- Firewall status
- Local users
- Installed Windows updates

### Process Analysis

Displays running processes and identifies unknown processes.

### File Integrity Monitoring

Calculates SHA-256 hashes for monitored files and detects modifications.

### Risk Assessment

Generates:

- Risk Score
- Risk Level
- Highest Severity
- Security Findings

---

## Database

CyberGuard uses SQLite.

Current tables:

- `file_integrity`
- `findings`
- `scan_history`

---

## Running the Project

### Clone the repository

```bash
git clone <repository-url>
cd CyberGuard
```

### Create a virtual environment

```bash
python -m venv venv
```

### Activate the environment

Windows

```bash
venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## Run the CLI

```bash
python cli.py
```

---

## Run the Dashboard

```bash
streamlit run app.py
```

---

## Screenshots

Screenshots are available in:

```text
docs/screenshots/
```

Current screenshots include:

- Endpoint Information
- Windows Security Audit
- Process Analysis
- Process Explorer
- File Integrity Monitoring
- File Change Detection
- Dashboard

---

## Current Progress

Implemented:

- Endpoint information collection
- Windows security audit
- Process analysis
- File integrity monitoring
- Risk assessment engine
- Findings management
- SQLite database
- Scan history
- Streamlit dashboard

Planned:

- PDF report generation
- Dashboard improvements
- Additional security checks
- Export functionality

---

## Author

**Smriti Prajwal**

B.Tech Computer Science Engineering

---

## License

This project is developed for educational and internship purposes.