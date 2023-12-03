"""Программа принимает на вход имена, фамилии и отчества людей и
выводит пронумерованную таблицу инициалов каждого человека."""

# создаем список для сохранения введеных ФИО
names: list[list, ...] = []

# заводим переменную самой длинной фамилии
max_surname: int = 0
while True:
    name_user: list[str, ...] = input().split()
    if name_user[0].lower() == 'end':
        break
    names.append(name_user)

# определяем макс длину фамилии
    lenght_surname = len(name_user[0])
    if lenght_surname > max_surname:
        max_surname = lenght_surname

# выводим шапку таблицы
print(f"{'№':^3} {'ФИО':^{max_surname}}")

# заводим счетчик номеров
n = 1
for name in names:
    fio = f'{name[0].title()} {name[1][0].title()}.{name[2][0].title()}.'
    print(f"{n:02} | {fio}")
    n += 1
