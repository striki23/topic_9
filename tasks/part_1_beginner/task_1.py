# Программа, которая удаляет повторяющиеся символы из заданной строки
# Нельзя использовать встроенные функции и методы

line = input()

new_line = ''
for i in line:
    if i not in new_line:
        new_line += i

print(new_line)
