import csv

FILENAME = "sample_accounts.csv"

flagged = []
approved = []

with open(FILENAME, newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        username = row["username"]
        if username.lower().startswith("temp"):
            flagged.append(username)
        else:
            approved.append(username)

print(f"{len(flagged)} flagged, {len(approved)} approved")
print("Flagged: ", flagged)