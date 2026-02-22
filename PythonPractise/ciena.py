# ##increment ip

# import ipaddress

# def increment_ip(ip_str, step=1):
#     """Increment an IPv4 address by a given step."""
#     ip = ipaddress.IPv4Address(ip_str)
#     new_ip = ip + step
#     return str(new_ip)

# # Example usage
# ip = "192.168.1.1"
# for i in range(5):
#     ip = increment_ip(ip)
#     print(ip)


# # Decorators
# def div(a,b):
#     print(a/b)

# def smart_div(func):
#     def inner(a,b):
#         if a<b:
#             a,b = b,a
#         return func(a,b)
#     return inner

# div = smart_div(div)
# div(2,4)

# #Generators
# squares = (x*x for x in range(5))
# for num in squares:
#     print(num)

# def squares():
#     n = 1
    
#     while n <= 10:
#         sq = n*n
#         yield sq
#         n+=1

# values=squares()
# for i in values:
#     print(i)


# # Count word frequency
# text = "python is easy and python is powerful"
# words = text.split()
# freq = {}

# for word in words:
#     freq[word] = freq.get(word, 0) + 1

# print(freq)