import validators

CATEGORIES = ["Wi-Fi", "Electricity", "Water", "Cleaning", "Maintenance", "Mess", "Other"]


def chooseFrom(options, prompt):
    for number, option in enumerate(options, 1):
        print(f"  {number}. {option}")
    choice = input(prompt).strip()
    if not validators.checkChoice(choice, len(options)):
        print("Invalid choice.")
        return None
    return options[int(choice) - 1]


def getIssueHelp(category):
    if category == "Wi-Fi":
        issue = chooseFrom(["Cannot connect", "Slow connection", "Network is missing"],
                           "Select the Wi-Fi issue: ")
        if issue == "Cannot connect":
            suggestion = "Turn Wi-Fi off and on, then reconnect to the hostel network."
        elif issue == "Slow connection":
            suggestion = "Try another device or move closer to the access point."
        elif issue == "Network is missing":
            suggestion = "Check whether the network appears on another device, then restart Wi-Fi."
        else:
            return None
    elif category == "Cleaning":
        area = chooseFrom(["Room", "Washroom"], "Which area needs cleaning? ")
        if area is None:
            return None
        issue = f"{area} cleaning"
        if area == "Room":
            suggestion = "Check whether housekeeping has visited; contact hostel staff if the room was missed."
        else:
            suggestion = "Check whether washroom cleaning has taken place; contact hostel staff if it was missed."
    elif category == "Mess":
        issue = chooseFrom(["Food quality", "Food hygiene", "Portion or quantity", "Meal timing"],
                           "Select the mess issue: ")
        if issue == "Food quality":
            suggestion = "Check the meal menu and tell the mess supervisor what needs improvement."
        elif issue == "Food hygiene":
            suggestion = "Do not eat food that appears unsafe; report the meal and time to mess staff."
        elif issue == "Portion or quantity":
            suggestion = "Ask mess staff whether another serving is available."
        elif issue == "Meal timing":
            suggestion = "Check the posted meal schedule and ask staff about any delay."
        else:
            return None
    elif category == "Electricity":
        issue = chooseFrom(["Light or fan not working", "Power unavailable"],
                           "Select the electricity issue: ")
        if issue is None:
            return None
        suggestion = "Check the switch and whether nearby rooms have power. Do not open electrical fittings."
    elif category == "Water":
        issue = chooseFrom(["No water", "Low water flow"], "Select the water issue: ")
        if issue is None:
            return None
        suggestion = "Check another tap; if more than one tap is affected, report it to hostel staff."
    elif category == "Maintenance":
        issue = chooseFrom(["Door or lock", "Furniture", "Other maintenance"],
                           "Select the maintenance issue: ")
        if issue is None:
            return None
        suggestion = "Stop using the item if it may be unsafe and report its location to maintenance staff."
    else:
        issue = input("Describe the issue: ").strip()
        if not validators.checkName(issue):
            print("Issue description cannot be empty.")
            return None
        suggestion = "If this quick check does not help, file a complaint for hostel staff."

    print(f"\nSuggested check: {suggestion}")
    answer = input("Did this solve the problem? (y/n): ").strip().lower()
    if answer == "y":
        print("Glad that helped. No complaint was filed.")
        return None
    if answer != "n":
        print("Please answer y or n. Start the help flow again if needed.")
        return None
    return f"{issue}: {suggestion}"


def guideComplaint():
    print("\nChoose a complaint category to see quick help first:")
    category = chooseFrom(CATEGORIES, "Select category: ")
    if category is None:
        return None
    issueSummary = getIssueHelp(category)
    if issueSummary is None:
        return None
    return category, issueSummary
