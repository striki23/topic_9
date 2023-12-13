# Программа заменяет все гласные в словах на знак '?'
line: str = input().lstrip()

vowels: str = 'AaEeIiOoUuАаИиОоУуЫыЭэЁёЕеЮюЯя'
symbol_swap: str = '?' * len(vowels)

tbl: dict = line.maketrans(vowels, symbol_swap)
print(line.translate(tbl))
