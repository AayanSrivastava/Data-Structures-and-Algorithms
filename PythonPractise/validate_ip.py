def validate_ip(ip):

    parts = ip.split(".")

    if len(parts) != 4:
        return False

    for part in parts:

        if not part.isdigit():
            return False

        num = int(part)

        if num < 0 or num > 255:
            return False

    return True


print(validate_ip("192.168.1.1"))  # True
print(validate_ip("999.1.1.1"))    # False


#using regex
import re

def validate_ip(ip):

    pattern = r"^(?:\d{1,3}\.){3}\d{1,3}$"

    if not re.match(pattern, ip):
        return False

    parts = ip.split(".")

    return all(0 <= int(p) <= 255 for p in parts)


print(validate_ip("192.168.1.1"))