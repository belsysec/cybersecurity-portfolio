def load_events(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return [line.strip() for line in file if line.strip()]


def count_events(events):
    categories = {
        "INFO": 0,
        "WARNING": 0,
        "FAILED LOGIN": 0,
        "PORT SCAN": 0,
        "MALWARE DETECTED": 0
    }

    for event in events:
        if "MALWARE DETECTED" in event:
            categories["MALWARE DETECTED"] += 1
        elif "FAILED LOGIN" in event:
            categories["FAILED LOGIN"] += 1
        elif "PORT SCAN" in event:
            categories["PORT SCAN"] += 1
        elif "WARNING" in event:
            categories["WARNING"] += 1
        elif "INFO" in event:
            categories["INFO"] += 1

    return categories


def get_critical_events(events):
    critical_events = []

    for event in events:
        if "MALWARE DETECTED" in event or "PORT SCAN" in event:
            critical_events.append(event)

    return critical_events


def display_dashboard(counts, critical_events):
    print("========== MINI SIEM DASHBOARD ==========\n")

    print(f"Total Events: {sum(counts.values())}\n")

    for event_type, count in counts.items():
        print(f"{event_type:<18} {count}")

    print("\nCritical Events:")

    if critical_events:
        for event in critical_events:
            print(f"ALERT: {event}")
    else:
        print("No critical events detected.")

    print("\n=========================================")


def save_dashboard(counts, critical_events):
    with open("siem_dashboard_report.txt", "w", encoding="utf-8") as report:
        report.write("========== MINI SIEM DASHBOARD ==========\n\n")
        report.write(f"Total Events: {sum(counts.values())}\n\n")

        for event_type, count in counts.items():
            report.write(f"{event_type:<18} {count}\n")

        report.write("\nCritical Events:\n")

        if critical_events:
            for event in critical_events:
                report.write(f"ALERT: {event}\n")
        else:
            report.write("No critical events detected.\n")

        report.write("\n=========================================")


events = load_events("security_events.txt")
counts = count_events(events)
critical_events = get_critical_events(events)

display_dashboard(counts, critical_events)
save_dashboard(counts, critical_events)

print("\nDashboard report saved as siem_dashboard_report.txt")