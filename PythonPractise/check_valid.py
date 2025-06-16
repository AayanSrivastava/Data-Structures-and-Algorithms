class Solution:
    def is_valid_ip(self, ip):
        parts = ip.split('.')

        print(f"number of parts in ip is {parts}")
        if len(parts)!=4:
            return False
        
        for part in parts:
            if not part.isdigit():
                return False
            

            num = int(part)

            if num < 0 or num > 255:
                return False

            if part != str(num):
                return False
        
        return True
    
if __name__ == "__main__":
    obj = Solution()
    ips = ["192.168.1.0", "255.255.255.255", "256.1.1.1", "192.168.01.1", "abc.def.ghi.jkl"]
    for ip in ips:
        print(obj.is_valid_ip(ip))
    # ip = input("Enter the ip")
    # ip1, ip2, ip3 = input.split()
    mylist = list(map, int(input().split()))
    


# import ipaddress

# def is_valid_ip(ip):
#     try:
#         ipaddress.IPv4Address(ip)
#         return True
#     except ipaddress.AddressValueError:
#         return False

def parse_ip_route(output):
    routes = {}
    for line in output.splitlines():
        if "via" in line:
            parts = line.split()
            routes[parts[1]] = parts[3]  # destination: next-hop
    return routes