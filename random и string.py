# IP адрес состоит из четырех чисел из диапазона от 00 до 255255 (включительно) разделенных точкой.
#
# Напишите функцию generate_ip(), которая с помощью модуля random  генерирует и возвращает случайный корректный IP адрес.
#
# Примечание 1. Пример правильного (неправильного) IP адреса:
#
# 192.168.5.250        # правильный
# 199.300.521.255      # неправильный


#
# import random
# def generate_ip():
#    return (f'{random.randint(100, 256)}.{random.randint(100, 256)}.{random.randint(0, 9)}.{random.randint(100, 256)}')
# print(generate_ip())
#
# ___________
import random

#
# def generate_ip():
#     return '.'.join([str(random.randint(0, 255)) for _ in range(4)])
# print(generate_ip())
# _________
# import random
# def generate_ip():
#     a = []
#     for _ in range(4):
#         a.append(str(random.randint(0, 255)))
#     return '.'.join(a)
# _________________________________________________

# Почтовый индекс в Латверии имеет вид: LetterLetterNumber_NumberLetterLetter, где Letter – заглавная буква английского алфавита, Number – число от 00 до 9999 (включительно).
#
# Напишите функцию generate_index(), которая с помощью модуля randomгенерирует и возвращает случайный корректный почтовый индекс Латверии.
#
# Примечание 1. Пример правильного (неправильного) индекса Латверии:
#
# AB23_56VG          # правильный
# V3F_231GT          # неправильный
# Примечание 2. Обратите внимание на символ _ в почтовом индексе.

# import random
# import string
# def generate_ip():
#      return (f"{random.choice(string.ascii_uppercase)}{random.choice(string.ascii_uppercase)}{random.randint(0, 9)}_{random.randint(0, 9)}{random.randint(0, 9)}{random.choice(string.ascii_uppercase)}")
# print(generate_ip())
#
# _________________
#
# from random import choice, randrange
# from string import ascii_uppercase
#
# def generate_index():
#     n1, n2 = (randrange(100) for i in range(2))
#     a, b, c, d = (choice(ascii_uppercase) for i in range(4))
#     return (f'{a}{b}{n1}_{n2}{c}{d}')
#
# _________________________________________________________________
# Напишите программу, которая с помощью модуля random перемешивает случайным образом содержимое матрицы (двумерного списка).
# import random
# numbers = [[1, 2, 3, 4],
#           [5, 6, 7, 8],
#           [9, 10, 11, 12],
#           [13, 14, 15, 16]]
#
# random.shuffle(numbers)
#
# print(numbers, sep="\n")
#
# import random
# ___________________________________________________________

# Напишите программу, которая с помощью модуля random генерирует 100 случайных номеров лотерейных билетов и выводит их каждый на отдельной строке. Обратите внимание, вы должны придерживаться следующих условий:
#
# номер не может начинаться с нулей;
# номер лотерейного билета должен состоять из 7 цифр;
# все 100 лотерейных билетов должны быть различными.


# import random
#
# s =[]
# count = 0
# while count == 100:
#     n = ""
#     while len(n) < 8:
#            l = random.randint(0, 100)
#            print(l)
#            n += str(l)
#            print(n)
#            if n[0] in "0":
#                del n[0]
#     if n not in s:
#         s.append(n)
#         count += 1
#         print(n)
# ______________________________________________________________________________________
# Анаграмма – это слово образованное путём перестановки букв, составляющих другое слово.
#
# Например, слова пила и липа или пост и стоп – анаграммы.
#
# Напишите программу, которая считывает одно слово и выводит с помощью модуля random его случайную анаграмму.
#
# Примечание. Обратите внимание на то, что метод shuffle() работает со списком, а не со строкой.
#
# import random
# numbers = [i for i in input().lower()]
# random.shuffle(numbers)
# print(''.join(numbers))
#
# # _____________________________
# print(''.join(shuffle(list(input()))))
# _____________________________________________________________

# Для игры в бинго требуется карточка размером 5 \times 55×5, содержащая различные (уникальные) целые числа от 11 до 7575 (включительно), при этом центральная клетка является пустой (она заполняется числом 00).
# Напишите программу, которая с помощью модуля random генерирует и выводит случайную карточку для игры в бинго.
#
# Примечание 1. Для наглядности рекомендуем отводить на вывод каждого числа ровно 33 символа. Для этого используйте строковый метод ljust().
#
# Примечание 2. Пример возможного ответа:
#
# 1  16 31 46 61
# 10 30 42 47 68
# 3  18 0  48 63
# 9  19 34 49 70
# 5  20 35 50 65

# import random
# mtr2 =[]
# for i in range(5):
#     mtr = []
#     for j in range(5):
#         if i == 2 and j == 2:
#             mtr.append(0)
#         else:
#             numbers = random.randint(1, 75)
#             mtr.append(numbers)
#     mtr2.append(mtr)
# for i in range(5):
#     for j in range(5):
#         print(str(mtr2[i][j]).ljust(3), end=' ')
#     print()

# ____________________________________________________________________
# Напишите программу, которая с помощью модуля random генерирует nn паролей длиной mm символов, состоящих из строчных и прописных английских букв и цифр, кроме тех, которые легко перепутать между собой:
#
# «l» (L маленькое);
# «I» (i большое);
# «1» (цифра);
# «o» и «O» (большая и маленькая буквы);
# «0» (цифра).
# Формат входных данных
# На вход программе подаются два числа nn и mm, каждое на отдельной строке.
#
# Формат выходных данных
# Программа должна вывести nn паролей длиной mm символов в соответствии с условием задачи, каждый на отдельной строке.
#
# Примечание 1. Считать, что числа nn и mm всегда таковы, что требуемые пароли сгенерировать возможно.
#
# Примечание 2. В каждом пароле необязательно должна присутствовать хотя бы одна цифра и буква в верхнем и нижнем регистре.
#
# Примечание 3. Решение задачи удобно оформить в виде двух вспомогательных функций:
#
# функция generate_password(length) – возвращает случайный пароль длиной length символов;
# функция generate_passwords(count, length) – возвращает список, состоящий из count случайных паролей длиной length символов.
# Примечание 4. Приведенные ниже тесты – это лишь образцы возможного ответа. Возможны и другие способы генерации паролей.
#
# Для отладки кода 🟡
# Sample Input 1:
#
# 9
# 7
# Sample Output 1:
#
# YbykdW8
# heEWSyL
# MDxYCzf
# syWRujr
# mFGBYNJ
# bhmg5ip
# 2XmPgsx
# hy7UMVs
# JzKPyBw

# import random
#
# digits = '0123456789'
# lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
# uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#
#
# chars = ''
# n, m = int(input()), int(input())
# chars = digits + lowercase_letters +uppercase_letters
# for c in 'lI1oO0':
#     chars = chars.replace(c, '')
# for i in range(n):
#     password = ""
#     for j in range(m):
#          password += random.choice(chars)
#     print(password)

# _________________________________________________________________
# Напишите программу, которая с помощью модуля random генерирует nn паролей длиной mm символов, состоящих из строчных и прописных английских букв и цифр, кроме тех, которые легко перепутать между собой:
#
# «l» (L маленькое);
# «I» (i большое);
# «1» (цифра);
# «o» и «O» (большая и маленькая буквы);
# «0» (цифра).
# Дополнительное условие: в каждом пароле обязательно должна присутствовать хотя бы одна цифра и как минимум по одной букве в верхнем и нижнем регистре.
#
# Формат входных данных
# На вход программе подаются два числа nn и mm, каждое на отдельной строке.
#
# Формат выходных данных
# Программа должна вывести nn паролей длиной mm символов в соответствии с условием задачи, каждый на отдельной строке.
#
# Примечание 1. Считать, что числа nn и mm всегда таковы, что требуемые пароли сгенерировать возможно.
#
# Примечание 2. Решение задачи удобно оформить в виде двух вспомогательных функций:
#
# функция generate_password(length) – возвращает случайный пароль длиной length символов;
# функция generate_passwords(count, length) – возвращает список, состоящий из count случайных паролей длиной length символов.
# Примечание 3. Приведенные ниже тесты – это лишь образцы возможного ответа. Возможны и другие способы генерации паролей.

#
# import random
#
# digits = '23456789'
# lowercase_letters = 'abcdefghijkmnpqrstuvwxyz'
# uppercase_letters = 'ABCDEFGHJKLMNPQRSTUVWXYZ'
#
#
# chars = ''
# n, m = int(input()), int(input())
# chars = digits + lowercase_letters +uppercase_letters
# for i in range(n):
#     password = ""
#     password = random.choice(digits) + random.choice(lowercase_letters) + random.choice(uppercase_letters)
#     for j in range(m - 3):
#          password += random.choice(chars)
#     print(password)

# ________________________________________________________________________
#
#
# import random
# mtr_second =[]
# i = 0
# while i < 5:
#     mtr = []
#     j = 0
#     i+=1
#     while j < 5:
#         if i == 3 and j == 2:
#             mtr.append(0)
#             j += 1
#         else:
#             numbers = random.randint(1, 75)
#             if (numbers in mtr_second[0]) and (numbers in mtr):
#                 continue
#             else:
#                 mtr.append(numbers)
#                 j += 1
#     mtr_second.append(mtr)
# for i in range(5):
#     for j in range(5):
#         print(str(mtr_second[i][j]).ljust(3), end=' ')
#     print()
#
# ___________________________________________
# import random
# a = [[random.randint(1, 75) for _ in range(5)] for _ in range(5)]
# a[2][2] = 0
#
# for i in range(5):
#     for j in range(5):
#         print(str(a[i][j]).ljust(3), end='')
#     print()
#
# # ____________________________________________-
from random import *
numbers = set(sample([i for i in range(1, 76)], 25))
s = [[numbers.pop() for _ in range(5)] for _ in range(5)]
s[2][2] = 0
for row in s:
    print(*(str(k).ljust(3) for k in row))
#
#
# import numpy as np
# from numpy import random
# p=np.random.choice(range(50),size=(5, 5), replace=False)
# p[2,2]=0
# for i in range(5):
#     for j in range(5):
#         print(str(p[i][j]).ljust(3), end=' ')
#     print()