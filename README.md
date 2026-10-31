# Stale Account Checker

A small Python script that reviews a CSV list of user accounts and flags the ones a person should look at: temporary accounts, accounts that have never logged in, and accounts with no login in a long time. It writes the flagged accounts, with the reasons, to a CSV report.

This is a practice project that automates one common access-review check. It is not a production tool, and all data in this repo is made up.

## Why I built it

Unused and temporary accounts are a common finding in access reviews and offboarding audits, because accounts nobody uses can be taken over or keep access they no longer need. I built this to practice automating that check while learning Python file handling, dates and error handling.

## What it does

For each account, the script checks three rules. An account can match more than one.

| Rule                                             | Reason in the report       |
| ------------------------------------------------ | -------------------------- |
| Username starts with `temp` (not case-sensitive) | `temporary account`        |
| No last login date                               | `never logged in`          |
| Last login is more than 90 days ago              | `no login in over 90 days` |

Accounts that match no rule are approved. The script prints a summary, then writes the flagged accounts to `flagged_accounts.csv`.

## Input format

A CSV file with two columns, `username` and `last_login` (`YYYY-MM-DD`, or empty if the account never logged in). See `sample_accounts.csv`:

```csv
username,last_login
jsmith,2026-10-20
mlopez,2026-10-27
tempcook,2026-10-15
tempadmin,2026-04-01
rpatel,2026-05-02
akim,2026-09-30
newuser,
dthomas,2026-02-14
cwong,2026-10-01
temp_vendor,2026-10-10
Temp_intern,2026-10-25
temp_new,
```

## How to run

Requires Python 3.9 or newer. There are no extra packages to install.

```bash
python3 stale_accounts.py
```

## Example output

Results depend on the date you run it, because "no login in over 90 days" is measured from today. This output is from a run on October 30, 2026:

```text
Report written to flagged_accounts.csv
8 flagged, 4 approved, 0 skipped accounts
Approved:  ['jsmith', 'mlopez', 'akim', 'cwong']
tempcook - temporary account
tempadmin - temporary account; no login in over 90 days
rpatel - no login in over 90 days
newuser - never logged in
dthomas - no login in over 90 days
temp_vendor - temporary account
Temp_intern - temporary account
temp_new - temporary account; never logged in
```

`flagged_accounts.csv`:

```csv
username,reason
tempcook,temporary account
tempadmin,temporary account; no login in over 90 days
rpatel,no login in over 90 days
newuser,never logged in
dthomas,no login in over 90 days
temp_vendor,temporary account
Temp_intern,temporary account
temp_new,temporary account; never logged in
```

## Error handling

- **Missing input file:** the script prints a clear message and stops, instead of showing a traceback.
- **Bad date:** a row with a date that is not in `YYYY-MM-DD` format is skipped with a warning that names the account. The summary shows how many rows were skipped. Skipped rows are not included in the report.

## Notes and limitations

- The 90-day threshold is the `STALE_DAYS` constant at the top of the script.
- The input and report file names are set in the script, not on the command line.
- The report is overwritten each time the script runs.
- It only checks login dates and username patterns. It does not check privileges, group membership or account status.
- It reads a CSV file, not a live directory such as Microsoft Entra ID.

## What I learned

- Reading and writing CSV files with Python's `csv` module
- Working with dates using `datetime`
- Collecting reasons in a list so one account can match several rules
- Handling errors with `try` and `except`
- Building a project in small, committed steps

## Ideas for next steps

- Accept the file name and threshold as command-line options
- Flag accounts with a bad date for review instead of skipping them
- Add the run date to the report

## About me

Entry-level cybersecurity professional working toward a career in cloud and identity security.
