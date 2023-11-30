# Программа считает количество гласных и согласных букв
# (как в русском, так и в английском) в заданной строке.

line = input()

vowels: str = 'AaEeIiOoUuАаИиОоУуЫыЭэЁёЕеЮюЯя'
consonants: str = ('BbCcDdFfGgHhJjKkLlMm'
                   'NnPpQqRrSsTtVvWwXxYyZz'
                   'БбВвГгДдЖжЗзЙйКкЛлМмЬьЪъ'
                   'НнПпРрСсТтФфХхЦцЧчШшЩщ')
vowels_counter = 0
consonants_counter = 0

for i in line:
    if i in vowels:
        vowels_counter += 1
    elif i in consonants:
        consonants_counter += 1

print(vowels_counter, consonants_counter, sep='\n')
