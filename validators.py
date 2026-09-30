def checkChoice(choice, maxChoice):
    try:
        num = int(choice)
        return 1 <= num <= maxChoice
    except ValueError:
        return False


def checkName(text):
    return text is not None and text.strip() != ""


def checkComplaintId(text):
    if text is None:
        return False
    complaintId = text.strip().upper()
    return complaintId.startswith("HC") and complaintId[2:].isdigit()
