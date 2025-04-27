def colnum(s):
    column_number = 0
    for char in s:
        column_number = column_number * 26 + (ord(char) - ord('A')) + 1
    return column_number

s = "AA"
result = colnum(s)
print(result)