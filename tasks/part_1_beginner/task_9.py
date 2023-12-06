# Программа принимает строку и подсчитывает количество слов в ней.
# Слова разделяются пробелами.
line: str = input()

counter: int = 0
# is_word: bool = True
is_word: bool = False

for symbol in line:
    # if symbol != ' ' and is_word is True:
    if symbol != ' ' and not is_word:
        counter += 1
        # is_word = False
        is_word = True

    # elif symbol == ' ' and is_word is False:
    elif symbol == ' ' and is_word:
        # is_word = True
        is_word = False

print(counter)
