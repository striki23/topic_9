"""Вводится скидка в форсате х% на товары и их цены (без скидки)
Программа вычисляет размер скидки, цену со скидкой на все товары
и выводит их в консоль"""

discount: int = int(input())
# prices: list[float, ...] = list(map(float, input().split()))
prices: list[float, ...] = [float(num) for num in input().split()]

if 0 < discount < 100:
    print(f"{'Название':<15}"
          f"{'Цена':<10}"
          f"{'Сумма скидки':<15}"
          f"{'Новая цена':<10}")
    for idx, price in enumerate(prices, start=1):
        discount_value: float = price * discount / 100
        new_price: float = price - discount_value

        product = f'Товар {idx}'
        print(f"{product:<15}"
              f"{price:<10.2f}"
              f"{discount_value:<15.2f}"
              f"{new_price:<10.2f}")
else:
    print('Размер скидки должен быть больше 0 и не должен превышать 100')
