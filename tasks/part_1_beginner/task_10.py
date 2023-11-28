# Программа считает количество гласных и согласных букв
# (как в русском, так и в английском) в заданной строке.

line = input()

vowels = 'AaEeIiOoUuYyАаИиОоУуЫыЭэЁёЕеЯя'
consonants = 'BbCcDdFfGgHhJjKkLlMm' \
             'NnPhQqRrSsTtVvWwXxZz' \
             'БбВвГгДдЖжЗзЙйКкЛлМмЪъ' \
             'НнПпРрСсТтФфХхЦцЧчШшЩщ'
vowels_counter = 0
consonants_consonants = 0

for i in line:
    if i in vowels:
        vowels_counter += 1
    if i in consonants:
        consonants_consonants += 1
print(vowels_counter)
print(consonants_consonants)
