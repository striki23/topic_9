# Программа проверяет, является ли введенная строка числом (целым или с плавающей точкой).
# Выводит True в случае если number число, False в ином случае

number: str = input()

digits: str = '+-.0123456789'
is_num: bool = True
is_point: bool = False

for symbol in number:
# если символ пробел - игнорируем, переходим к следующему
    if symbol == ' ':
        continue
# если символ нет в digits, завершаем цикл и выводим False
    elif symbol not in digits:
        is_num = False
        break
# если символ точка, проверяем это первая точка или нет
    elif symbol == '.' and is_point is False:
        is_point = True
    elif symbol == '.' and is_point is True:
        is_num = False
        break

print(is_num)
