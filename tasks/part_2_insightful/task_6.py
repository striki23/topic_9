# Программа подсчитывает и выводит количество
# букв, цифр и пробелов в введенной строке line
line: str = input()

# letters, digits, spaces = 0, 0, 0
letters = digits = spaces = 0

for el in line:
    if el.isalpha():
        letters += 1
    elif el.isnumeric():
        digits += 1
    elif el.isspace():
        spaces += 1

print(letters, digits, spaces, sep='\n')
