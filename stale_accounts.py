import csv
from datetime import datetime, timedelta

FILENAME = "sample_accounts.csv"
STALE_DAYS = 90

flagged = []
approved = []
todays_date = datetime.today() 
cutoff_date=todays_date - timedelta(days=STALE_DAYS)

with open(FILENAME, newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        username = row["username"]
        last_login = row["last_login"]

        if  last_login != "":
            login_date = datetime.strptime(last_login, "%Y-%m-%d")
            if username.lower().startswith("temp") or login_date < cutoff_date:
                flagged.append(username)
            else:
                        approved.append(username)
        else:
            approved.append(username)

print(f"{len(flagged)} flagged, {len(approved)} approved")
print("Flagged: ", flagged)
print("Approved: ", approved)