def load_logs(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return [line.strip() for line in file if line.strip()]


def search_logs(logs, search_term):
    matches = []

    for log in logs:
        if search_term.lower() in log.lower():
            matches.append(log)

    return matches


def save_results(search_term, matches):
    with open("search_results.txt", "w", encoding="utf-8") as report:
        report.write("========== THREAT HUNT RESULTS ==========\n\n")
        report.write(f"Search Term: {search_term}\n")
        report.write(f"Matches Found: {len(matches)}\n\n")

        if matches:
            for match in matches:
                report.write(f"{match}\n")
        else:
            report.write("No matching log entries were found.\n")

        report.write("\n==========================================")


logs = load_logs("security_logs.txt")

print("========== LOG SEARCH TOOL ==========")
print("Examples: Alice, LOGIN FAILED, malware, 192.168.1.50")

search_term = input("\nEnter a username, IP, domain, or event type: ").strip()

if not search_term:
    print("Search term cannot be empty.")
else:
    matches = search_logs(logs, search_term)

    print(f"\nMatches Found: {len(matches)}\n")

    if matches:
        for match in matches:
            print(match)
    else:
        print("No matching log entries were found.")

    save_results(search_term, matches) 
    print("\nResults saved as search_results.txt")