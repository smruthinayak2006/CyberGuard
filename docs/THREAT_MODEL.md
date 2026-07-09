# Threat Model

## Overview

CyberGuard is designed to perform basic endpoint security assessments on Windows systems. It identifies common security indicators, collects system information, and generates a summarized security report.

This document outlines the scope of the project, the threats it attempts to identify, and its current limitations.

---

# Assets

CyberGuard assesses the following endpoint assets:

- Operating System information
- Hostname
- IP Address
- CPU usage
- RAM usage
- Disk usage
- Running processes
- Windows Firewall status
- Local user accounts
- Installed Windows updates
- Monitored files

---

# Security Checks

The current implementation performs the following security checks.

## Endpoint Information

Collects basic information about the endpoint including:

- Hostname
- Username
- Operating System
- IP Address
- Boot Time
- CPU usage
- Memory usage
- Disk usage

---

## Windows Security Audit

Verifies:

- Firewall status
- Local user accounts
- Installed Windows updates

---

## Process Analysis

Collects information about running processes including:

- Process ID
- Process name
- CPU usage
- Memory usage
- Executable path

The analyzer generates findings based on predefined detection rules.

---

## File Integrity Monitoring

CyberGuard calculates SHA-256 hashes for monitored files.

Each scan compares the current hash with the stored baseline to determine whether a file has changed.

Possible states include:

- Unchanged
- Modified
- New file

---

# Risk Assessment

CyberGuard combines the results from all assessment modules to calculate an overall security score.

The assessment includes:

- Raw Score
- Normalized Score
- Highest Severity
- Overall Risk
- Total Findings

---

# Current Threat Coverage

CyberGuard currently assists in identifying:

- Unknown or suspicious processes
- Unexpected file modifications
- Disabled Windows Firewall
- Basic endpoint security misconfigurations

---

# Out of Scope

The current version of CyberGuard does **not** provide:

- Malware detection
- Antivirus capabilities
- Real-time monitoring
- Network intrusion detection
- Memory forensics
- Vulnerability scanning
- Log analysis
- Threat intelligence integration
- Cloud-based management
- Automatic incident response

---

# Assumptions

The project assumes that:

- It is executed on a Windows endpoint.
- The user has permission to collect system information.
- SQLite is available for local data storage.
- Required Python dependencies are installed.

---

# Limitations

Current limitations include:

- Windows-only implementation
- Local SQLite database
- Static detection rules
- Limited process analysis
- Manual scan execution
- No centralized management

---

# Future Improvements

Potential enhancements include:

- Linux support
- Real-time monitoring
- Advanced detection rules
- Scheduled assessments
- Email notifications
- Network security checks
- JSON and CSV report export
- Dashboard analytics
- Multi-endpoint management

---

# Summary

CyberGuard provides a lightweight endpoint security assessment solution for educational and internship purposes. It combines endpoint information collection, Windows security auditing, process analysis, file integrity monitoring, risk assessment, and reporting into a modular Python application.