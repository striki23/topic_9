# Программа, которая удаляет повторяющиеся символы из заданной строки
# Нельзя использовать встроенные функции и методы

line: str = input()

new_line: str = ''
for char in line:
    if char not in new_line:
        new_line += char

print(new_line)
