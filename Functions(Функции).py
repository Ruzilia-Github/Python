# Напишите функцию matrix(), которая создает, заполняет и возвращает матрицу заданного размера. При этом (в зависимости от переданных аргументов) она должна вести себя так:
#
# matrix() — возвращает матрицу 1 \times 11× 1, в которой единственное число равно нулю;
# matrix(n) — возвращает матрицу n \times nn× n, заполненную нулями;
# matrix(n, m) — возвращает матрицу из nn строк и mm столбцов, заполненную нулями;
# matrix(n, m, value) — возвращает матрицу из nn строк и mm столбцов, в которой каждый элемент равен числу value.
# При создании функции пользуйтесь аргументами по умолчанию.
#
# Примечание 1. Приведенный ниже код:
#
# print(matrix())                   # матрица 1 × 1 из 0
# print(matrix(3))                  # матрица 3 × 3 из 0
# print(matrix(2, 5))               # матрица 2 × 5 из 0
# print(matrix(3, 4, 9))            # матрица 3 × 4 из 9
# должен выводить:
#
# [[0]]
# [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
# [[9, 9, 9, 9], [9, 9, 9, 9], [9, 9, 9, 9]]

# def matrix(n=0, m=0, value=0):
#     if n == 0  and m == 0 and value == 0:
#         return [[0]]
#     if n > 0  and m == 0 and value == 0:
#         return [[0 for i in range(n)] for j in range(n)]
#     if n > 0  and m > 0 and value == 0:
#         return [[0 for i in range(m)] for j in range(n)]
#     if n > 0 and m > 0 and value > 0:
#         return [[value for i in range(m)] for j in range(n)]
#
# print(matrix())                   # матрица 1 × 1 из 0
# print(matrix(3))                  # матрица 3 × 3 из 0
# print(matrix(2, 5))               # матрица 2 × 5 из 0
# print(matrix(3, 4, 9))            # матрица 3 × 4 из 9
#
# ______________________________
#
# def matrix(n=1, m=0, value=0):
#     return [[value for _ in range(m if m else n)] for _ in range(n)]
# ____________________________________________________________________________
# Напишите функцию count_args(), которая принимает произвольное количество аргументов и возвращает количество переданных в нее аргументов.
#
# Примечание 1. Обратите внимание, что функция должна принимать не список, а именно произвольное количество аргументов.
#
# Примечание 2. Следующий программный код:
#
# print(count_args())
# print(count_args(10))
# print(count_args('stepik', 'beegeek'))
# print(count_args([], (''), 'a', 12, False))
# должен выводить:
#
# 0
# 1
# 2
# 5

# def count_args(*args):
#    return len(args)
#
# print(count_args())
# print(count_args(10))
# print(count_args('stepik', 'beegeek'))
# print(count_args([], (''), 'a', 12, False))
#
# _____________________________________________________________
# Напишите функцию sq_sum(), которая принимает произвольное количество числовых аргументов и возвращает сумму их квадратов.
#
# Примечание 1. Обратите внимание, что функция должна принимать не список, а именно произвольное количество аргументов.
#
# Примечание 2. Следующий программный код:
#
# print(sq_sum())
# print(sq_sum(2))
# print(sq_sum(1.5, 2.5))
# print(sq_sum(1, 2, 3))
# print(sq_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
# должен выводить:
#
# 0
# 4
# 8.5
# 14
# 385

# def sq_sum(*args):
#     sum = 0
#     for i in args:
#         sum += i**2
#     return sum
# _____________________________________________________________
#
# Напишите функцию mean(), которая принимает произвольное количество аргументов и возвращает среднее арифметическое переданных в нее числовых (int или float) аргументов.
#
# Примечание 1. Обратите внимание, что функция должна принимать не список, а именно произвольное количество аргументов.
#
# Примечание 2. Функция должна игнорировать аргументы всех типов, кроме int или float.
#
# Примечание 3. Следующий программный код:
#
# print(mean())
# print(mean(7))
# print(mean(1.5, True, ['stepik'], 'beegeek', 2.5, (1, 2)))
# print(mean(True, ['stepik'], 'beegeek', (1, 2)))
# print(mean(-1, 2, 3, 10, ('5')))
# print(mean(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
# должен выводить:
#
# 0.0
# 7.0
# 2.0
# 0.0
# 3.5
# 5.5
#
# def mean(*args):
#     sum = 0
#     count = 0
#     for i in args:
#         if type(i) is float or type(i) is int:
#             sum += i
#             count +=1
#         else:
#             continue
#     if count == 0:
#        return 0.0
#     else:
#        return sum / count
#
#
# print(mean())
# print(mean(7))
# print(mean(1.5, True, ['stepik'], 'beegeek', 2.5, (1, 2)))
# print(mean(True, ['stepik'], 'beegeek', (1, 2)))
# print(mean(-1, 2, 3, 10, ('5')))
# print(mean(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
#
# _________________________
#
# def mean(*args):
#     nums = [i for i in args if type(i) in (int, float)]
#     if len(nums) > 0:
#         return sum(nums) / len(nums)
#     else:
#         return 0

# ______________________________________________________________________________
# Напишите функцию greet(), которая принимает произвольное количество аргументов строк имен (как минимум одно) и возвращает приветствие в соответствии с образцом.
#
# Примечание 1. Обратите внимание, что функция должна принимать не список, а именно произвольное количество аргументов.
#
# Примечание 2. Следующий программный код:
#
# print(greet('Timur'))
# print(greet('Timur', 'Roman'))
# print(greet('Timur', 'Roman', 'Ruslan'))
# должен выводить:
#
# Hello, Timur!
# Hello, Timur and Roman!
# Hello, Timur and Roman and Ruslan!
#
# def greet(*args):
#     return f"Hello, {' and '.join(args)}!"
#
# print(greet('Timur'))
# print(greet('Timur', 'Roman'))
# print(greet('Timur', 'Roman', 'Ruslan'))
# __________________________________________________________________________


# Напишите функцию print_products(), которая принимает произвольное количество аргументов и выводит список продуктов (любая непустая строка) по образцу: <номер продукта>) <название продукта> (нумерация продуктов начинается с единицы). Если среди переданных аргументов нет ни одного продукта, необходимо вывести текст Нет продуктов.
#
# Примечание 1. Обратите внимание, что функция должна принимать не список, а именно произвольное количество аргументов.
#
# Примечание 2. Числа, списки, кортежи, словари, множества и другие нестроковые объекты продуктами не являются и их нужно игнорировать.

# def print_products(*args):
#     count = 0
#     for i in args:
#         if i == "":
#             continue
#         if type(i) is str:
#             count += 1
#             #print(f"{count}) {i}")
#         if type(i) is not str:
#             continue
#     if count == 0:
#         pass
#
#
#         # print("Нет продуктов")
# print(print_products('Бананы', [1, 2], ('Stepik',), 'Яблоки', '', 'Макароны', 5, True))
# print(print_products([4], {}, 1, 2, {'Beegeek'}, ''))
# #
#
# # #-----------Birkan---------------
# def Products(*args):
#     """
#     Put here description about your fonction like that
#     """
#     count = 0
#     for i in args:
#         if count == 0:
#             pass
#         if type(i) is str and len(i)!=0:
#             count += 1
#             print(f"{count}) {i}")
#         else:
#             pass
#     if count == 0:
#         print("Нет продуктов")
#     return "heyy"
#
# Products('Бананы', [1, 2], ('Stepik',), 'Яблоки', '', 'Макароны', 5, True)
# Products([4], {}, 1, 2, {'Beegeek'}, '')
#
# _______________________________________________________________________________________________
# Напишите функцию info_kwargs(), которая принимает произвольное количество именованных аргументов и печатает именованные аргументы в соответствии с образцом: <имя аргумента>: <значение аргумента>, при этом имена аргументов следуют в алфавитном порядке (по возрастанию).
#
# Примечание 1. Обратите внимание, что функция должна принимать не список, а именно произвольное количество именованных аргументов.
#
# Примечание 2. Следующий программный код:
#
# info_kwargs(first_name='Timur', last_name='Guev', age=28, job='teacher')
# должен выводить:
#
# age: 28
# first_name: Timur
# job: teacher
# last_name: Guev

#
# def info_kwargs(**kwargs):
#     for key, value in sorted(kwargs.items()):
#         print(f'{key}: {value}')
# info_kwargs(first_name='Timur', last_name='Guev', age=28, job='teacher')
#
# --------------------
# def info_kwargs(**kwargs):
#     for key in sorted(kwargs):
#         print (key+':',kwargs[key])
#
#
# ____________________________________________________________________

# Дан список numbers, содержащий кортежи чисел. Напишите программу, которая с помощью встроенных функций min() и max() выводит те кортежи (каждый на отдельной строке), которые имеют минимальное и максимальное среднее арифметическое значение элементов.

#
#
# def compare_by_second(point):
#     return sum(point)/len(point)
#
#
# def compare_by_sum(point):
#     return sum(point)/len(point)
#
#
# # points = [(1, -1), (2, 3), (-10, 15), (10, 9), (7, 18), (1, 5), (2, -4)]
# points = [(10, 10, 10), (30, 45, 56), (81, 39), (1, 2, 3), (12,), (-2, -4, 100), (1, 2, 99), (89, 9, 34), (10, 20, 30, -2), (50, 40, 50), (34, 78, 65), (-5, 90, -1, -5), (1, 2, 3, 4, 5, 6), (-9, 8, 4), (90, 1, -45, -21)]
#
#
# print(sorted(points, key=compare_by_second)[0])
# print(sorted(points, key=compare_by_sum)[-1])
# ________________________________________
# numbers = [(10, 10, 10), (30, 45, 56), (81, 39), (1, 2, 3), (12,), (-2, -4, 100), (1, 2, 99), (89, 9, 34), (10, 20, 30, -2), (50, 40, 50), (34, 78, 65), (-5, 90, -1, -5), (1, 2, 3, 4, 5, 6), (-9, 8, 4), (90, 1, -45, -21)]
# print(min(numbers, key=lambda a: sum(a) / len(a)))
# print(max(numbers, key=lambda a: sum(a) / len(a)))

# --------------------------------

# numbers = [(10, 10, 10), (30, 45, 56), (81, 39), (1, 2, 3), (12,), (-2, -4, 100), (1, 2, 99), (89, 9, 34), (10, 20, 30, -2), (50, 40, 50), (34, 78, 65), (-5, 90, -1, -5), (1, 2, 3, 4, 5, 6), (-9, 8, 4), (90, 1, -45, -21)]
# def comporant(num):
#     return sum(num) / len(num)
# print(min(numbers, key=comporant))
# print(max(numbers, key=comporant))



# __________________________________________________________________________________
# Напишите программу, которая сортирует список points координат точек плоскости в соответствии с расстоянием от начала координат (точки (0; \, 0)(0;0)). Программа должна вывести отсортированный список.

# numbers = [(-1, 1), (5, 6), (12, 0), (4, 3), (0, 1), (-3, 2), (0, 0), (-1, 3), (2, 0), (3, 0), (-9, 1), (3, 6), (8, 8)]
# def comporant(num):
#     return num[0]**2 + num[1]**2
# print(sorted(numbers, key=comporant))
# __________________________________
# points = [(-1, 1), (5, 6), (12, 0), (4, 3), (0, 1), (-3, 2), (0, 0), (-1, 3), (2, 0), (3, 0), (-9, 1), (3, 6), (8, 8)]
# points.sort(key=lambda a: abs(complex(a[0], a[1])))
# print(points)

# _____________________________
#
# Дан список numbers, содержащий кортежи чисел. Напишите программу, которая сортирует и выводит список numbers в соответствии с суммой минимального и максимального элемента кортежа.
#
# Примечание 1. В этой задаче мы считаем, что кортеж (2, 1, 3)(2,1,3) меньше кортежа (6, 4, 5)(6,4,5), так как 1+3 < 4+61+3<4+6. При этом кортеж (1, 2, 9)(1,2,9) равен кортежу (4, 5, 6)(4,5,6), так как 1+9 = 4+61+9 = 4+6.

# numbers = [(10, 10, 10), (30, 45, 56), (81, 80, 39), (1, 2, 3), (12, 45, 67), (-2, -4, 100), (1, 2, 99), (89, 90, 34), (10, 20, 30), (50, 40, 50), (34, 78, 65), (-5, 90, -1)]
# def comporant(num):
#     return min(num) + max(num)
#
# print(sorted(numbers, key=comporant))
#
# _____________________
#
# numbers = [(10, 10, 10), (30, 45, 56), (81, 80, 39), (1, 2, 3), (12, 45, 67), (-2, -4, 100), (1, 2, 99), (89, 90, 34), (10, 20, 30), (50, 40, 50), (34, 78, 65), (-5, 90, -1)]
# numbers.sort(key=lambda i: min(i) + max(i))
#
#
# print(numbers)
# ___________________________________________________________________________________
# Список athletes содержит сведения о спортсменах в виде кортежей: (имя, возраст, рост, вес).
#
# Напишите программу сортировки списка спортсменов по указанному полю:
#
# 11: по имени;
# 22: по возрасту;
# 33: по росту;
# 44: по весу.
# Формат входных данных
# На вход программе подается натуральное число от 11 до 44 – номер поля по которому требуется отсортировать список.
#
# Формат выходных данных
# Программа должна вывести отсортированный по заданному полю список в соответствии с примерами.
#
# Примечание. Решите задачу без использования условного оператора.
#
# Sample Input 1:
#
# 3
# Sample Output 1:
#
# Рустам 10 128 30
# Дима 10 130 35
# Тимур 11 135 39
# Руслан 9 140 33
# Матвей 17 168 68
# Амир 16 170 70
# Рома 16 188 100
# Петя 15 190 90
# _________________________________________________________________________
#
#
# numbers = [('Дима', 10, 130, 35), ('Тимур', 11, 135, 39), ('Руслан', 9, 140, 33), ('Рустам', 10, 128, 30), ('Амир', 16, 170, 70), ('Рома', 16, 188, 100), ('Матвей', 17, 168, 68), ('Петя', 15, 190, 90)]
#
# def comporant(num):
#     return num[n-1]
#
# n = int(input())
# print(*(sorted(numbers, key=comporant)), sep='\n')
#
# _______________________________________________________________________________
# Напишите программу, которая принимает число и название функции, а выводит результат применения функции к данному числу.
#
# Список возможных функций:
#
# квадрат: функция принимает число и возвращает его квадрат;
# куб: функция принимает число и возвращает его куб;
# корень: функция принимает число и возвращает корень квадратный из этого числа;
# модуль: функция принимает число и возвращает его модуль;
# синус: функция принимает число (в радианах) и возвращает синус этого числа.
# Формат входных данных
# На вход программе подается целое число и название функции, записанные на отдельных строках.
#
# Формат выходных данных
# Программа должна выдать результат применения функции к числу.
#
# Примечание. Решите задачу без использования условного оператора.
#
# Sample Input 1:
#
# 5
# квадрат
#
# from math import sin
#
# def f1():
#     return num ** 2
#
# def f2():
#     return num ** 3
#
# def f3():
#     return num ** 0.5
#
# def f4():
#     return abs(num)
#
# def f5():
#     return sin(num)
#
# commands = {'квадрат': f1, 'куб': f2, 'корень': f3, 'модуль': f4, 'синус': f5 }  # словарь соответствия команда → функция
#
# num = int(input())       # считываем цифру
# command = input()        # считываем название команды
# commands[command]()      # вызываем нужную функцию через словарь по ключу


# from math import sin
#
# def f1():
#     return num ** 2
#
# def f2():
#     return num ** 3
#
# def f3():
#     return num ** 0.5
#
# def f4():
#     return abs(num)
#
# def f5():
#     return sin(num)
#
# commands = {'квадрат': f1, 'куб': f2, 'корень': f3, 'модуль': f4, 'синус': f5 }  # словарь соответствия команда → функция
#
# num = int(input())       # считываем цифру
# command = input()        # считываем название команды
# print(commands[command]())      # вызываем нужную функцию через словарь по

# __________________________________________________________________________
# На вход программе подается строка натуральных чисел. Из элементов строки формируется список чисел.
# #
# # Напишите программу сортировки списка чисел в порядке неубывания суммы их цифр. При этом, если два числа имеют одинаковую сумму цифр, следует сохранить их взаиморасположение в начальном списке.
# #
# # Формат входных данных
# # На вход программе подается строка текста, содержащая натуральные числа, разделенные пробелами.
# #
# # Формат выходных данных
# # Программа должна вывести отсортированный список чисел в соответствии с условием задачи, разделяя его элементы одним пробелом.
# #
# # Подсказка
# # Sample Input 1:
# #
# # 12 14 79 7 4 123 45 90 111
# # Sample Output 1:
# #
# # 12 111 4 14 123 7 45 90 79


# def dig_sum(num):
#   num = str(num)
#   return sum(int(c) for c in num)
#
# nums = [int(c) for c in input().split()]
# nums.sort()
#
# print(*sorted(nums, key=dig_sum))
# ____________________________________

# n = input().split()
# s1 = []
# s2 = []
# for i in n:
#     s1.append(int(i))
#     sum = 0
#     for j in i:
#         sum += int(j)
#     s2.append(sum)
# dic = dict(zip(s1, s2))
# num = []
# for key, value in sorted(dic.items(), key=lambda para: (para[1], para[0])):
#     num.append(key)
# print(*num)
#
# _________________________________________________________________

# На вход программе подается строка натуральных чисел. Из элементов строки формируется список чисел.
#
# Напишите программу сортировки списка чисел в порядке неубывания суммы их цифр. При этом, если у двух чисел одинаковая сумма цифр, их следует вывести в порядке неубывания.
#
# Формат входных данных
# На вход программе подается строка текста, содержащая натуральные числа, разделенные пробелами.
#
# Формат выходных данных
# Программа должна вывести отсортированный список чисел в соответствии с условием задачи, разделяя его элементы одним пробелом.
#
# Подсказка
# Sample Input 1:
#
# 111 14 79 7 4 123 90 45 12 171
# Sample Output 1:
#
# 12 111 4 14 123 7 45 90 171 79
#
# n = input().split()
# n = sorted(n)
# s1 = []
# s2 = []
# for i in n:
#     s1.append(int(i))
#     sum = 0
#     for j in i:
#         sum += int(j)
#     s2.append(sum)
# dic = dict(zip(s1, s2))
# num = []
# for key, value in sorted(dic.items(), key=lambda para: (para[1], para[0])):
#     num.append(key)
# print(*num)

# numbers = [-2, 45, 45, -7, -45, 37, -42, 27, -58, -58, -12, -27, -49, -27, -56, 4, -99, -11, 86]
#
# var1 = max(numbers, key=abs)
# var2 = min(map(abs, numbers))
#
# print(var1 + var2)

#
# numbers = [('Дима', 10, 130, 35), ('Тимур', 11, 135, 39), ('Руслан', 9, 140, 33), ('Рустам', 10, 128, 30), ('Амир', 16, 170, 70), ('Рома', 16, 188, 100), ('Матвей', 17, 168, 68), ('Петя', 15, 190, 90)]
#
# def comporant(num):
#     return num[n-1]
# n = int(input())
# print(*(sorted(numbers, key=comporant)), sep='\n')

# #---------------------------------------------------------------------------------------
# Напишите программу, которая с помощью функции map() округляет все элементы списка numbers до 22 десятичных знаков, а затем выводит их, каждый на отдельной строке.
#
#
# def map(items):
#     result = []
#     for item in items:
#         result.append(round(item, 2))
#     return print (*result, sep = '\n')
#
# numbers = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.12013, 23.22222, 90.09873, 45.45, 314.1528, 2.71828, 1.41546]
#
# map(numbers)
#
# ______________________
#
# def map(function, items):
#     result = []
#     for item in items:
#         result.append(function(item))
#     return result
#
#
# def roun(f):
#     return round(f, 2)
#
#
# numbers = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.12013, 23.22222, 90.09873, 45.45, 314.1528, 2.71828, 1.41546]
# print(*map(roun, numbers), sep='\n')

# ____________________________________________________________________
# Напишите программу, которая с помощью функций filter() и map() отбирает из заданного списка numbers трёхзначные числа, дающие при делении на 55 остаток 22, и выводит их кубы, каждый в отдельной строке.
#
# Примечание. Остаток 2 при делении на 5 должно давать само число, а не его куб.
#
# def map(function, items):
#     result = []
#     for item in items:
#         result.append(function(item))
#     return result
#
#
# def filter(function, items):
#     result = []
#     for item in items:
#         if function(item):
#             result.append(item)
#     return result
#
#
# def len_num(a):
#     return (len(str(a)) == 3)  and (a % 5 == 2)
#
# def rnd(item):
#     return item**3
#
#
# numbers = [1014, 1321, 675, 1215, 56, 1386, 1385, 431, 1058, 486, 1434, 696, 1016, 1084, 424, 1189, 475, 95, 1434, 1462, 815, 776, 657, 1225, 912, 537, 1478, 1176, 544, 488, 668, 944, 207, 266, 1309, 1027, 257, 1374, 1289, 1155, 230, 866, 708, 144, 1434, 1163, 345, 394, 560, 338, 232, 182, 1438, 1127, 928, 1309, 98, 530, 1013, 898, 669, 105, 130, 1363, 947, 72, 1278, 166, 904, 349, 831, 1207, 1496, 370, 725, 926, 175, 959, 1282, 336, 1268, 351, 1439, 186, 273, 1008, 231, 138, 142, 433, 456, 1268, 1018, 1274, 387, 120, 340, 963, 832, 1127]
#
#
# print(*(filter(len_num, numbers)), sep='\n')

#
# numbers = [1014, 1321, 675, 1215, 56, 1386, 1385, 431, 1058, 486, 1434, 696, 1016, 1084, 424, 1189, 475, 95, 1434, 1462, 815, 776, 657, 1225, 912, 537, 1478, 1176, 544, 488, 668, 944, 207, 266, 1309, 1027, 257, 1374, 1289, 1155, 230, 866, 708, 144, 1434, 1163, 345, 394, 560, 338, 232, 182, 1438, 1127, 928, 1309, 98, 530, 1013, 898, 669, 105, 130, 1363, 947, 72, 1278, 166, 904, 349, 831, 1207, 1496, 370, 725, 926, 175, 959, 1282, 336, 1268, 351, 1439, 186, 273, 1008, 231, 138, 142, 433, 456, 1268, 1018, 1274, 387, 120, 340, 963, 832, 1127]
# n = []
# for i in numbers:
#     if len(str(i)) == 3  and  i % 5 == 2:
#        print(i**3)
#
# ______________________________________
#
# def numb(num):
#     return 99 < num < 1000 and num % 5 == 2
#
# def cube(num):
#     return num**3
#
# numbers = [1014, 1321, 675, 1215, 56, 1386, 1385, 431, 1058, 486, 1434, 696, 1016, 1084, 424, 1189, 475, 95, 1434, 1462, 815, 776, 657, 1225, 912, 537, 1478, 1176, 544, 488, 668, 944, 207, 266, 1309, 1027, 257, 1374, 1289, 1155, 230, 866, 708, 144, 1434, 1163, 345, 394, 560, 338, 232, 182, 1438, 1127, 928, 1309, 98, 530, 1013, 898, 669, 105, 130, 1363, 947, 72, 1278, 166, 904, 349, 831, 1207, 1496, 370, 725, 926, 175, 959, 1282, 336, 1268, 351, 1439, 186, 273, 1008, 231, 138, 142, 433, 456, 1268, 1018, 1274, 387, 120, 340, 963, 832, 1127]
#
# print(*map(cube, filter(numb, numbers)), sep = '\n')
#
# ________________________________________________
# def map(function, items):
#     result = []
#     for item in items:
#         result.append(function(item))
#     return result
#
#
# def filter(function, items):
#     result = []
#     for item in items:
#         if function(item):
#             result.append(item)
#     return result
#
#
# def filters2(x):
#     return x in range(100, 1000) and x % 5 == 2
#
#
# def kub(x):
#     return x ** 3
#
#
# numbers = [1014, 1321, 675, 1215, 56, 1386, 1385, 431, 1058, 486, 1434, 696, 1016, 1084, 424, 1189, 475, 95, 1434, 1462,
#            815, 776, 657, 1225, 912, 537, 1478, 1176, 544, 488, 668, 944, 207, 266, 1309, 1027, 257, 1374, 1289, 1155,
#            230, 866, 708, 144, 1434, 1163, 345, 394, 560, 338, 232, 182, 1438, 1127, 928, 1309, 98, 530, 1013, 898, 669,
#            105, 130, 1363, 947, 72, 1278, 166, 904, 349, 831, 1207, 1496, 370, 725, 926, 175, 959, 1282, 336, 1268, 351,
#            1439, 186, 273, 1008, 231, 138, 142, 433, 456, 1268, 1018, 1274, 387, 120, 340, 963, 832, 1127]
#
# print(*map(kub, filter(filters2, numbers)), sep='\n')
# ____________________________________________________________________________
# Напишите программу для вычисления и вывода суммы квадратов элементов списка numbers. Решите задачу двумя способами: с помощью функции reduce(), и с помощью функций map() и sum().

# def reduce(operation, items, initial_value):
#     acc = initial_value
#     for item in items:
#         acc = operation(acc, item)
#     return acc
#
# def add(x, y):
#     return x**2+y**2

# def square(x):
#     sum = 0
#     return sum +=(x**2)
#
# numbers = [97, 42, 9, 32, 3, 45, 31, 77, -1, 11, -2, 75, 5, 51, 34, 28, 46, 1, -8, 84, 16, 51, 90, 56, 65, 90, 23, 35, 11, -10, 70, 90, 90, 12, 96, 58, -8, -4, 91, 76, 94, 60, 72, 43, 4, -6, -5, 51, 58, 60, 30, 38, 67, 62, 36, 72, 34, 82, 62, -1, 60, 82, 87, 81, -7, 57, 26, 36, 17, 43, 80, 40, 75, 94, 91, 64, 38, 72, 29, 84, 38, 35, 7, 54, 31, 95, 78, 27, 82, 1, 64, 94, 31, 29, -8, 98, 24, 61, 7, 73]
#
# s = 0
# for i in numbers:
#     s += i**2
# print(s)
# ___________________________________
# def reduce(operation, items, initial_value):
#     acc = initial_value
#     for item in items:
#         acc = operation(acc, item)
#     return acc
# def add(x, y):
#     return x + y**2
#
# numbers = [97, 42, 9, 32, 3, 45, 31, 77, -1, 11, -2, 75, 5, 51, 34, 28, 46, 1, -8, 84, 16, 51, 90, 56, 65, 90, 23, 35, 11, -10, 70, 90, 90, 12, 96, 58, -8, -4, 91, 76, 94, 60, 72, 43, 4, -6, -5, 51, 58, 60, 30, 38, 67, 62, 36, 72, 34, 82, 62, -1, 60, 82, 87, 81, -7, 57, 26, 36, 17, 43, 80, 40, 75, 94, 91, 64, 38, 72, 29, 84, 38, 35, 7, 54, 31, 95, 78, 27, 82, 1, 64, 94, 31, 29, -8, 98, 24, 61, 7, 73]
#
# print(reduce(add, numbers, 0))
# __________________________________
# def map(function,items):
# 	result = []
# 	for item in items:
# 		new_item = function(item)
# 		result.append(new_item)
# 	return result
# def square(num):
# 	return num**2
# numbers = [97, 42, 9, 32, 3, 45, 31, 77, -1, 11, -2, 75, 5, 51, 34, 28, 46, 1, -8, 84, 16, 51, 90, 56, 65, 90, 23, 35, 11, -10, 70, 90, 90, 12, 96, 58, -8, -4, 91, 76, 94, 60, 72, 43, 4, -6, -5, 51, 58, 60, 30, 38, 67, 62, 36, 72, 34, 82, 62, -1, 60, 82, 87, 81, -7, 57, 26, 36, 17, 43, 80, 40, 75, 94, 91, 64, 38, 72, 29, 84, 38, 35, 7, 54, 31, 95, 78, 27, 82, 1, 64, 94, 31, 29, -8, 98, 24, 61, 7, 73]
# print(sum(map(square, numbers)))

# _________________________________________________________________________
# Напишите программу для вычисления и вывода суммы квадратов двузначных чисел, которые делятся на 77 без остатка.
#
# Примечание 1. При решении задачи используйте функции filter(), map() и sum().
#
# Примечание 2. На 77 должно делиться исходное двузначное число, а не его квадрат.
#
# Примечание 3. Не забывайте про отрицательные двузначные числа.


# def map(function, items):
#     result = []
#     for item in items:
#         result.append(function(item))
#     return result
#
#
# def filter(function, items):
#     result = []
#     for item in items:
#         if function(item):
#             result.append(item)
#     return result
#
#
# def filters2(x):
#     return x in range(10, 100) and x % 7 == 0
#
#
# def add(x, y):
#     return x + y**2
#
# numbers = [77, 293, 28, 242, 213, 285, 71, 286, 144, 276, 61, 298, 280, 214, 156, 227, 228, 51, -4, 202, 58, 99, 270, 219, 94, 253, 53, 235, 9, 158, 49, 183, 166, 205, 183, 266, 180, 6, 279, 200, 208, 231, 178, 201, 260, -35, 152, 115, 79, 284, 181, 92, 286, 98, 271, 259, 258, 196, -8, 43, 2, 128, 143, 43, 297, 229, 60, 254, -9, 5, 187, 220, -8, 111, 285, 5, 263, 187, 192, -9, 268, -9, 23, 71, 135, 7, -161, 65, 135, 29, 148, 242, 33, 35, 211, 5, 161, 46, 159, 23, 169, 23, 172, 184, -7, 228, 129, 274, 73, 197, 272, 54, 278, 26, 280, 13, 171, 2, 79, -2, 183, 10, 236, 276, 4, 29, -10, 41, 269, 94, 279, 129, 39, 92, -63, 263, 219, 57, 18, 236, 291, 234, 10, 250, 0, 64, 172, 216, 30, 15, 229, 205, 123, -105]
#
#
# # print(*map(add, filter(filters2, numbers)), sep='\n')
# numbers = [77, 293, 28, 242, 213, 285, 71, 286, 144, 276, 61, 298, 280, 214, 156, 227, 228, 51, -4, 202, 58, 99, 270, 219, 94, 253, 53, 235, 9, 158, 49, 183, 166, 205, 183, 266, 180, 6, 279, 200, 208, 231, 178, 201, 260, -35, 152, 115, 79, 284, 181, 92, 286, 98, 271, 259, 258, 196, -8, 43, 2, 128, 143, 43, 297, 229, 60, 254, -9, 5, 187, 220, -8, 111, 285, 5, 263, 187, 192, -9, 268, -9, 23, 71, 135, 7, -161, 65, 135, 29, 148, 242, 33, 35, 211, 5, 161, 46, 159, 23, 169, 23, 172, 184, -7, 228, 129, 274, 73, 197, 272, 54, 278, 26, 280, 13, 171, 2, 79, -2, 183, 10, 236, 276, 4, 29, -10, 41, 269, 94, 279, 129, 39, 92, -63, 263, 219, 57, 18, 236, 291, 234, 10, 250, 0, 64, 172, 216, 30, 15, 229, 205, 123, -105]
#
# s = 0
# for i in numbers:
#
#      if i in range(10, 100):
#          if i % 7 == 0:
#              s += (int(i)**2)
#      if i < 0  and len(str(i)) == 3:
#           if i % 7 == 0:
#              s += (int(i)**2)
# print(s)
# ____________________________
# def map(function, items):
#     result = []
#     for item in items:
#         result.append(function(item))
#     return result
#
#
# def filter(function, items):
#     result = []
#     for item in items:
#         if function(item):
#             result.append(item)
#     return result
#
# def is_2(x):
#     return len(str(abs(x))) == 2 and x % 7 == 0
#
# def square_x(x):
#     return x*x
#
# numbers = [77, 293, 28, 242, 213, 285, 71, 286, 144, 276, 61, 298, 280, 214, 156, 227, 228, 51, -4, 202, 58, 99, 270, 219, 94, 253, 53, 235, 9, 158, 49, 183, 166, 205, 183, 266, 180, 6, 279, 200, 208, 231, 178, 201, 260, -35, 152, 115, 79, 284, 181, 92, 286, 98, 271, 259, 258, 196, -8, 43, 2, 128, 143, 43, 297, 229, 60, 254, -9, 5, 187, 220, -8, 111, 285, 5, 263, 187, 192, -9, 268, -9, 23, 71, 135, 7, -161, 65, 135, 29, 148, 242, 33, 35, 211, 5, 161, 46, 159, 23, 169, 23, 172, 184, -7, 228, 129, 274, 73, 197, 272, 54, 278, 26, 280, 13, 171, 2, 79, -2, 183, 10, 236, 276, 4, 29, -10, 41, 269, 94, 279, 129, 39, 92, -63, 263, 219, 57, 18, 236, 291, 234, 10, 250, 0, 64, 172, 216, 30, 15, 229, 205, 123, -105]
#
# print(sum(map(square_x, filter(is_2, numbers))))
# ___________________________________________________________________________________________
# Напишите функцию func_apply(), принимающую на вход функцию и список значений и возвращающую список, в котором каждое значение будет результатом применения переданной функции к переданному списку.
#
# Примечание 1. Приведенный ниже код, при условии, что функция func_apply() написана правильно
#
# def add3(x):
#     return x + 3
#
#
# def mul7(x):
#     return x * 7
#
#
# print(func_apply(mul7, [1, 2, 3, 4, 5, 6]))
# print(func_apply(add3, [1, 2, 3, 4, 5, 6]))
# print(func_apply(str, [1, 2, 3, 4, 5, 6]))
# должен выводить:
#
# [7, 14, 21, 28, 35, 42]
# [4, 5, 6, 7, 8, 9]
# ['1', '2', '3', '4', '5', '6']
# _________________________________________________________________________
#
# Требовалось написать программу, которая:
#
# преобразует список floats в список чисел, возведенных в квадрат и округленных с точностью до одного десятичного знака;
# фильтрует список words  и оставляет только палиндромы длиной более 44 символов;
# находит произведение чисел из списка numbers.
# Программист торопился и написал программу неправильно. Доработайте его программу.
#
# from functools import reduce
#
# floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59, 34.23, 12.12, 4.67, 2.45, 9.32]
# words = ['racecar', 'akinremi', 'deed', 'temidayo', 'omoseun', 'civic', 'TATTARRATTAT', 'malayalam', 'nun']
# numbers = [4, 6, 9, 23, 5]
#
# # Исправьте этот код
# map_result = list(map(lambda num: round(num**2, 1), floats))
# filter_result = list(filter(lambda name: len(name) > 4 and name[:] == name[::-1], words))
# reduce_result = reduce(lambda num1, num2: num1 * num2, numbers)
#
# print(map_result)
# print(filter_result)
# print(reduce_result)
# ____________________________________________________________________________________
# Напишите программу, которая с помощью встроенных функций filter(), map(), sorted() и reduce() выводит в алфавитном порядке список primary городов с населением более 10\,000\, 00010000000 человек, в формате:
#
# Cities: Beijing, Buenos Aires, ...
# Примечание 1. Тестирующая система никак не "покарает" вас за неиспользование встроенных функций filter(), map(), sorted() и reduce(), однако лучше сделать это задание честно 😃.
#
# Примечание 2. Ставить запятую в конце вывода не нужно.

from functools import reduce

data = [['Tokyo', 35676000, 'primary'],
        ['New York', 19354922, 'nan'],
        ['Mexico City', 19028000, 'primary'],
        ['Mumbai', 18978000, 'admin'],
        ['Sao Paulo', 18845000, 'admin'],
        ['Delhi', 15926000, 'admin'],
        ['Shanghai', 14987000, 'admin'],
        ['Kolkata', 14787000, 'admin'],
        ['Los Angeles', 12815475, 'nan'],
        ['Dhaka', 12797394, 'primary'],
        ['Buenos Aires', 12795000, 'primary'],
        ['Karachi', 12130000, 'admin'],
        ['Cairo', 11893000, 'primary'],
        ['Rio de Janeiro', 11748000, 'admin'],
        ['Osaka', 11294000, 'admin'],
        ['Beijing', 11106000, 'primary'],
        ['Manila', 11100000, 'primary'],
        ['Moscow', 10452000, 'primary'],
        ['Istanbul', 10061000, 'admin'],
        ['Paris', 9904000, 'primary']]

city = list(sorted(filter(lambda x: int(x[1]) > 10000000 and x[2] in 'primary', data)))
list_city = [i[0] for i in city]
sentence = reduce(lambda x, y: x + y if x == list_city[0] else x + ", " + y, list_city, 'Cities:')
sentence = sentence.replace(',', '', 1)
print(sentence)
