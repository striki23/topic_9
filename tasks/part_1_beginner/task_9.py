# Программа принимает строку и подсчитывает количество слов в ней.
# Слова разделяются пробелами.
line: str = input()

counter: int = 0
is_word: bool = True

for symbol in line:
    if symbol != ' ' and is_word is True:
        counter += 1
        is_word = False

    elif symbol == ' ' and is_word is False:
        is_word = True

print(counter)
