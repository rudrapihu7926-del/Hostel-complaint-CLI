from datetime import datetime, timedelta

STATUSES = ["Pending", "In Progress", "Resolved"]
PENDING_DAYS = 2
IN_PROGRESS_DAYS = 4


def currentTimestamp():
    return datetime.now().isoformat(timespec="microseconds")


def parseTimestamp(value):
    if isinstance(value, datetime):
        return value
    return datetime.fromisoformat(value)


def calculateProgress(status, createdAt, statusUpdatedAt=None, now=None):
    if status not in STATUSES:
        return None
    if status == "Resolved":
        return 100

    currentTime = now or datetime.now()
    createdTime = parseTimestamp(createdAt)

    if status == "Pending":
        elapsed = max(timedelta(0), currentTime - createdTime)
        progress = elapsed.total_seconds() / (PENDING_DAYS * 86400) * 50
        return min(int(progress + 0.5), 50)

    progressStartedAt = parseTimestamp(statusUpdatedAt or createdAt)
    elapsed = max(timedelta(0), currentTime - progressStartedAt)
    progress = 50 + elapsed.total_seconds() / (IN_PROGRESS_DAYS * 86400) * 49
    # Time estimates stop at 99%; only staff confirmation can complete a complaint.
    return min(int(progress + 0.5), 99)
