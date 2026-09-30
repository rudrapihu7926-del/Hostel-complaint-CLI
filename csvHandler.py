import csv
import os

import complaintProgress

CSV_FILE = "complaints.csv"
FIELDS = ["complaintId", "studentName", "roomNumber", "category", "description", "status",
          "createdAt", "statusUpdatedAt"]


def createCsv():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=FIELDS)
            writer.writeheader()


def readComplaints():
    createCsv()
    with open(CSV_FILE, "r", newline="") as f:
        reader = csv.DictReader(f)
        sourceFields = reader.fieldnames or []
        complaints = list(reader)

    # Remove demo rows left by earlier versions when migrating an existing file.
    originalCount = len(complaints)
    complaints = [c for c in complaints if c.get("recordType") != "Demo"]
    changed = sourceFields != FIELDS or len(complaints) != originalCount
    for complaint in complaints:
        if not complaint.get("createdAt"):
            complaint["createdAt"] = complaintProgress.currentTimestamp()
            changed = True
        if not complaint.get("statusUpdatedAt"):
            complaint["statusUpdatedAt"] = complaint["createdAt"]
            changed = True

    if changed:
        writeComplaints([{field: complaint.get(field, "") for field in FIELDS}
                         for complaint in complaints])
    return complaints


def writeComplaints(complaints):
    with open(CSV_FILE, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(complaints)
