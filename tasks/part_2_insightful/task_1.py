"""Программа принимает строку и подсчитывает количество слов в ней."""

chars: list = input().split()

if not chars:
    print(False)
else:
    print(len(chars))
