def load_incidents(filename):
    incidents = []

    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if not line:
                continue

            incident_id, severity, description, status = line.split("|")

            incidents.append({
                "id": incident_id,
                "severity": severity,
                "description": description,
                "status": status
            })

    return incidents


def count_incidents(incidents):
    summary = {
        "Critical": 0,
        "High": 0,
        "Medium": 0,
        "Low": 0
    }

    for incident in incidents:
        summary[incident["severity"]] += 1

    return summary


def get_open_incidents(incidents):
    open_cases = []

    for incident in incidents:
        if incident["status"] == "Open":
            open_cases.append(incident)

    return open_cases


def save_report(incidents, summary, open_cases):

    with open(
        "incident_report.txt",
        "w",
        encoding="utf-8"
    ) as report:

        report.write("========== INCIDENT RESPONSE REPORT ==========\n\n")

        report.write(f"Total Incidents: {len(incidents)}\n\n")

        report.write("Severity Summary\n")

        for severity, count in summary.items():
            report.write(f"{severity}: {count}\n")

        report.write("\nOpen Incidents\n\n")

        for incident in open_cases:
            report.write(
                f"{incident['id']} | "
                f"{incident['severity']} | "
                f"{incident['description']}\n"
            )

        report.write("\nRecommended Actions\n\n")

        report.write(
            "- Isolate affected systems.\n"
        )

        report.write(
            "- Notify Incident Response Team.\n"
        )

        report.write(
            "- Preserve forensic evidence.\n"
        )

        report.write(
            "- Begin containment procedures.\n"
        )

        report.write(
            "- Continue monitoring.\n"
        )

        report.write(
            "\n=============================================="
        )


incidents = load_incidents("incidents.txt")

summary = count_incidents(incidents)

open_cases = get_open_incidents(incidents)

print("========== INCIDENT RESPONSE DASHBOARD ==========\n")

print(f"Total Incidents: {len(incidents)}\n")

for severity, count in summary.items():
    print(f"{severity:<10}: {count}")

print("\nOpen Incidents\n")

for incident in open_cases:
    print(
        f"{incident['id']} | "
        f"{incident['severity']} | "
        f"{incident['description']}"
    )

save_report(
    incidents,
    summary,
    open_cases
)

print("\nReport saved as incident_report.txt")