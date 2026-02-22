import re
match = re.search(r"(\d{3})-(\d{4})", "123-4567")
print(match.group(1))

# s1 = re.split("\

import re

text = "Price is 500 and tax is 50"
print(re.findall(r"\d+", text))

def validate(email):
    pattern = r"^[\w.-]+@[\w.-]+\.\w+$"
    return re.match(pattern, email) is not None
    
print(validate("aayansrivastava13@gmail.com"))
# pattern = r"^[\w.-]+@[\w.-]+\.\w+$"

pattern = r"^\d{10}$"
print(bool(re.match(pattern, "9876543210")))
# pattern = r"^\d{10}$"

pattern = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&]).{8,}$"
print(bool(re.match(pattern, "Test@123")))

output = """

IPv4 Sessions
NeighAddr        LD/RD         RH/RS     State     Int
10.1.1.2         1001/1002     Up        Up        GigabitEthernet0/0
10.1.1.3         1003/1004     Up        Down      GigabitEthernet0/1
10.1.1.4         1005/1006     Up        Up        GigabitEthernet0/2
    
"""
pattern = r"^(\d+\.\d+\.\d+\.\d+)\s+(\d+/\d+)\s+\w+\s+(Up|Down)\s+\w+$"

import re

output = """
IPv4 Sessions
NeighAddr        LD/RD         RH/RS     State     Int
10.1.1.2         1001/1002     Up        Up        GigabitEthernet0/0
10.1.1.3         1003/1004     Up        Down      GigabitEthernet0/1
10.1.1.4         1005/1006     Up        Up        GigabitEthernet0/2
"""

pattern = r"(\d+\.\d+\.\d+\.\d+)\s+\d+/\d+\s+\w+\s+(Up|Down)\s+\S+"
# pattern = r"(\d+\.\d+\.\d+\.\d+)\s+\d+/\d+\s+\w+\s+(Up|Down)\s+\S+"


matches = re.findall(pattern, output)

print(matches)

for ip, state in matches:
    if state == "Up":
        print(f"{ip} BFD is UP")
    else:
        print(f"{ip} BFD is DOWN")


import re

def validate_ospf_neighbors(output):

    pattern = re.compile(
        r"(?P<neighbor_id>\d{1,3}(?:\.\d{1,3}){3})\s+"
        r"(?P<priority>\d+)\s+"
        r"(?P<state>\S+)\s+"
        r"(?P<dead_time>\d{2}:\d{2}:\d{2})\s+"
        r"(?P<address>\d{1,3}(?:\.\d{1,3}){3})\s+"
        r"(?P<interface>\S+)"
    )

    all_valid = True

    for match in pattern.finditer(output):

        neighbor_id = match.group("neighbor_id")
        state = match.group("state")

        if "FULL" not in state:
            print(f"FAIL: Neighbor {neighbor_id} not FULL ({state})")
            all_valid = False
        else:
            print(f"PASS: Neighbor {neighbor_id} is FULL")

    return all_valid

output = """
Neighbor ID     Pri   State           Dead Time   Address         Interface
10.1.1.2          1   FULL/DR         00:00:33    192.168.1.2     GigabitEthernet0/0
10.1.1.3          1   FULL/BDR        00:00:31    192.168.1.3     GigabitEthernet0/1
10.1.1.4          1   2WAY/DROTHER    00:00:39    192.168.1.4     GigabitEthernet0/2
"""

result = validate_ospf_neighbors(output)

if result:
    print("\nOSPF validation PASSED")
else:
    print("\nOSPF validation FAILED")