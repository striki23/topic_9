# Программа принимает строку и выводит все её подстроки,
# начиная с первого символа и
# увеличивая длину подстроки на один символ с каждым шагом.

line = input()

# new_line = ''
# for i in line:
#     new_line += i
# # обрабатываем случай, когда в начале строки есть пробелы
#     if new_line == ' ':
#         new_line = ''
#         continue
#     print(new_line)


# --------------------

out_line: str = ''
is_printed: bool = False

for char in line:
    if is_printed or char != ' ':
        is_printed = True
        out_line += char
        print(out_line)
