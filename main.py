import complaintManager
import contactInfo
import feedback
import statistics
import troubleshooting
import csvHandler


def showMainMenu():
    print("\n" + "=" * 48)
    print("                 HOSTEL HELP DESK")
    print("=" * 48)
    print("A simple place to report issues and follow them up.\n")
    print("  1  Student Help     Get advice, report an issue, or track it")
    print("  2  Staff Desk       Review complaints and update their status")
    print("  0  Exit")
    return input("\nWhere would you like to go? ").strip()


def showStudentMenu():
    print("\n--------------- STUDENT SERVICES ---------------")
    print("1. Get Help / File a Complaint")
    print("2. My Complaints")
    print("3. Track a Complaint ID")
    print("4. Give Feedback on a Resolved Complaint")
    print("5. Hostel Contact Information")
    print("0. Back to Main Menu")
    return input("\nChoose an option: ").strip()


def showAdministrationMenu():
    print("\n--------------- ADMINISTRATION ---------------")
    print("1. View All Complaints")
    print("2. Update Complaint Status")
    print("3. Complaint Statistics")
    print("4. Delete a Complaint")
    print("5. View Feedback")
    print("6. Hostel Contact Information")
    print("0. Back to Main Menu")
    return input("\nChoose an option: ").strip()


def runComplaintHelp():
    guidedIssue = troubleshooting.guideComplaint()
    if guidedIssue is not None:
        category, issueSummary = guidedIssue
        complaintManager.registerComplaint(category, issueSummary)


def showStatistics():
    stats = statistics.getStatistics()
    print("\nComplaint Statistics")
    print(f"  Total complaints: {stats['total']}")
    print(f"  Pending: {stats['pending']}")
    print(f"  In Progress: {stats['inProgress']}")
    print(f"  Resolved: {stats['resolved']}")
    print(f"  Most common category: {stats['mostCommon']}")


def studentPortal():
    while True:
        choice = showStudentMenu()
        if choice == "1":
            runComplaintHelp()
        elif choice == "2":
            complaintManager.myComplaints()
        elif choice == "3":
            complaintManager.searchComplaint()
        elif choice == "4":
            feedback.submitFeedback()
        elif choice == "5":
            contactInfo.showContactInfo()
        elif choice == "0":
            return
        else:
            print("Invalid choice. Select one of the listed options.")


def administrationPortal():
    while True:
        choice = showAdministrationMenu()
        if choice == "1":
            complaintManager.viewAll()
        elif choice == "2":
            complaintManager.updateComplaintStatus()
        elif choice == "3":
            showStatistics()
        elif choice == "4":
            complaintManager.deleteComplaint()
        elif choice == "5":
            feedback.viewFeedback()
        elif choice == "6":
            contactInfo.showContactInfo()
        elif choice == "0":
            return
        else:
            print("Invalid choice. Select one of the listed options.")


def main():
    csvHandler.createCsv()
    while True:
        choice = showMainMenu()
        if choice == "1":
            studentPortal()
        elif choice == "2":
            administrationPortal()
        elif choice == "0":
            print("\nThanks for using the Hostel Help Desk.")
            break
        else:
            print("Invalid choice. Select one of the listed options.")


if __name__ == "__main__":
    main()
