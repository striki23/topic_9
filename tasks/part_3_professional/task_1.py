"""Программа принимает строку и используя форматирование,
добавляет по 5 символов ~ (тильда) с каждой стороны. """

line: str = input()

# определяем общую длину строки и добавляем 10 (5 '~' с каждой стороны)
length: int = len(line) + 10

print(f"{line:~^{length}}")
