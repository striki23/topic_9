# Программа, которая принимает строку и
# находит наибольший символ в этой строке.

line = input()

codes = []
for i in line:
    codes.append(ord(i))
    max_code = max(codes)
print(max_code)
print(chr(max_code))
