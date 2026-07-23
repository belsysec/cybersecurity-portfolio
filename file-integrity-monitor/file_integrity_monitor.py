import hashlib
import os

filename = "sample.txt"
baseline_file = "baseline.hash"

with open(filename, "rb") as file:
    data = file.read()

current_hash = hashlib.sha256(data).hexdigest()

if not os.path.exists(baseline_file):

    with open(baseline_file, "w") as file:
        file.write(current_hash)

    print("✅ Baseline hash created.")

else:

    with open(baseline_file, "r") as file:
        original_hash = file.read()

    if current_hash == original_hash:
        print("✅ File integrity verified.")

    else:
        print("🚨 WARNING! File has been modified!")