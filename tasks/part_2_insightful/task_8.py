# Программа принимает строку и ищет имена с наибольшим кол-вом гласных букв
# Вывод: имена с максимальным кол-ом гласных, каждое с новой строки

names: list[str, ...] = input().lower().split()

# перечисляем все возможные гласные
vowels: str = 'аоеёияэыую'

# заводим переменную с макс.значением гласных в слове
max_vowels: int = 0
result: list[str, ...] = []
# перебираем все имена, введенные пользователем
for name in names:

    # заводим счетчик гласных в слове и считаем кол-во в слове
    sum_vowels: int = 0
    for vowel in vowels:
        sum_vowels += name.count(vowel)

    # если кол-во гласных превышает макс.значение гласных,
    # то добавляем в список имя
    # и присваиваем новое значение max_vowels
    if sum_vowels > max_vowels:
        max_vowels = sum_vowels
        result.clear()
        result.append(name.capitalize())

    # если кол-во гласных равно макс.значению, то добавляем
    # имя в список result
    elif sum_vowels == max_vowels:
        result.append(name.capitalize())

# выводим результат в консоль
for i in result:
    print(i)
