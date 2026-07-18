# Threat Model

## Overview

CyberGuard is a Windows endpoint security assessment platform that evaluates the security posture of a system through local data collection, security analysis, file integrity monitoring, and rule-based risk assessment. This document defines the assets assessed, the threats considered, and the current assessment scope.

---

# Protected Assets

CyberGuard evaluates the following endpoint assets:

- Operating system information
- Hostname and IP address
- CPU, RAM, and disk utilization
- Running processes
- Startup programs
- Windows Firewall configuration
- Local user accounts
- Installed Windows updates
- Monitored files

---

# Threat Coverage

CyberGuard is designed to identify indicators of the following security risks:

| Threat | Detection Method |
|---------|------------------|
| Unknown or suspicious processes | Process analysis |
| Processes executing from untrusted locations | Process analysis |
| Unexpected startup entries | Startup analysis |
| Modified monitored files | SHA-256 file integrity monitoring |
| Disabled Windows Firewall | Windows security audit |
| Basic endpoint misconfigurations | Windows security audit |

---

# Assessment Workflow

```text
Endpoint Assessment
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
Generate Dashboard & PDF Report
```

---

# Risk Assessment

CyberGuard consolidates findings from all assessment modules to determine the endpoint's security posture.

The assessment includes:

- Raw Risk Score
- Normalized Security Score
- Highest Severity
- Overall Risk Level
- Total Findings

---

# Out of Scope

CyberGuard is **not** intended to perform:

- Malware detection
- Antivirus protection
- Real-time monitoring
- Network intrusion detection
- Vulnerability scanning
- Memory forensics
- Threat intelligence integration
- Automatic incident response
- Cloud-based endpoint management

---

# Assumptions

CyberGuard assumes:

- The assessment is executed on a Windows endpoint.
- The user has permission to collect endpoint information.
- SQLite is available for local storage.
- Required Python dependencies are installed.

---

# Limitations

Current limitations include:

- Windows-only implementation
- Local SQLite database
- Rule-based detection logic
- Manual assessment execution
- Single-endpoint assessment

---

## Summary

CyberGuard provides a lightweight endpoint security assessment solution by combining endpoint information collection, Windows security auditing, process and startup analysis, file integrity monitoring, and rule-based risk assessment into a modular Python application. The generated findings are intended to support security assessment and should be validated before operational or compliance decisions are made.