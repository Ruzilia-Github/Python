1. Для удаления ненужных символов можно использовать конструкцию:

import re

words = re.sub(r'[.,;:-?-!]', '', input())
(где

re.sub(pattern, replacement, original_string)

pattern: знаки препинания или шаблон выражений, которые мы хотим заменить.

replacement: строка, которая будет заменять шаблон.)))
______________________________________________________________________

words = [i.lower().strip('.,,,!,?,:,;,-') for i in input().split()]

__________________________________________________
words2 = words1.replace('!','')

2.   Посчитать  кол-во  значений в  строке

text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'
result = {}
for num in text:
    result[num] = result.get(num, 0) + 1

________________________________
dct = {}
lst = ["dog", "cat","dog"]
for word in lst:
    dct[word] = dct.get(word, 0) + 1

________________________________
numbers = [9, 8, 32, 1, 10, 1, 10, 23, 1, 4, 10, 4, 2, 2, 2, 2, 1, 10, 1, 2, 2, 32, 23, 23]

result = {}
for num in numbers:
    if num not in result:
        result[num] = 1
    else:
        result[num] += 1

3. Соединение 2 списков  в словарь

letters = [c for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789']
morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '-----', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.']
d = dict(zip(letters, morse))

4  Красивое  оформление словоря

from pprint import pprint
pprint(dict)

5. Создание  словоря  из строки "Змея: язык программирования Python", где "Змея"  - ключ "язык программирования Python"-значение
result = {}
for i in range(int(input())):
    tmp = input().split(': ')
    result[tmp[0]] = tmp[1]
______________
d = {}
for _ in range(int(input())):
    a, *b = input().split()
    d.update(dict.fromkeys(b, a))

https://www.youtube.com/watch?v=4jUxJULjvpY&t=2s&ab_channel=IsraelAizen
_____________

s = {}
for i in range(int(input())):
    a = input().split()
    s[a[0]] = tuple(a[1:])

________________
s = {}
for i in range(int(input())):
    a = input().split()
    s[a[0]] = tuple(a[1:])
_________________
d={}
for _ in range(int(input())):
    a=input().split()
    for c in a[1:]:
        d[c]=a[0]

________________
def sity_country(num):
    dct = {}
    for i in range(num):
        a, *b = tuple(input().split())
        b = tuple(b)
        dct[b] = a
    return dct



6 Добавление элементов  в словать

dic.setdefault(name, []).append(dog)

https: // www.youtube.com / watch?v = WNs9 - 1s4ir0 & ab_channel = PrettyPrinted

https: // www.youtube.com / watch?v = DyQrka_nbWs & ab_channel = PythonProgrammer



