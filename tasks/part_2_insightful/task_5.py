# Программа заменяет все гласные в словах на знак '?'
line: str = input().lstrip()

vowels: str = 'AaEeIiOoUuАаИиОоУуЫыЭэЁёЕеЮюЯя'
symbol_swap: str = '?' * 30
tbl: dict = line.maketrans(vowels, symbol_swap)
print(line.translate(tbl))


# vowels: str = 'AaEeIiOoUuАаИиОоУуЫыЭэЁёЕеЮюЯя'
#
# for symbol in vowels:
#     line = line.replace(symbol, '?')
# print(line)
