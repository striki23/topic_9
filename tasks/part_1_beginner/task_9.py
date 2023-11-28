# TODO: Пожалуйста, добавьте свой код ниже с комментариями и понятными названиями переменных.
line = input()

new_line = ''
for i in line:
    if i != ' ':
        new_line += '1'
    else:
        new_line += '0'

if '0' not in new_line and '1' in new_line:
    counter = 1
if '1' not in new_line:
    counter = 0
else:
    counter = 1
    x = new_line.count('101')
    counter += x

print(counter)
# НЕ РАБОТАЕТ правильно!!!!