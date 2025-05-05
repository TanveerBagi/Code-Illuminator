import subprocess
import os

ERROR_EXPLANATIONS = {
    "W292": "Missing newline at end of file.",
    "E302": "Expected 2 blank lines, found 1.",
    "E231": "Missing whitespace after ',', ';', or ':'.",
    "F401": "Module imported but unused.",
    "E501": "Line too long.",
}

def analyze_code(code):
    temp_file = "temp_code.py"
    with open(temp_file, "w") as f:
        f.write(code.rstrip() + "\n")

    result = subprocess.run(["flake8", temp_file], capture_output=True, text=True)
    os.remove(temp_file)

    if not result.stdout:
        return "✅ Your code looks clean!"

    readable_output = ""
    for line in result.stdout.strip().split("\n"):
        parts = line.split(":")
        if len(parts) >= 4:
            line_no, error_code = parts[1], parts[3].split()[0]
            explanation = ERROR_EXPLANATIONS.get(error_code, "Unknown issue.")
            readable_output += f"Line {line_no}, - {explanation} ({error_code})\n"

    return readable_output.strip()

