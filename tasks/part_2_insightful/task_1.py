"""Программа принимает строку и подсчитывает количество слов в ней."""

line: str = input().split()

if not line:
    print(False)
else:
    print(len(line))
