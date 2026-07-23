# 🛡️ File Integrity Monitor

## Overview

This Python project monitors the integrity of a file using SHA-256 hashing.

The program creates a baseline hash of a file during its first execution. On future executions, it compares the current hash against the saved baseline hash to determine whether the file has been modified.

This demonstrates one of the fundamental concepts used in cybersecurity for detecting unauthorized file changes.

---

## Features

- SHA-256 hashing
- Automatic baseline hash creation
- File integrity verification
- Detects file modifications
- Simple and beginner-friendly implementation

---

## Technologies Used

- Python 3
- hashlib
- os
- VS Code

---

## Example Output

### First Run

```
Baseline hash created.
```

### File Unchanged

```
File integrity verified.
```

### File Modified

```
WARNING! File has been modified!
```

---

## Skills Demonstrated

- Python programming
- File handling
- SHA-256 hashing
- Integrity verification
- Basic incident detection
- Cybersecurity fundamentals

---

## Cybersecurity Concept

File Integrity Monitoring (FIM) is commonly used by organizations to detect unauthorized changes to important files. Security tools such as Tripwire and Microsoft Defender use similar concepts to identify potential attacks or tampering.

---

## Author

Belsochukwu Amaonye