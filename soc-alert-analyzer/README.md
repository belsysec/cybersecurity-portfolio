# SOC Alert Analyzer

## Overview

The SOC Alert Analyzer is a Python-based cybersecurity tool that analyzes security event logs, categorizes alerts, assigns severity levels, identifies critical security events, and automatically generates a professional SOC incident report.

This project simulates a basic Security Operations Center (SOC) workflow by processing security logs and producing both a terminal summary and a downloadable report.

---

## Features

- Reads security alerts from a log file
- Categorizes alerts into:
  - INFO
  - WARNING
  - FAILED LOGIN
  - PORT SCAN
  - MALWARE DETECTED
- Counts the number of occurrences of each alert type
- Assigns a severity level to every alert category
- Identifies and extracts critical alerts
- Generates a formatted SOC report (`soc_report.txt`)
- Displays a security summary in the terminal

---

## Technologies Used

- Python 3
- Visual Studio Code
- File Handling
- Dictionaries
- Loops
- Conditional Statements
- String Searching
- UTF-8 File Encoding

---

## Skills Demonstrated

- Security log analysis
- SOC alert categorization
- Threat prioritization
- Automated report generation
- Python file input/output
- Dictionary data structures
- Cybersecurity scripting fundamentals

---

## Project Structure

```
soc-alert-analyzer/
│
├── soc_alert_analyzer.py
├── alerts.txt
├── soc_report.txt
└── README.md
```

---

## Example Output

```
========== SOC ALERT REPORT ==========

INFO: 4 | Severity: Low
WARNING: 2 | Severity: Medium
FAILED LOGIN: 2 | Severity: Medium
PORT SCAN: 2 | Severity: High
MALWARE DETECTED: 2 | Severity: Critical

Critical Alerts:

ALERT: 2026-07-18 08:03:40 PORT SCAN Detected from 192.168.1.20
ALERT: 2026-07-18 08:05:15 MALWARE DETECTED Trojan.Generic
ALERT: 2026-07-18 08:09:50 PORT SCAN Detected from 10.0.0.15
ALERT: 2026-07-18 08:11:45 MALWARE DETECTED Ransomware.Sample

======================================
```

---

## How to Run

1. Open the project folder in VS Code.
2. Ensure `alerts.txt` is in the same folder as `soc_alert_analyzer.py`.
3. Run:

```bash
python soc_alert_analyzer.py
```

4. Review the generated `soc_report.txt` report.

---

## Future Improvements

- Read log files supplied by the user at runtime
- Support JSON and CSV log formats
- Export reports as PDF or HTML
- Color-code alerts in the terminal
- Add timestamps to generated reports
- Integrate with SIEM platforms or threat intelligence feeds
- Build a graphical user interface (GUI)

---

## Author

Belsochukwu Amaonye

Cybersecurity Portfolio Project