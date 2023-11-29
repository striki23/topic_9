# Программы выводит индекс первого найденого symbol в строке line
# Если symbol в строке line не найден выводится -1
line = input()
symbol = input()

index = 0
for char in line:
    if char == symbol:
        print(index)
        break
    index += 1
else:
    print(-1)
