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
    elif symbol == '.' and not is_point:
        is_point = True
    elif symbol == '.' and is_point:
        is_num = False
        break

print(is_num)

# -----------------------------

digits: str = '0123456789'
symbols: str = '+-.'
is_num: bool = True
count_dots: int = 0
for num in number:
    if ((num not in digits)
            and (num not in symbols)
            and (num != ' ')):
        is_num = False
        break
    elif num == '.':
        count_dots += 1
    if count_dots > 1:
        is_num = False
        break
