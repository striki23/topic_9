# Программа подсчитывает и выводит количество
# букв, цифр и пробелов в введенной строке line
line: str = input()

# # заносим в список letters все элементы строки, которые являются буквой
# letters: list[str, ...] = [i for i in line if i.isalpha()]
# # заносим в список digit все элементы строки, которые являются цифрой
# digits: list[str, ...] = [i for i in line if i.isnumeric()]
# # заносим в список space все элементы строки, которые являются пробелом
# spaces: list[str, ...] = [i for i in line if i.isspace()]
#
# # выводим кол-во букв и цифр, пробелов
# print(len(letters), len(digits), len(spaces), sep='\n')

letters, digits, spaces = (0, 0, 0)

for el in line:
    if el.isalpha():
        letters += 1
    elif el.isnumeric():
        digits += 1
    elif el.isspace():
        spaces += 1

print(letters, digits, spaces, sep='\n')