# программа принимает строку и вычисляет отношение гласных букв в процентах
line: str = input().lower()

vowels: str = 'eyuioaёеуаыоэяию'
counter: int = 0
for i in line:
    if i in vowels:
        counter += 1
rate: float = counter / len(line)

print('Отношение гласных: {0:0>5.2%}'.format(rate))
# print(f'Отношение гласных: {rate:0>5.2%}')
