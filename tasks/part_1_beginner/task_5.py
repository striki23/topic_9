"""Программа принимает строку и символ-разделитель.
Программа разделяет строку, вставляя разделитель между каждым символом строки.
Если символ-разделитель не указан, по умолчанию используется - (дефис)."""

line = input()
symbol = input()

if not symbol:
    symbol = '-'

new_line = ''
for i in line[:-1]:
    if i == symbol:
        continue
    new_line += i + symbol
print(new_line+line[-1])