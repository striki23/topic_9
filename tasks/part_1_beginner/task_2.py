# Программы выводит индекс первого найденого symbol в строке line
# Если symbol в строке line не найден выводится -1
line = input()
symbol = input()

index = 0
for i in line:
    if i == symbol:
        print(index)
        break
    index += 1
else:
    print(-1)
