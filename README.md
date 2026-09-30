# Hostel Complaint Manager

A Python command-line program for recording and following up on hostel complaints.

## Features

- Student Help offers issue-specific suggestions before filing a complaint.
- Students can view their complaints, track an ID, and give feedback after resolution.
- Staff can view, update, and delete complaints, view statistics, and review feedback.
- Progress estimates recalculate from elapsed time and the current status.
- Hostel contact information is available from both portals.

## Requirements

- Python 3.x
- No external packages

## Run

From this folder, run:

```bash
python main.py
```

Complaints are stored in `complaints.csv` and remain available after restarting the program. Feedback is stored separately in `feedback.csv`.

Progress recalculates whenever a complaint is viewed. Pending complaints move from 0% to 50% over two days. In Progress complaints move from 50% to 99% over the next four days. A complaint reaches 100% only after staff manually set it to Resolved.

Run `python checkProgress.py` to check the progress formula with fixed timestamps. Only resolved complaints can receive feedback, and each complaint can receive feedback once. Feedback entries remain in `feedback.csv` if their complaint is later deleted.

## Project Files

- `main.py` — displays the Student Help and Staff Desk menus.
- `troubleshooting.py` — shows issue-specific suggestions and routes unresolved issues to complaint filing.
- `complaintManager.py` — registers, displays, searches, deletes, and updates complaints.
- `complaintProgress.py` — calculates progress using complaint timestamps and status.
- `checkProgress.py` — checks progress thresholds without waiting for real time to pass.
- `feedback.py` — submits and displays complaint feedback.
- `csvHandler.py` — reads and writes the complaints CSV file.
- `validators.py` — checks required input, category choices, and complaint IDs.
- `statistics.py` — calculates complaint totals and category counts.
- `contactInfo.py` — displays hostel contact information.
- `feedback.csv` — stores ratings and comments after resolution.
- `complaints.csv` — stores complaint details, creation time, and last status update time.
- `statement.md` — describes the project problem and scope.

## Example

```text
Select category: 1 (Wi-Fi)
Select the Wi-Fi issue: 2 (Slow connection)
Suggested check: Try another device or move closer to the access point.
Did this solve the problem? (y/n): n
Student name: Arjun
Room number: B205
Add any other details (optional): It is still slow
Registered! ID: HC006
```

New complaints start with the `Pending` status. Status changes remain manual; elapsed time never marks a complaint Resolved. New mess complaints use the `Mess` category. Older records saved as `Food` remain readable. The student and staff menus organize options but do not provide login or access control.
