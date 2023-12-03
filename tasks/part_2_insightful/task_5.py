# Программа заменяе все гласные в словах на знак '?'
line: str = input()

vowels: str = 'AaEeIiOoUuАаИиОоУуЫыЭэЁёЕеЮюЯя'

for symbol in vowels:
    line = line.replace(symbol, '?')
print(line)
