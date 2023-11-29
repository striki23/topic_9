# Программа меняет вводимую строку на новую.
# Если в строке присутствуют цифры, программа должна вывести каждую цифру,
# прибавив к ней символ ₽ (рубль). False в противном случае.

line = input()

new_line = ''
for i in line:
    if i in '0123456789':
        new_line += (i + '₽ ')

if not new_line:
    print(False)
else:
    print(new_line)

# -----------------------------

digits: str = '0123456789'
is_digit: bool = False

for char in line:
    if char in digits:
        is_digit = True
        print(char + '₽', end=' ')
        # print(char + chr(8381), end=' ')

if not is_digit:
    print(False)
