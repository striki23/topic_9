# Программа, подсчитывает количество символов заданной строки
# Нельзя использовать встроенные функции и методы
line: str = input()

counter: int = 0
for _ in line:
    counter += 1

print(counter)
