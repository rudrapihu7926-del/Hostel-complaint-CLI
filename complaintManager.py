import csvHandler
import complaintProgress
import validators

def makeComplaintId(complaints):
    highest = 0
    for c in complaints:
        cid = c.get("complaintId", "")
        if cid.startswith("HC") and cid[2:].isdigit():
            n = int(cid[2:])
            if n > highest:
                highest = n
    return f"HC{highest + 1:03d}"


def registerComplaint(category, issueSummary):
    print("\nFile Complaint")
    studentName = input("Student name: ").strip()
    if not validators.checkName(studentName):
        print("Name required.")
        return

    roomNumber = input("Room number: ").strip()
    if not validators.checkName(roomNumber):
        print("Room required.")
        return

    details = input("Add any other details (optional): ").strip()
    description = issueSummary
    if details:
        description += f" Extra details: {details}"

    complaints = csvHandler.readComplaints()
    complaintId = makeComplaintId(complaints)
    timestamp = complaintProgress.currentTimestamp()

    complaints.append({
        "complaintId": complaintId,
        "studentName": studentName,
        "roomNumber": roomNumber,
        "category": category,
        "description": description,
        "status": "Pending",
        "createdAt": timestamp,
        "statusUpdatedAt": timestamp,
    })
    csvHandler.writeComplaints(complaints)
    print(f"Registered! ID: {complaintId}")


def displayComplaints(complaints):
    if not complaints:
        print("\nNo complaints.")
        return

    for c in complaints:
        print(f"  ID: {c['complaintId']}")
        print(f"  Student: {c['studentName']}  |  Room: {c['roomNumber']}")
        print(f"  Category: {c['category']}  |  Status: {c['status']}")
        progress = complaintProgress.calculateProgress(
            c.get("status", ""), c.get("createdAt", ""), c.get("statusUpdatedAt")
        )
        if progress is not None:
            print(f"  Progress: {progress}%")
        print(f"  Description: {c['description']}")
        print("  " + "-" * 40)


def viewAll():
    complaints = csvHandler.readComplaints()
    if not complaints:
        print("\nNo complaints.")
        return
    print("\nAll Complaints")
    displayComplaints(complaints)


def searchComplaint():
    query = input("\nEnter Complaint ID: ").strip()
    if not validators.checkComplaintId(query):
        print("Enter a valid complaint ID, such as HC001.")
        return
    complaints = csvHandler.readComplaints()
    for c in complaints:
        if c.get("complaintId", "").lower() == query.lower():
            displayComplaints([c])
            return
    print("Not found.")


def myComplaints():
    identifier = input("\nEnter your student name or room number: ").strip()
    if not validators.checkName(identifier):
        print("Name or room number cannot be empty.")
        return

    complaints = csvHandler.readComplaints()
    matches = [c for c in complaints
               if c.get("studentName", "").lower() == identifier.lower()
               or c.get("roomNumber", "").lower() == identifier.lower()]
    if not matches:
        print("No matching complaints.")
        return

    print("\nMy Complaints")
    displayComplaints(matches)


def deleteComplaint():
    complaintId = input("\nEnter Complaint ID to delete: ").strip()
    if not validators.checkComplaintId(complaintId):
        print("Enter a valid complaint ID, such as HC001.")
        return
    complaints = csvHandler.readComplaints()
    for i, c in enumerate(complaints):
        if c.get("complaintId", "").lower() == complaintId.lower():
            confirm = input("Delete? (y/n): ").strip().lower()
            if confirm == "y":
                complaints.pop(i)
                csvHandler.writeComplaints(complaints)
                print("Deleted.")
            else:
                print("Cancelled.")
            return
    print("Not found.")


def updateComplaintStatus():
    complaintId = input("\nEnter Complaint ID to update: ").strip()
    if not validators.checkComplaintId(complaintId):
        print("Enter a valid complaint ID, such as HC001.")
        return

    complaints = csvHandler.readComplaints()
    for complaint in complaints:
        if complaint.get("complaintId", "").lower() == complaintId.lower():
            print("\nStatuses:")
            for number, status in enumerate(complaintProgress.STATUSES, 1):
                print(f"  {number}. {status}")
            choice = input("Select status: ").strip()
            if not validators.checkChoice(choice, len(complaintProgress.STATUSES)):
                print("Invalid status choice.")
                return
            complaint["status"] = complaintProgress.STATUSES[int(choice) - 1]
            complaint["statusUpdatedAt"] = complaintProgress.currentTimestamp()
            csvHandler.writeComplaints(complaints)
            progress = complaintProgress.calculateProgress(
                complaint["status"], complaint["createdAt"], complaint["statusUpdatedAt"]
            )
            print(f"Status updated. Current progress: {progress}%")
            return
    print("Complaint not found.")
