# Threat Intelligence IOC Scanner

## Overview

The Threat Intelligence IOC Scanner is a Python cybersecurity tool that compares network logs against a list of known Indicators of Compromise.

It identifies suspicious IP addresses, domains, and file hashes, then generates a structured threat-detection report.

## Features

- Loads Indicators of Compromise from a text file
- Scans network logs for IOC matches
- Performs case-insensitive matching
- Classifies IOCs as IP addresses, domains, or file hashes
- Displays findings in the terminal
- Generates an automated IOC scan report
- Handles empty lines in input files

## Project Structure

```text
threat-intelligence-ioc-scanner/
├── ioc_scanner.py
├── iocs.txt
├── network_logs.txt
├── ioc_scan_report.txt
└── README.md
```

## How to Run

```bash
python ioc_scanner.py
```

## Skills Demonstrated

- Threat intelligence analysis
- IOC detection
- Python functions
- Lists and dictionaries
- Nested loops
- File input and output
- String matching
- Automated report generation

## Example Finding

```text
IOC Detected: malicious-site.com
Type: Domain
Log Entry: 2026-07-23 08:17:30 DNS request sent to malicious-site.com
```

## Author

Belsochukwu Amaonye