from datetime import datetime, timedelta

import complaintProgress

start = datetime(2026, 9, 30, 12)

assert complaintProgress.calculateProgress("Pending", start, start, start) == 0
assert complaintProgress.calculateProgress(
    "Pending", start, start, start + timedelta(days=2)
) == 50
assert complaintProgress.calculateProgress("In Progress", start, start, start) == 50
assert complaintProgress.calculateProgress(
    "In Progress", start, start, start + timedelta(days=2)
) == 75
assert complaintProgress.calculateProgress(
    "In Progress", start, start, start + timedelta(days=4)
) == 99
assert complaintProgress.calculateProgress("Resolved", start, start, start) == 100

print("Progress checks passed.")
