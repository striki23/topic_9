# Программа принимает строку и символ, затем подсчитывает,
# сколько раз символ встречается в строке, без учета регистра.

line = input().lower()
symbol = input().lower()

if symbol not in line:
    print(False)
else:
    print(line.count(symbol))
