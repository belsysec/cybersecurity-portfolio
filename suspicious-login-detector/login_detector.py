log_file = "login_log.txt"

with open(log_file, "r") as file:
    lines = file.readlines()
failed_count = 0
failed_users = {}
for line in lines:
    if "LOGIN FAILED" in line:
        failed_count += 1
        username = line.split()[-1]
        if username not in failed_users:
            failed_users[username] = 1
        else:
            failed_users[username] += 1

print(f"\nTotal Failed Logins: {failed_count}")
print("\nFailed Login Summary:")
for username, attempts in failed_users.items():
    word = "attempt" if attempts == 1 else "attempts"
    print(f"{username}: {attempts} failed {word}")

    if attempts >= 3:
        print("⚠ Possible brute-force attack detected!")

        