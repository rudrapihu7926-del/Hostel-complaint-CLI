# Hostel Complaint Manager

## Problem Statement

Hostel students may face Wi-Fi, cleaning, mess, water, electricity, or maintenance problems. Informal reports can be missed, and students may not know what basic steps to try before contacting hostel staff.

## Proposed Solution

Hostel Complaint Manager is a Python command-line application. It offers category-specific suggestions first and lets a student file a complaint if the suggestions do not solve the problem. Hostel staff can review complaints, update their status, view statistics, and read feedback.

## Objectives

- Give students one place to get help and register unresolved problems.
- Keep complaint records available after the program closes by using a CSV file.
- Show an estimate of complaint progress based on status and elapsed time.
- Let staff review complaint details, update statuses, and see statistics and feedback.

## Scope and Features

### Student Services

- Choose a complaint category and see basic troubleshooting suggestions.
- For cleaning issues, choose room or washroom and receive relevant guidance.
- File a complaint with the selected category and issue details if the suggestion does not help.
- Search for a complaint, view complaints by student name or room, and submit feedback after resolution.

### Administration

- View, update, and delete complaint records.
- Review complaint statistics and submitted feedback.
- View hostel contact information.

### Progress Estimate

Progress is recalculated when a complaint is displayed. Pending advances from 0% to 50% over two days. In Progress advances from 50% to 99% over the next four days. A complaint reaches 100% only after its status is set to Resolved. Elapsed time does not resolve a complaint automatically.

## Target Users

- Hostel students who want to report an issue or check its status.
- Hostel staff who review and manage complaint records.

## Technologies

- Python 3 and its standard library
- CSV file storage through the built-in `csv` module
- Command-line interface

## Data Files

- `complaints.csv` stores complaint details, status, creation time, and last status update time.
- `feedback.csv` stores feedback ratings and comments.

## Limitations

- The student and administration portals organize the menu but do not include login or access control.
- Progress is an estimate. Staff must update a complaint to Resolved when work is actually complete.
- The project uses CSV files rather than a database, so it is suited to a small local application.
