"""Программа принимает строку и символ-разделитель.
Программа разделяет строку, вставляя разделитель между каждым символом строки.
Если символ-разделитель не указан, по умолчанию используется - (дефис)."""

line: str = input()
symbol: str = input()

if not symbol:
    symbol = '-'

# -----------------

for index in range(len(line)):
    # если символ в строке такой же как разделитель, пропускаем его
    if line[index] == symbol:
        continue
    # если символ в строке последний, то печатаем только
    # букву (без разделителя)
    elif index == len(line) - 1:
        print(line[index])
    # в остальных случаях печатаем букву + разделитель
    else:
        print(line[index] + symbol, end='')

# --------Variant 2-------------

length: int = len(line)
out_line: str = ''

for index in range(length):
    if line[index] != symbol:
        out_line += line[index]
        if index != length - 1:
            out_line += symbol
