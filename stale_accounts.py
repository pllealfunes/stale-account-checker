import csv
from datetime import datetime, timedelta



FILENAME = "sample_accounts.csv"
STALE_DAYS = 90

flagged = []
approved = []
todays_date = datetime.today() 
cutoff_date=todays_date - timedelta(days=STALE_DAYS)
REPORT_FILENAME = "flagged_accounts.csv"
skipped=0

try:

    with open(FILENAME, newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            reasons = []
            username = row["username"]
            last_login = row["last_login"]


            if username.lower().startswith("temp"):
                reasons.append("temporary account")

            if last_login == "":
                reasons.append("never logged in")
            else:
                try:
                    login_date = datetime.strptime(last_login, "%Y-%m-%d")
                except ValueError:
                    print(f"{username} has a bad login date")
                    skipped+=1
                    continue
                if login_date < cutoff_date:
                    reasons.append(f"no login in over {STALE_DAYS} days")
                        
            if reasons: 
                flagged.append({"username": username, "reason": "; ".join(reasons)})
            else:
                approved.append(username)

    with open(REPORT_FILENAME, "w", newline="") as flagged_report:
        writer = csv.DictWriter(flagged_report, fieldnames=["username", "reason"])
        writer.writeheader()
        writer.writerows(flagged)
            

    print(f"Report written to {REPORT_FILENAME}")
    print(f"{len(flagged)} flagged, {len(approved)} approved, {skipped} skipped accounts")
    print("Approved: ", approved)
    for item in flagged: print(item["username"], "-", item["reason"])

except FileNotFoundError:
    print(f"Could not find {FILENAME}. Check the file name and folder")