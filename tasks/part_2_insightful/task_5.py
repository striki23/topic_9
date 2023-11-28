# Программа заменяем все гласные в словах на знак '?'
line = input().lower()

vowels = [
    'a', 'e', 'o', 'y', 'i', 'а', 'о', 'u',
    'е', 'ё', 'у', 'и', 'я', 'ы', 'ю', 'э'
]
new_line = ''
for symbol in vowels:
    line = line.replace(symbol, '?')
# почему если мы задаем новую переменную, то не работает (new_line = line.replace(symbol, '?'))
print(line)