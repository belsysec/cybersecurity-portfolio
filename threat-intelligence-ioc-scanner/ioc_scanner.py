def load_file(filename):
    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()

    cleaned_lines = []

    for line in lines:
        cleaned_line = line.strip()

        if cleaned_line:
            cleaned_lines.append(cleaned_line)

    return cleaned_lines


def scan_logs(iocs, logs):
    matches = []

    for log in logs:
        for ioc in iocs:
            if ioc.lower() in log.lower():
                matches.append({
                    "ioc": ioc,
                    "log": log
                })

    return matches


def classify_ioc(ioc):
    if ioc.replace(".", "").isdigit():
        return "IP Address"

    elif "." in ioc and len(ioc) < 64:
        return "Domain"

    else:
        return "File Hash"


def generate_report(matches):
    with open("ioc_scan_report.txt", "w", encoding="utf-8") as report:
        report.write("========== IOC SCAN REPORT ==========\n\n")

        report.write(f"Total IOC Matches: {len(matches)}\n\n")

        if matches:
            for match in matches:
                ioc_type = classify_ioc(match["ioc"])

                report.write(f"IOC: {match['ioc']}\n")
                report.write(f"Type: {ioc_type}\n")
                report.write(f"Log Entry: {match['log']}\n")
                report.write("--------------------------------------\n")
        else:
            report.write("No indicators of compromise were detected.\n")

        report.write("\n======================================")


iocs = load_file("iocs.txt")
logs = load_file("network_logs.txt")

matches = scan_logs(iocs, logs)

print("========== IOC SCAN RESULTS ==========")
print(f"Total IOC Matches: {len(matches)}\n")

if matches:
    for match in matches:
        ioc_type = classify_ioc(match["ioc"])

        print(f"IOC Detected: {match['ioc']}")
        print(f"Type: {ioc_type}")
        print(f"Log Entry: {match['log']}")
        print()
else:
    print("No indicators of compromise were detected.")

print("======================================")

generate_report(matches)

print("\nIOC scan report saved as ioc_scan_report.txt")