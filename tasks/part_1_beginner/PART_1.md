## Начинающий

Задачи о строках без использования каких-либо встроенных методов и способов форматирования!

- [Задание 0](#задание-0)
- [Задание 1](#задание-1)
- [Задание 2](#задание-2)
- [Задание 3](#задание-3)
- [Задание 4](#задание-4)
- [Задание 5](#задание-5)
- [Задание 6](#задание-6)
- [Задание 7](#задание-7)
- [Задание 8](#задание-8)
- [Задание 9](#задание-9)
- [Задание 10](#задание-10)
- [Задание 11](#задание-11)

---

### [Задание 0](task_0.py)

Напишите программу, которая находит длину строки без использования встроенных функций.

**Входные данные:**

* Строка, для которой нужно найти длину.

**Выходные данные:**

* Длина строки (целое число).

**Примеры:**

| Ввод         | Вывод |
|:-------------|:------|
| Привет, мир! | 12    |

| Ввод   | Вывод |
|:-------|:------|
| Python | 6     |

| Ввод | Вывод |
|:-----|:------|
|      | 0     |

---

### [Задание 1](task_1.py)

Напишите программу, которая удаляет повторяющиеся символы из заданной строки, оставляя только уникальные символы.

**Входные данные:**

* Строка, из которой нужно удалить повторяющиеся символы.

**Выходные данные:**

* Строка с уникальными символами.

> Примечание:
>
> - Нельзя использовать встроенные функции и методы.
> - Гарантируется, что строка не будет пустой.

**Примеры:**

| Ввод   | Вывод |
|:-------|:------|
| aabbcc | abc   |

| Ввод   | Вывод  |
|:-------|:-------|
| Python | Python |

| Ввод              | Вывод |
|:------------------|:------|
| Gooooooooooooogle | Gogle |

| Ввод       | Вывод  |
|:-----------|:-------|
| DuckDuckGo | DuckGo |

---

### [Задание 2](task_2.py)

Напишите программу, которая принимает строку и символ, а затем находит первое вхождение введенного символа в строке.
Если искомый символ присутствует, программа должна вывести его индекс (позицию) в строке, иначе -1.

**Входные данные:**

* Строка и искомый символ.

**Выходные данные:**

* Индекс искомого символа или -1, если символ не найден.

> Примечание:
>
> - Поиск символа должен быть регистрозависимым.
> - Если символ встречается несколько раз в строке, программа должна вернуть индекс первого вхождения слева.

**Примеры:**

| Ввод        | Вывод |
|:------------|:------|
| Python<br>h | 3     |

| Ввод              | Вывод |
|:------------------|:------|
| Привет, Мир!<br>М | 8     |

| Ввод       | Вывод |
|:-----------|:------|
| hello<br>l | 2     |

| Ввод      | Вывод |
|:----------|:------|
| Java<br>j | -1    |

| Ввод     | Вывод |
|:---------|:------|
| Lua<br>a | 2     |

| Ввод       | Вывод |
|:-----------|:------|
| Cplus<br>C | 0     |

---

### [Задание 3](task_3.py)

Напишите программу, которая принимает строку и выводит все её подстроки, начиная с первого символа и
увеличивая длину подстроки на один символ с каждым шагом.

**Входные данные:**

* Одна строка.

**Выходные данные:**

* Строки выводятся в порядке увеличения длины подстроки.

> Примечание:
>
> Пропускайте пробелы, если они находятся в начале строки.

**Примеры:**

| Ввод    | Вывод                                                |
|:--------|:-----------------------------------------------------|
| Самолет | С<br>Са<br>Сам<br>Само<br>Самол<br>Самоле<br>Самолет |

| Ввод       | Вывод                                          |
|:-----------|:-----------------------------------------------|
| la&#160;la | l<br>la<br>la&#160;<br>la&#160;l<br>la&#160;la |

| Ввод                                 | Вывод                                     |
|:-------------------------------------|:------------------------------------------|
| &#160;&#160;&#160;&#160;&#160;Yandex | Y<br>Ya<br>Yan<br>Yand<br>Yande<br>Yandex |

| Ввод                              | Вывод                                                                                                                                                                                                                                                                                                                 |
|:----------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Go&#160;&#160;oo&#160;&#160;oogle | G<br>Go<br>Go&#160;<br>Go&#160;&#160;<br>Go&#160;&#160;o<br>Go&#160;&#160;oo<br>Go&#160;&#160;oo&#160;<br>Go&#160;&#160;oo&#160;&#160;<br>Go&#160;&#160;oo&#160;&#160;o<br>Go&#160;&#160;oo&#160;&#160;oo<br>Go&#160;&#160;oo&#160;&#160;oog<br>Go&#160;&#160;oo&#160;&#160;oogl<br>Go&#160;&#160;oo&#160;&#160;oogle |

---

### [Задание 4](task_4.py)

Напишите программу, которая принимает строку. Если в строке присутствуют цифры, программа должна вывести
каждую цифру, прибавив к ней символ `₽` (рубль). `False` в противном случае.

**Входные данные:**

* Строка.

**Выходные данные:**

* Строка, в которой каждой цифре прибавлен символ `₽`, или `False`, если цифр в строке нет.

> Примечание:
>
> Все цифры выводятся на одной строке через пробел.

**Примеры:**

| Ввод          | Вывод                                                    |
|:--------------|:---------------------------------------------------------|
| 0abc123def456 | 0₽&#160;1₽&#160;2₽&#160;3₽&#160;4₽&#160;5₽&#160;6₽&#160; |

| Ввод | Вывод |
|:-----|:------|
|      | False |

| Ввод                             | Вывод                                                                    |
|:---------------------------------|:-------------------------------------------------------------------------|
| 4.05&#160;&#160;&#160;452#$12#$5 | 4₽&#160;0₽&#160;5₽&#160;4₽&#160;5₽&#160;2₽&#160;1₽&#160;2₽&#160;5₽&#160; |

| Ввод   | Вывод |
|:-------|:------|
| Python | False |

---

### [Задание 5](task_5.py)

Напишите программу, которая принимает строку и символ-разделитель.
Программа должна разделить строку, вставляя разделитель между каждым символом строки,
и вывести результат. Если символ-разделитель не указан, по умолчанию
используется `-` (дефис).

**Входные данные:**

* Строка.
* Символ-разделитель.

**Выходные данные:**

* Строка, в которой каждый символ разделен указанным символом-разделителем.

> Примечание:
> - Гарантируется, что строка не будет пустой.
> - Если символ-разделитель уже присутствует в строке, он не должен удваиваться в результирующей строке.


**Примеры:**

| Ввод     | Вывод |
|:---------|:------|
| abc<br>$ | a$b$c |

| Ввод        | Вывод     |
|:------------|:----------|
| hel@lo<br>@ | h@e@l@l@o |

| Ввод              | Вывод             |
|:------------------|:------------------|
| developer<br><br> | d-e-v-e-l-o-p-e-r |

| Ввод                | Вывод               |
|:--------------------|:--------------------|
| python-java<br><br> | p-y-t-h-o-n-j-a-v-a |

---

### [Задание 6](task_6.py)

Напишите программу, которая принимает строку и разделяет её на две подстроки. Одну, содержащую символы с
четными индексами, а другую с нечетными.

**Входные данные:**

* Строка.

**Выходные данные:**

* Две строки, разделенные символами с четными и нечетными индексами.

> Примечание:
>
> Каждая строка выводится на отдельной строке.
> Гарантируется, что длина строки больше двух символов.

**Примеры:**

| Ввод     | Вывод        |
|:---------|:-------------|
| abcdefgh | aceg<br>bdfh |

| Ввод   | Вывод      |
|:-------|:-----------|
| banana | bnn<br>aaa |

| Ввод | Вывод  |
|:-----|:-------|
| py   | p<br>y |

---

### [Задание 7](task_7.py)

Напишите программу, которая определяет, является ли введенная строка палиндромом
(читается одинаково как с начала, так и с конца).

**Входные данные:**

* Одно слово.

**Выходные данные:**

* `True`, если слово является палиндромом, `False` в противном случае.

> Примечание:
>
> - Гарантируется, что строка будет в нижнем регистре и не будет пустой.

**Примеры:**

| Ввод    | Вывод |
|:--------|:------|
| racecar | True  |

| Ввод  | Вывод |
|:------|:------|
| заказ | True  |

| Ввод    | Вывод |
|:--------|:------|
| укулеле | False |

| Ввод  | Вывод |
|:------|:------|
| level | True  |

---

### [Задание 8](task_8.py)

Напишите программу, которая принимает строку и находит наибольший символа в этой строке.

**Входные данные:**

* Строка.

**Выходные данные:**

* Максимальный код символа в строке и сам символ.

> Примечание:
>
> - Гарантируется, что строка не будет пустой.
> - Код символа - это целое число, представляющее позицию символа в таблице символов Unicode.


**Примеры:**

| Ввод     | Вывод    |
|:---------|:---------|
| Assembly | 121<br>y |

| Ввод           | Вывод     |
|:---------------|:----------|
| Питон & Python | 1090<br>т |

| Ввод     | Вывод   |
|:---------|:--------|
| 1&#160;0 | 49<br>1 |

| Ввод | Вывод   |
|:-----|:--------|
| aaaa | 97<br>a |

---

### [Задание 9](task_9.py)

Напишите программу, которая принимает строку и подсчитывает количество слов в ней. Слова разделяются пробелами.

**Входные данные:**

* Строка.

**Выходные данные:**

* Количество слов (целое число).

> Примечание:
>
> Считайте слова как последовательности символов, разделенные пробелами.
> Не учитывайте знаки препинания внутри слов.


**Примеры:**

| Ввод         | Вывод |
|:-------------|:------|
| Привет, Мир! | 2     |

| Ввод      | Вывод |
|:----------|:------|
| Однослово | 1     |

| Ввод                                      | Вывод |
|:------------------------------------------|:------|
| ЗдесьБольшоеКоличествоСимволовВОдномСлове | 1     |

| Ввод                                                                                                                             | Вывод |
|:---------------------------------------------------------------------------------------------------------------------------------|:------|
| Это тест&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;с большим количеством пробелов | 6     |

| Ввод                                                                                            | Вывод |
|:------------------------------------------------------------------------------------------------|:------|
| &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;a$b$ c#@3, sd2135% %$DS&#160;&#160;&#160;&#160; | 4     |

| Ввод | Вывод |
|:-----|:------|
|      | 0     |

---

### [Задание 10](task_10.py)

Напишите программу, которая считает количество гласных и согласных букв
(как в русском, так и в английском) в заданной строке.

**Входные данные:**

* Строка.

**Выходные данные:**

* Количество гласных и согласных букв.

> Примечание:
>
> Программа должна учитывать как прописные, так и заглавные буквы.

**Примеры:**

| Ввод          | Вывод  |
|:--------------|:-------|
| Hello, World! | 3<br>7 |

| Ввод         | Вывод  |
|:-------------|:-------|
| Привет, Мир! | 3<br>6 |

| Ввод                                                     | Вывод    |
|:---------------------------------------------------------|:---------|
| Съешь ещё этих мягких французских булок, да выпей же чаю | 18<br>28 |

| Ввод                                        | Вывод    |
|:--------------------------------------------|:---------|
| The quick brown fox jumps over the lazy dog | 11<br>24 |

| Ввод         | Вывод  |
|:-------------|:-------|
| !@#$%^&*()_+ | 0<br>0 |

| Ввод   | Вывод  |
|:-------|:-------|
| 123456 | 0<br>0 |

---

### [Задание 11](task_11.py)

Напишите программу, которая проверяет, является ли введенная строка числом (целым или с плавающей точкой).

**Входные данные:**

* Строка, которую нужно проверить на число.

**Выходные данные:**

* `True`, если строка является числом, и `False` в противном случае.

> Примечание:
>
> - Гарантируется, что знаки `+` и `-` вводится перед числом, но не более одного раза и только в начале строки.
> - Гарантируется, что символ `.` вводится после числа.
> - Строка может содержать пробелы в начале и/или конце, они должны игнорироваться при проверке.

**Примеры:**

| Ввод | Вывод |
|:-----|:------|
| 84   | True  |

| Ввод         | Вывод |
|:-------------|:------|
| 3.1415926535 | True  |

| Ввод                  | Вывод |
|:----------------------|:------|
| &#160;&#160;&#160;+23 | True  |

| Ввод                      | Вывод |
|:--------------------------|:------|
| -3.1415&#160;&#160;&#160; | True  |

| Ввод       | Вывод |
|:-----------|:------|
| 0.5.325353 | False |

| Ввод   | Вывод |
|:-------|:------|
| Python | False |