import hashlib
from datetime import datetime
from pathlib import Path


BASE_DIRECTORY = Path(__file__).resolve().parent

LOG_FILE = BASE_DIRECTORY / "security_logs.txt"
IOC_FILE = BASE_DIRECTORY / "iocs.txt"
SAMPLE_FILE = BASE_DIRECTORY / "sample_file.txt"
REPORT_DIRECTORY = BASE_DIRECTORY / "reports"


def load_lines(file_path):
    """
    Read a text file and return a list of non-empty lines.
    """

    try:
        with file_path.open("r", encoding="utf-8") as file:
            return [
                line.strip()
                for line in file
                if line.strip()
            ]

    except FileNotFoundError:
        print(f"\nFile not found: {file_path.name}")
        return []

    except OSError as error:
        print(f"\nCould not read {file_path.name}: {error}")
        return []


def classify_event(log_entry):
    """
    Determine the security category of a log entry.
    """

    event_categories = [
        "MALWARE DETECTED",
        "FAILED LOGIN",
        "PORT SCAN",
        "WARNING",
        "DNS REQUEST",
        "INFO"
    ]

    uppercase_entry = log_entry.upper()

    for category in event_categories:
        if category in uppercase_entry:
            return category

    return "OTHER"


def analyze_logs(logs):
    """
    Count security events by category.
    """

    event_counts = {
        "INFO": 0,
        "WARNING": 0,
        "FAILED LOGIN": 0,
        "PORT SCAN": 0,
        "MALWARE DETECTED": 0,
        "DNS REQUEST": 0,
        "OTHER": 0
    }

    for log_entry in logs:
        category = classify_event(log_entry)
        event_counts[category] += 1

    return event_counts


def display_log_summary(logs, event_counts):
    """
    Display a summary of security events.
    """

    print("\n========== SECURITY EVENT SUMMARY ==========\n")
    print(f"Total Events: {len(logs)}\n")

    for category, count in event_counts.items():
        print(f"{category:<20}: {count}")

    print("\n============================================")


def search_logs(logs):
    """
    Search security logs for a user-provided term.
    """

    search_term = input(
        "\nEnter an IP address, username, event or keyword: "
    ).strip()

    if not search_term:
        print("\nSearch term cannot be empty.")
        return

    matches = []

    for log_entry in logs:
        if search_term.lower() in log_entry.lower():
            matches.append(log_entry)

    print(
        f"\n========== SEARCH RESULTS: {search_term} ==========\n"
    )

    if matches:
        for match in matches:
            print(match)

        print(f"\nMatches Found: {len(matches)}")
    else:
        print("No matching log entries found.")

    print("\n==================================================")


def scan_for_iocs(logs, iocs):
    """
    Search security logs for known Indicators of Compromise.
    """

    matches = []

    for log_entry in logs:
        for ioc in iocs:
            if ioc.lower() in log_entry.lower():
                matches.append({
                    "ioc": ioc,
                    "log": log_entry
                })

    print("\n========== IOC SCAN RESULTS ==========\n")

    if matches:
        for match in matches:
            print(f"IOC: {match['ioc']}")
            print(f"Log: {match['log']}")
            print("--------------------------------------")

        print(f"\nIOC Matches Found: {len(matches)}")
    else:
        print("No known Indicators of Compromise were found.")

    print("\n======================================")

    return matches


def calculate_sha256(file_path):
    """
    Calculate the SHA-256 hash of a file.
    """

    try:
        sha256_hash = hashlib.sha256()

        with file_path.open("rb") as file:
            while True:
                data_chunk = file.read(4096)

                if not data_chunk:
                    break

                sha256_hash.update(data_chunk)

        return sha256_hash.hexdigest()

    except FileNotFoundError:
        print(f"\nFile not found: {file_path.name}")
        return None

    except OSError as error:
        print(f"\nCould not hash {file_path.name}: {error}")
        return None


def display_file_hash():
    """
    Calculate and display the sample file's SHA-256 hash.
    """

    file_hash = calculate_sha256(SAMPLE_FILE)

    print("\n========== FILE HASH ANALYSIS ==========\n")

    if file_hash:
        print(f"File: {SAMPLE_FILE.name}")
        print(f"SHA-256: {file_hash}")
    else:
        print("The file hash could not be calculated.")

    print("\n========================================")


def get_critical_events(logs):
    """
    Return high-priority security events.
    """

    critical_keywords = [
        "MALWARE DETECTED",
        "PORT SCAN",
        "FAILED LOGIN"
    ]

    critical_events = []

    for log_entry in logs:
        uppercase_entry = log_entry.upper()

        for keyword in critical_keywords:
            if keyword in uppercase_entry:
                critical_events.append(log_entry)
                break

    return critical_events


def generate_soc_report(logs, event_counts, ioc_matches):
    """
    Generate a timestamped SOC investigation report.
    """

    REPORT_DIRECTORY.mkdir(exist_ok=True)

    current_time = datetime.now()
    timestamp = current_time.strftime("%Y%m%d_%H%M%S")

    report_path = (
        REPORT_DIRECTORY /
        f"soc_investigation_report_{timestamp}.txt"
    )

    critical_events = get_critical_events(logs)
    sample_hash = calculate_sha256(SAMPLE_FILE)

    try:
        with report_path.open("w", encoding="utf-8") as report:
            report.write(
                "========== SOC INVESTIGATION REPORT ==========\n\n"
            )

            report.write(
                f"Generated: "
                f"{current_time.strftime('%Y-%m-%d %H:%M:%S')}\n"
            )

            report.write(f"Total Security Events: {len(logs)}\n")
            report.write(
                f"IOC Matches Found: {len(ioc_matches)}\n\n"
            )

            report.write("EVENT SUMMARY\n")
            report.write("---------------------------------------------\n")

            for category, count in event_counts.items():
                report.write(f"{category}: {count}\n")

            report.write("\nCRITICAL EVENTS\n")
            report.write("---------------------------------------------\n")

            if critical_events:
                for event in critical_events:
                    report.write(f"ALERT: {event}\n")
            else:
                report.write("No critical events detected.\n")

            report.write("\nIOC MATCHES\n")
            report.write("---------------------------------------------\n")

            if ioc_matches:
                for match in ioc_matches:
                    report.write(
                        f"IOC: {match['ioc']}\n"
                        f"LOG: {match['log']}\n\n"
                    )
            else:
                report.write("No IOC matches detected.\n")

            report.write("\nFILE HASH ANALYSIS\n")
            report.write("---------------------------------------------\n")

            if sample_hash:
                report.write(f"File: {SAMPLE_FILE.name}\n")
                report.write(f"SHA-256: {sample_hash}\n")
            else:
                report.write("File hash unavailable.\n")

            report.write("\nRECOMMENDED ACTIONS\n")
            report.write("---------------------------------------------\n")
            report.write(
                "1. Investigate systems associated with IOC matches.\n"
            )
            report.write(
                "2. Isolate hosts affected by detected malware.\n"
            )
            report.write(
                "3. Review repeated failed-login activity.\n"
            )
            report.write(
                "4. Block confirmed malicious IP addresses and domains.\n"
            )
            report.write(
                "5. Preserve logs and forensic evidence.\n"
            )
            report.write(
                "6. Escalate critical incidents to the response team.\n"
            )

            report.write(
                "\n=============================================="
            )

        print(f"\nSOC report created: {report_path.name}")

    except OSError as error:
        print(f"\nCould not create SOC report: {error}")


def display_menu():
    """
    Display the SOC Analyst Toolkit menu.
    """

    print("\n========== SOC ANALYST TOOLKIT ==========")
    print("1. Analyze security logs")
    print("2. Search security logs")
    print("3. Scan logs for IOCs")
    print("4. Calculate file SHA-256 hash")
    print("5. Generate SOC investigation report")
    print("6. Exit")
    print("=========================================")


def main():
    """
    Run the SOC Analyst Toolkit.
    """

    logs = load_lines(LOG_FILE)
    iocs = load_lines(IOC_FILE)

    if not logs:
        print(
            "\nThe toolkit cannot continue without security logs."
        )
        return

    event_counts = analyze_logs(logs)
    latest_ioc_matches = []

    while True:
        display_menu()

        choice = input("\nSelect an option from 1 to 6: ").strip()

        if choice == "1":
            display_log_summary(logs, event_counts)

        elif choice == "2":
            search_logs(logs)

        elif choice == "3":
            latest_ioc_matches = scan_for_iocs(logs, iocs)

        elif choice == "4":
            display_file_hash()

        elif choice == "5":
            if not latest_ioc_matches:
                latest_ioc_matches = scan_for_iocs(logs, iocs)

            generate_soc_report(
                logs,
                event_counts,
                latest_ioc_matches
            )

        elif choice == "6":
            print("\nExiting SOC Analyst Toolkit.")
            break

        else:
            print(
                "\nInvalid selection. Please choose a number from 1 to 6."
            )


if __name__ == "__main__":
    main()