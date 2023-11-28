# Программа проверяет является ли строка палиндромом
# игнорируются все пробелы, знаки препитания и дефисы

# c = s.decode('utf-8')
line = input().lower()
wrong = [' ', '-', ',']
for symbol in wrong:
     line = line.replace(symbol, '')
print(line == line[::-1])
