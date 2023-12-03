"""Вводится скидка в форсате х% на товары и их цены (без скидки)
Программа вычисляет размер скидки, цену со скидкой на все товары
и выводит их в консоль"""

discount: int = int(input())
prices: list[float, ...] = list(map(float, input().split()))

if 0 < discount < 100:
    n = 1
    print(f"{'Название':<15}{'Цена':<10}{'Сумма скидки':<15}{'Новая цена':<10}")
    for price in prices:
        discount_value = price * discount / 100
        new_price = price - discount_value
        print(f"Товар {n:<9}{price:<10.2f}{discount_value:<15.2f}{new_price:<10.2f}")
        n += 1
else:
    print('Размер скидки должен быть больше 0 и не должен превышать 100')
