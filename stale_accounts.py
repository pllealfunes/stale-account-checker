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
        reasons = []
        username = row["username"]
        last_login = row["last_login"]


        if username.lower().startswith("temp"):
            reasons.append("temporary_access")

        if last_login == "":
            reasons.append("never logged in")
        else:
             login_date = datetime.strptime(last_login, "%Y-%m-%d")
             if login_date < cutoff_date:
                reasons.append("stale (over 90 days)")
                    
        if reasons: 
           flagged.append({"username": username, "reason": "; ".join(reasons)})
        else:
            approved.append(username)
            


print(f"{len(flagged)} flagged, {len(approved)} approved")
print("Approved: ", approved)
for item in flagged: print(item["username"], "-", item["reason"])