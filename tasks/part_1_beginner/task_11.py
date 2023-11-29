# Программа проверяет, является ли введенная строка числом (целым или с плавающей точкой).
# Выводит True в случае если number число, False в ином случае

number: str = input()

digits: str = '0123456789'
signs: str = '+-.'
is_num: bool = ...

for i in number:
    if i not in ...:
        print(False)
        break

print(is_num)
