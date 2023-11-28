# Программа подсчитывает и выводит количество
# букв, цифр и пробелов в введенной строке line
line = input()

# заносим в список letters все элементы строки, которые являются буквой
letters = [i for i in line if i.isalpha()]
# заносим в список digit все элементы строки, которые являются цифрой
digit = [i for i in line if i.isnumeric()]
# заносим в список space все элементы строки, которые являются пробелом
space = [i for i in line if i.isspace()]

# выводим кол-во букв и цифр, пробелов
print(len(letters))
print(len(digit))
print(len(space))

