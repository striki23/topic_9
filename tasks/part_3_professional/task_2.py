"""Программа 'Конвертер валют'."""

print('Программа "Конвертер валют"')

while True:
    try:
        number: int = int(input(
            '\nВыберите операцию (0 для выхода):'
            '\n1. Конвертировать рубли в доллары'
            '\n2. Конвертировать доллары в рубли'
            '\nВведите номер операции: '
        ))
    except ValueError:
        print('Введите числовое значение (номер операции)')
        continue

    # number = input(
    #     '\nВыберите операцию (0 для выхода):'
    #     '\n1. Конвертировать рубли в доллары'
    #     '\n2. Конвертировать доллары в рубли'
    #     '\nВведите номер операции: '
    # )
    # if not number.isdigit():
    #     print('Введите числовое значение (номер операции)')
    #     continue

    if number == 0:
        print('До свидания!')
        break

    if number not in (1, 2):
        print('Неверный выбор операции. Попробуйте ещё раз.')
        continue

    rate_hint = 'Введите курс доллара к рублю:'
    budget_hint = 'Введите количество рублей:'
    sign = 'USD'

    if number == 2:
        rate_hint = 'Введите курс рубля к доллару:'
        budget_hint = 'Введите количество долларов:'
        sign = 'RUB'

    rate = float(input(rate_hint))
    budget = float(input(budget_hint))
    print(f'Вы получите {(budget * rate):.2f} {sign}\n')
