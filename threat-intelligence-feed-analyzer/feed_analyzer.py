def load_feed(filename):
    threat_entries = []

    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            cleaned_line = line.strip()

            if not cleaned_line:
                continue

            parts = cleaned_line.split("|")

            if len(parts) == 4:
                threat_entries.append({
                    "indicator": parts[0],
                    "type": parts[1],
                    "severity": parts[2],
                    "description": parts[3]
                })

    return threat_entries


def remove_duplicates(entries):
    unique_entries = []
    seen_indicators = set()

    for entry in entries:
        indicator = entry["indicator"].lower()

        if indicator not in seen_indicators:
            unique_entries.append(entry)
            seen_indicators.add(indicator)

    return unique_entries


def count_by_field(entries, field_name):
    counts = {}

    for entry in entries:
        value = entry[field_name]

        if value not in counts:
            counts[value] = 1
        else:
            counts[value] += 1

    return counts


def get_high_priority_entries(entries):
    high_priority = []

    for entry in entries:
        if entry["severity"] in ["Critical", "High"]:
            high_priority.append(entry)

    return high_priority


def save_report(
    original_entries,
    unique_entries,
    type_counts,
    severity_counts,
    high_priority
):
    with open(
        "threat_feed_report.txt",
        "w",
        encoding="utf-8"
    ) as report:
        report.write(
            "========== THREAT INTELLIGENCE FEED REPORT ==========\n\n"
        )

        report.write(
            f"Original Entries: {len(original_entries)}\n"
        )
        report.write(
            f"Unique Entries: {len(unique_entries)}\n"
        )
        report.write(
            f"Duplicates Removed: "
            f"{len(original_entries) - len(unique_entries)}\n\n"
        )

        report.write("IOC Type Summary:\n")

        for ioc_type, count in type_counts.items():
            report.write(f"{ioc_type}: {count}\n")

        report.write("\nSeverity Summary:\n")

        for severity, count in severity_counts.items():
            report.write(f"{severity}: {count}\n")

        report.write("\nHigh-Priority Indicators:\n\n")

        if high_priority:
            for entry in high_priority:
                report.write(
                    f"{entry['severity']} | "
                    f"{entry['type']} | "
                    f"{entry['indicator']} | "
                    f"{entry['description']}\n"
                )
        else:
            report.write("No high-priority indicators found.\n")

        report.write(
            "\n====================================================="
        )


entries = load_feed("threat_feed.txt")
unique_entries = remove_duplicates(entries)

type_counts = count_by_field(unique_entries, "type")
severity_counts = count_by_field(unique_entries, "severity")
high_priority = get_high_priority_entries(unique_entries)

print("========== THREAT FEED ANALYZER ==========\n")

print(f"Original Entries: {len(entries)}")
print(f"Unique Entries: {len(unique_entries)}")
print(f"Duplicates Removed: {len(entries) - len(unique_entries)}")

print("\nIOC Type Summary:")

for ioc_type, count in type_counts.items():
    print(f"{ioc_type}: {count}")

print("\nSeverity Summary:")

for severity, count in severity_counts.items():
    print(f"{severity}: {count}")

print("\nHigh-Priority Indicators:")

for entry in high_priority:
    print(
        f"{entry['severity']} | "
        f"{entry['type']} | "
        f"{entry['indicator']} | "
        f"{entry['description']}"
    )

save_report(
    entries,
    unique_entries,
    type_counts,
    severity_counts,
    high_priority
)

print("\nReport saved as threat_feed_report.txt")