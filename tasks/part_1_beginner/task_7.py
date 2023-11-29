# Программа проверяет является ли слово палиндроном.

word: str = input()

print(word == word[::-1])

# Вариант №2

length: int = len(word)
right: int = length - 1

for i in range(length // 2):
    if word[i] != word[right]:
        print(False)
        break
    right -= 1
else:
    print(True)
