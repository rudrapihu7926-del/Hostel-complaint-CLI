import csv
import os

import csvHandler
import validators

FEEDBACK_FILE = "feedback.csv"
FIELDS = ["complaintId", "rating", "comment"]


def readFeedback():
    if not os.path.exists(FEEDBACK_FILE):
        with open(FEEDBACK_FILE, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDS)
            writer.writeheader()
    with open(FEEDBACK_FILE, "r", newline="") as file:
        return list(csv.DictReader(file))


def submitFeedback():
    complaintId = input("\nEnter resolved Complaint ID: ").strip()
    if not validators.checkComplaintId(complaintId):
        print("Enter a valid complaint ID, such as HC001.")
        return

    complaint = next((c for c in csvHandler.readComplaints()
                      if c.get("complaintId", "").lower() == complaintId.lower()), None)
    if complaint is None:
        print("Complaint not found.")
        return
    if complaint.get("status") != "Resolved":
        print("Feedback can be submitted after the complaint is resolved.")
        return

    feedbackEntries = readFeedback()
    if any(entry.get("complaintId", "").lower() == complaintId.lower()
           for entry in feedbackEntries):
        print("Feedback has already been submitted for this complaint.")
        return

    rating = input("Rate the resolution from 1 to 5: ").strip()
    if not validators.checkChoice(rating, 5):
        print("Enter a rating from 1 to 5.")
        return

    comment = input("Comment (optional): ").strip()
    with open(FEEDBACK_FILE, "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        writer.writerow({
            "complaintId": complaintId.upper(),
            "rating": rating,
            "comment": comment,
        })
    print("Thank you for your feedback.")


def viewFeedback():
    feedbackEntries = readFeedback()
    if not feedbackEntries:
        print("\nNo feedback has been submitted.")
        return

    print("\nComplaint Feedback")
    for entry in feedbackEntries:
        print(f"  Complaint: {entry['complaintId']}  |  Rating: {entry['rating']}/5")
        print(f"  Comment: {entry['comment'] or '(no comment)'}")
