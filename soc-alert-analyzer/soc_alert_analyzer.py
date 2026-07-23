alert_file = "alerts.txt"

with open(alert_file, "r") as file:
    lines = file.readlines()

alert_counts = {}

severity_levels = {
    "INFO": "Low",
    "WARNING": "Medium",
    "FAILED LOGIN": "Medium",
    "PORT SCAN": "High",
    "MALWARE DETECTED": "Critical"
}
    
for line in lines:
    print(line.strip())

    if "INFO" in line:
        alert_type = "INFO" 

    elif "WARNING" in line:
        alert_type = "WARNING"

    elif "FAILED LOGIN" in line:
        alert_type = "FAILED LOGIN"

    elif "PORT SCAN" in line:
        alert_type = "PORT SCAN"

    elif "MALWARE DETECTED" in line:
        alert_type = "MALWARE DETECTED"

    else:
        continue

    if alert_type not in alert_counts:
        alert_counts[alert_type] = 1
    else:
        alert_counts[alert_type] += 1

print("\n========== SOC ALERT REPORT ==========")

for alert_type, count in alert_counts.items():
    severity = severity_levels[alert_type]
    print(f"{alert_type}: {count} | Severity: {severity}")

print("\nCritical Alerts:")

for line in lines:
    if "MALWARE DETECTED" in line:
        print("⚠", line.strip())

    elif "PORT SCAN" in line:
        print("⚠", line.strip())

print("======================================")

with open("soc_report.txt", "w", encoding="utf-8") as report:

    report.write("========== SOC ALERT REPORT ==========\n\n")

    alert_order = [
    "INFO",
    "WARNING",
    "FAILED LOGIN",
    "PORT SCAN",
    "MALWARE DETECTED"
]

    for alert_type in alert_order:
        if alert_type in alert_counts:
            count = alert_counts[alert_type]
            severity = severity_levels[alert_type]
            report.write(f"{alert_type}: {count} | Severity: {severity}\n")

    report.write("\nCritical Alerts:\n")
     
    for line in lines:
        if "MALWARE DETECTED" in line or "PORT SCAN" in line:
            report.write(f"ALERT: {line.strip()}\n")

    report.write("\n======================================")

print("\nSOC report successfully saved as soc_report.txt")
