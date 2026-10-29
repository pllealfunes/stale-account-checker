# Stale Account Checker

A small Python practice project that reviews a list of user accounts and flags the ones a person should look at.

**Status: work in progress.**

## What works now

- Reads accounts from a CSV file (`sample_accounts.csv`, all made-up data)
- Flags usernames that start with `temp`
- Prints a count of flagged and approved accounts

## Planned

- Flag accounts that haven't logged in for more than 90 days
- Flag accounts that have never logged in
- Write the flagged accounts, with reasons, to a CSV report
- Handle a missing or badly formatted input file

## How to run

```bash
python3 stale_accounts.py
```

## Notes

This is a learning project that practices Python file handling, dates and error handling. All data is fictional.
