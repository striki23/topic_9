# Программа принимает строку и символ, затем подсчитывает,
# сколько раз символ встречается в строке, без учета регистра.

line: str = input().lower()
symbol: str = input().lower()

if symbol not in line:
    print(False)
else:
    print(line.count(symbol))
