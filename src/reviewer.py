def review_code(code):
    issues = []

    if "print" in code:
        issues.append("Avoid excessive print statements in production code.")

    if len(code) < 20:
        issues.append("Code is too short, may lack meaningful logic.")

    if "==" in code:
        issues.append("Ensure proper comparison logic is used.")

    return issues
