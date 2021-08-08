1. Для удаления ненужных символов можно использовать конструкцию:

import re

words = re.sub(r'[.,;:-?-!]', '', input())
(где

re.sub(pattern, replacement, original_string)

pattern: знаки препинания или шаблон выражений, которые мы хотим заменить.

replacement: строка, которая будет заменять шаблон.)))
______________________________________________________________________

words = [i.lower().strip('.,,,!,?,:,;,-') for i in input().split()]

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

3.