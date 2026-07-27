# Threat Intelligence Feed Analyzer

## Overview

The Threat Intelligence Feed Analyzer is a Python cybersecurity tool that processes a threat intelligence feed, removes duplicate Indicators of Compromise, categorizes entries, summarizes severity levels, and highlights high-priority threats.

## Features

- Loads structured threat intelligence data
- Parses IP addresses, domains, and file hashes
- Removes duplicate IOC entries
- Counts indicators by type
- Counts indicators by severity
- Highlights Critical and High threats
- Generates an automated threat intelligence report

## Project Structure

```text
threat-intelligence-feed-analyzer/
├── feed_analyzer.py
├── threat_feed.txt
├── threat_feed_report.txt
└── README.md
```

## How to Run

```bash
python feed_analyzer.py
```

## Skills Demonstrated

- Threat intelligence analysis
- IOC deduplication
- Python sets
- Lists of dictionaries
- File parsing
- Data aggregation
- Risk prioritization
- Automated reporting

## Author

Belsochukwu Amaonye