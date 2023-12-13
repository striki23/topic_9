"""Программа считает общую цену билетов
в зависимости от введенного возраста посетителей зоопарка"""

ages = map(int, input('Введите возрасты посетителей через пробел: ').split())

# создаем словарь с категориями посетителмя и нудевыми значениями
category_dict = {'baby': 0, 'child': 0, 'adult': 0, 'senior': 0}
for age in ages:
    if 0 < age <= 2:
        category_dict['baby'] += 1
    elif 3 <= age <= 12:
        category_dict['child'] += 1
    elif 13 <= age <= 64:
        category_dict['adult'] += 1
    elif 65 <= age <= 200:
        category_dict['senior'] += 1

price = (
        (category_dict['child'] * 1055)
        + (category_dict['adult'] * 2099)
        + (category_dict['senior'] * 1449)
)

TABLE_TEMPLATE: str = '{:<20}{:<25}{:<20}{:<20}'

print(TABLE_TEMPLATE.format(
    'Дети до 2-х лет',
    'Дети от 3-х до 12 лет',
    'Взрослые',
    'Пенсионеры'))

print(TABLE_TEMPLATE.format(
    category_dict['baby'],
    category_dict['child'],
    category_dict['adult'],
    category_dict['senior']))

print(f'\nОбщая стоимость билетов: {f"{price:,}₽"}')
