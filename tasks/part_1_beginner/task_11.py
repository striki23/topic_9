# Программа проверяет, является ли введенная строка числом (целым или с плавающей точкой).
# Выводит True в случае если number число, False в ином случае

number = input()

for i in number:
    if i not in '+-0123456789. ':
        print(False)
        break
else:
    print(True)
