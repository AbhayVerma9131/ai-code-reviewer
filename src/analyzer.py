def analyze_code(code):
    lines = code.split("\n")
    return {
        "lines": len(lines),
        "has_loops": "for" in code or "while" in code,
        "has_functions": "def" in code
    }
