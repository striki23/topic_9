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

    if number == 0:
        print('До свидания!')
        break

    elif number == 1:
        rate = float(input('Введите курс доллара к рублю:'))
        budget = float(input('Введите количество рублей:'))
        print(f'Вы получите {(budget * rate):.2f} USD\n')

    elif number == 2:
        rate = float(input('Введите курс рубля к доллару:'))
        budget = float(input('Введите количество долларов:'))
        print(f'Вы получите {(budget * rate):.2f} RUB\n')

    else:
        print('Неверный выбор операции. Попробуйте ещё раз.\n')
