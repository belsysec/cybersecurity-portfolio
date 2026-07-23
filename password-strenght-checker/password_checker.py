password = input("Enter a password: ")

score = 0
feedback = []
common_passwords = [
    "password",
    "password123",
    "123456",
    "12345678",
    "qwerty",
    "admin",
    "welcome",
    "letmein"
]
if len(password) >= 12:
    score += 1
else:
    feedback.append("Use at least 12 characters.")

if any(char.isupper() for char in password):
    score += 1
else:
    feedback.append("Add at least one uppercase letter.")

if any(char.islower() for char in password):
    score += 1
else:
    feedback.append("Add at least one lowercase letter.")

if any(char.isdigit() for char in password):
    score += 1
else:
    feedback.append("Add at least one number.")

if any(not char.isalnum() for char in password):
    score += 1
else:
    feedback.append("Add at least one special character.")

if password.lower() in common_passwords:
    feedback.append("This is a commonly used password. Choose something unique.")
    score = 0    
print(f"Password Score: {score}/5")
bars = "█" * score + "░" * (5 - score)
print(f"Strength: {bars}")
if score == 5:
    print("Strong Password 💪")
elif score >= 3:
    print("Medium Password 👍")
else:
    print("Weak Password ❌")

if feedback:
    print("\nSuggestions:")
    for message in feedback:
        print("-", message)