import os
import re

repo_path = "."  # root of your repo

# Find classes with RSVP in the name
class_pattern = re.compile(r"class\s+(\w*RSVP\w*)")

# Match pms_tc_id = ["..."] (list of strings)
pms_pattern = re.compile(r"pms_tc_id\s*=\s*\[([^\]]+)\]")

for root, _, files in os.walk(repo_path):
    for file in files:
        if file.endswith(".py"):
            filepath = os.path.join(root, file)
            with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                lines = f.readlines()

            current_class = None
            for line_num, line in enumerate(lines, start=1):
                class_match = class_pattern.search(line)
                if class_match:
                    current_class = class_match.group(1)

                if current_class:
                    pms_match = pms_pattern.search(line)
                    if pms_match:
                        # Extract inside list and clean values
                        values = [v.strip().strip('"').strip("'") for v in pms_match.group(1).split(",")]
                        print(f"{filepath}:{line_num} | Class: {current_class} | pms_tc_id = {values}")
