# Suspicious Login Detector

## Description

This Python program analyzes login logs and detects suspicious login activity by identifying failed login attempts. It also summarizes failed logins for each user and flags accounts that may be experiencing a brute-force attack.

## Features

- Reads login logs from a text file
- Detects failed login attempts
- Counts total failed logins
- Counts failed logins per user
- Flags users with 3 or more failed login attempts
- Displays a clean security summary

## Technologies Used

- Python 3
- VS Code

## How to Run

1. Open the project folder.
2. Run:

```bash
python login_detector.py
```

## Example Output

```
Total Failed Logins: 6

Failed Login Summary:

Bob: 5 failed attempts
⚠ Possible brute-force attack detected!

Alice: 1 failed attempt
```

## Skills Demonstrated

- File handling
- Dictionaries
- Loops
- Conditional statements
- String processing
- Basic SOC log analysis
- Brute-force detection