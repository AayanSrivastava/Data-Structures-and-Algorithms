import os
import re

repo_path = "."  # root of your repo

# Regex to find pms_tc_id = ["..."]
pms_pattern = re.compile(r"pms_tc_id\s*=\s*\[([^\]]+)\]")

ids = set()

for root, _, files in os.walk(repo_path):
    for file in files:
        if file.endswith(".py"):
            filepath = os.path.join(root, file)
            with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                for line in f:
                    match = pms_pattern.search(line)
                    if match:
                        values = [v.strip().strip('"').strip("'") for v in match.group(1).split(",")]
                        ids.update(values)

# Print all IDs
for tc_id in sorted(ids):
    print(tc_id)