# На ввод подается строка, где слова разделены * (звездочкой)
# Каждое слово выводиться с новой строки с заглавной буквы

line: str = input().split(sep='*')

for word in line:
    print(word.capitalize())
