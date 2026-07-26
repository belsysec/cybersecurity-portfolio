# Log Search and Threat Hunting Tool

## Overview

This Python tool allows a security analyst to search security logs for usernames, IP addresses, domains, and event types.

It simulates a basic threat-hunting workflow by filtering logs and generating a search report.

## Features

- Loads security logs from a text file
- Accepts a search term from the user
- Performs case-insensitive searches
- Searches usernames, IP addresses, domains, and event types
- Displays matching events in the terminal
- Generates a `search_results.txt` report
- Handles empty searches and zero-result searches

## Project Structure

```text
log-search-threat-hunting-tool/
├── log_search.py
├── security_logs.txt
├── search_results.txt
└── README.md
```

## How to Run

```bash
python log_search.py
```

Enter a search term such as:

```text
LOGIN FAILED
```

## Skills Demonstrated

- Threat hunting
- Security log filtering
- Python functions
- User input
- Lists
- Loops
- Conditional logic
- File input and output
- Case-insensitive string searching

## Author

Belsochukwu Amaonye