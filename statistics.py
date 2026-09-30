import csvHandler

def getStatistics():
    complaints = csvHandler.readComplaints()
    total = len(complaints)
    pending = 0
    inProgress = 0
    resolved = 0
    categoryCount = {}

    for c in complaints:
        status = c.get("status", "")
        if status == "Pending":
            pending += 1
        elif status == "In Progress":
            inProgress += 1
        elif status == "Resolved":
            resolved += 1

        cat = c.get("category", "Other")
        categoryCount[cat] = categoryCount.get(cat, 0) + 1

    mostCommon = "N/A"
    if categoryCount:
        best = max(categoryCount.values())
        for k, v in categoryCount.items():
            if v == best:
                mostCommon = k
                break

    return {
        "total": total,
        "pending": pending,
        "inProgress": inProgress,
        "resolved": resolved,
        "mostCommon": mostCommon,
    }
