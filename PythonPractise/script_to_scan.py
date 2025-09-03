import os
import re

repo_path = "."  # root of your repo

class_pattern = re.compile(r"class\s+(\w+)")  # capture class name
pms_pattern = re.compile(r"pms_tc_id\s*=\s*\[([^\]]+)\]")

ids = set()
current_class = None

for root, _, files in os.walk(repo_path):
    for file in files:
        if file.endswith(".py"):
            filepath = os.path.join(root, file)
            with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                for line in f:
                    class_match = class_pattern.search(line)
                    if class_match:
                        current_class = class_match.group(1)

                    match = pms_pattern.search(line)
                    if current_class and "L3TC_FUNC_RSVP" in current_class and match:
                        values = [v.strip().strip('"').strip("'") for v in match.group(1).split(",")]
                        ids.update(values)

# Print all IDs
for tc_id in sorted(ids):
    print(tc_id)