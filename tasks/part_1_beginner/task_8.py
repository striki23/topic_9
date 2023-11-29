# Программа, которая принимает строку и
# находит наибольший символ в этой строке.

line = input()

codes: list[int, ...] = []
for i in line:
    codes.append(ord(i))
    max_code = max(codes)

print(max_code)
print(chr(max_code))

# -------------------------------

max_code_of_char: int = 0
char: str | None = None

for let in line:
    let_code: int = ord(let)

    if let_code > max_code_of_char:
        max_code_of_char = let_code
        char = let

print(max_code_of_char, char, sep='\n')
