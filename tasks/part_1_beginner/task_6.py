# TODO: Пожалуйста, добавьте свой код ниже с комментариями и понятными названиями переменных.
line = input()

# new_line_1 = ''
# new_line_2 = ''

# counter = 0
# for i in line:
#     if counter % 2 == 0:
#         new_line_1 += i
#     else:
#         new_line_2 += i
#     counter += 1
#
# print(new_line_1)
# print(new_line_2)

# ----------------------

odds: str = line[0::2]
evens: str = line[1::2]

print(odds, evens, sep='\n')
