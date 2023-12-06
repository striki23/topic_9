# Программа принимает на вход строку и преобразует её в три варианта записи
# camelCase, PascalCase и snake_case
line: str = input()
capital_line: list[str, ...] = (line.title()).split()

temp: str = ''.join(capital_line)

s1: str = 'camel' + temp
s2: str = 'Pascal' + temp
s3 = 'snake_' + ('_'.join(line.lower().split()))

print(s1, s2, s3, sep='\n')
