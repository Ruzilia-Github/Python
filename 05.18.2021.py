# 1. 5.6 Вложенные списки
# Вам нужно посчитать сумму элементов двумерного квадратного (NxN) списка, которые расположены на главной диагонали.
#
# Под главной диагональю матрицы подразумевается диагональ, проведённая из левого верхнего угла в правый нижний.
#
# Программа сперва принимает на вход число N (N<=15) - количество строк и столбцов в списке, а затем в N строках записаны элементы списка.
#
# Sample Input 1:
#
# 2
# 1 2
# 3 4
# Sample Output 1:
#
# 5
#
# a = []
# n = int(input())
# for i in range (n):
#     a.append(list(map(int.input().split())))
#     s=0
#     for i in range(len(a)):
#         for j in range(len(a)):
#             if i==j:
#                 s +=a[i][j]
# print(s)


# 2. 5.6 Вложенные списки
# Обход элементов матрицы - 1
# Задана целочисленная квадратная матрица размером N x N. Необходимо обойти элементы этой матрицы сверху вниз слева направо и вывести элементы именно в таком порядке в виде таблицы.
#
# Программа принимает на вход натуральное число N – количество строк и столбцов матрицы. В каждой из последующих N строк записаны N целых чисел – элементы матрицы. Все числа во входных данных не превышают 100 по абсолютной величине.
#
# Sample Input 1:
#
# 5
# 3 4 9 1 2
# 8 2 0 5 1
# 4 7 4 8 7
# 7 1 3 3 8
# 5 6 3 7 0
# Sample Output 1:
#
# 3 8 4 7 5
# 4 2 7 1 6
# 9 0 4 3 3
# 1 5 8 3 7
# 2 1 7 8 0


# a = []
# n = int(input())
# for i in range(n):
#     a.append(list(map(int, input().  split())))
# for i in range(len(a)):
#     for j in range(len(a)):
#             print (a [j][i], end = " ")
#     print()
#
#  3  5.6 Вложенные списки
# Обход элементов матрицы - 2
# Задана целочисленная квадратная матрица размером N x N. Необходимо обойти элементы этой матрицы снизу вверх справо налево и вывести элементы именно в таком порядке в виде таблицы.
#
# Программа принимает на вход натуральное число N – количество строк и столбцов матрицы. В каждой из последующих N строк записаны N целых чисел – элементы матрицы.
# Sample Input 1:
#
# 5
# 3 4 9 6 2
# 8 2 0 5 1
# 4 7 4 8 7
# 7 1 3 3 8
# 5 6 3 7 0
# Sample Output 1:
#
# 0 8 7 1 2
# 7 3 8 5 6
# 3 3 4 0 9
# 6 1 7 2 4
# 5 7 4 8 3


# a = []
# n=int(input("NUMBER:\n"))
# for i in range(n):
#     a.append(list(map(int, input().split())))
# for row in range(n-1,-1,-1):
#     for line in range(n-1,-1,-1):
#
#         print(a[row][line], end=' ')
#     print()
#
#
# 4. 5.6 Вложенные списки
#
# Обход элементов матрицы - 3
# Задана целочисленная матрица, состоящая из N строк и M столбцов. Необходимо обойти элементы этой матрицы cправо налево сверху вниз и вывести элементы именно в таком порядке в виде таблицы.
#
# Программа принимает на вход два натуральных числа N и M – количество строк и столбцов матрицы. В каждой из последующих N строк записаны M целых чисел – элементы матрицы.
# Sample Input 1:
#
# 3 4
# 5 9 2 6
# 6 2 4 3
# 1 2 8 7
# Sample Output 1:
#
# 6 2 9 5
# 3 4 2 6
# 7 8 2 1

# a=[]
# n,m = map(int, input('number:\n').split())
# for i in range(n):
#     a.append(list(map(int, input().split())))
# for line in range(n):
#     for row in range (m-1,-1,-1):
#         print(a[line][row], end=' ')
#     print()
#
# 5. 5.6 Вложенные списки
# Обход элементов матрицы - 4
# Задана целочисленная матрица, состоящая из N строк и M столбцов. Необходимо обойти элементы этой матрицы слева направо снизу вверх и вывести элементы именно в таком порядке в виде таблицы.
#
# Программа принимает на вход два натуральных числа N и M – количество строк и столбцов матрицы. В каждой из последующих N строк записаны M целых чисел – элементы матрицы.
#
# Sample Input 1:
#
# 3 4
# 5 9 2 6
# 6 2 4 3
# 1 2 8 7
# Sample Output 1:
#
# 1 2 8 7
# 6 2 4 3
# 5 9 2 6
#
# a=[]
# n,m=map(int, input('number:\n').split())
# for i in range (n):
#     a.append(list(map(int, input().split())))
# for line in range (n-1,-1,-1):
#      for row in range (0,m):
#         print( a[line][row], end=' ')
#      print()
#
# 6. 5.6 Вложенные списки
#
# A. Красивая матрица
#
# Перед Вами матрица размера 5 × 5, состоящая из 24-x нулей и единственной единицы. Строки матрицы пронумеруем числами от 1 до 5 сверху вниз, столбцы матрицы пронумеруем числами от 1 до 5 слева направо. За один ход разрешается применить к матрице одно из двух следующих преобразований:
#
# Поменять местами две соседние строки матрицы, то есть строки с номерами i и i + 1 для некоторого целого i (1 ≤ i < 5).
# Поменять местами два соседних столбца матрицы, то есть столбцы с номерами j и j + 1 для некоторого целого j (1 ≤ j < 5).
# Вы считаете, что матрица будет выглядеть красиво, если единственная единица этой матрицы будет находиться в ее центре (в клетке, которая находится на пересечении третьей строки и третьего столбца). Посчитайте, какое минимальное количество ходов потребуется, чтобы сделать матрицу красивой.
#
# Входные данные
#
# Входные данные состоят из пяти строк, в каждой из которых записаны пять целых чисел: j-ое число в i-ой строке входных данных обозначает элемент матрицы, стоящий на пересечении i-ой строки и j-ого столбца. Гарантируется, что матрица состоит из 24-x нулей и единственной единицы.
#
# Выходные данные
#
# Выведите единственное целое число — минимальное количество действий, которое требуется, чтобы сделать матрицу красивой.
#
# Решение задачи Youtube Patreon Boosty
#
# Sample Input 1:
#
# 0 0 1 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# Sample Output 1:
#
# 2

# m=[]
# for i in range(5):
#     m.append(list(map(int, input().split())))
# for i in range(5):
#     for j in range(5):
#          if m[i][j]==1:
#             row = i
#             column = j
# print(abs(2-row)+(abs(2-column)))

# 7. 5.6 Вложенные списки
# Сумма строк и столбцов двумерного массива
# Сумма строк и столбцов двумерного массива
# Задан целочисленный двумерный массив, состоящий из N строк и M столбцов. Требуется вычислить сумму элементов в каждой строке и в каждом столбце.
#
# Программа получает на вход два натуральных числа N и M – количество строк и столбцов двумерного массива. В каждой из последующих N строк записаны M целых чисел – элементы массива. Все числа во входных данных не превышают 1000 по абсолютной величине.
#
# В первой строке вам необходимо вывести N чисел – суммы элементов массива для каждой строки в отдельности.
#
# Во второй строке в аналогичном формате выведите M чисел – суммы элементов для каждого столбца.
#
# Sample Input 1:
#
# 3 4
# 5 9 2 6
# 6 2 4 3
# 1 2 8 7
# Sample Output 1:
#
# 22 15 18
# 12 13 14 16

# a=[]
# n,m = map(int, input().split())
# for i in range (n):
#       a.append(list(map(int,input().split())))
# for i in range (n):
#     print(sum (a[i]), end=' ')
# print()
# for i in range (m):
#     p=0
#     for j in range(n):
#         p+=a[j][i]
#     print(p, end=' ')

# 8 5.6 Вложенные списки
# Симметричная ли матрица?
#
# Проверьте, является ли двумерный массив симметричным относительно главной диагонали. Главная диагональ — та, которая идёт из левого верхнего угла двумерного массива в правый нижний.
#
# Входные данные
#
# Программа получает на вход число n<100, являющееся числом строк и столбцов в массиве. Далее во входном потоке идет n строк по n чисел, являющихся элементами массива.
#
# Выходные данные
#
# Программа должна выводить слово Yes для симметричного массива и слово No для несимметричного.
#
# Решение задачи Youtube Patreon Boosty
#
# Sample Input 1:
#
# 3
# 0 1 2
# 1 5 3
# 2 3 4
# Sample Output 1:
#
# Yes

# a=[]
# n=int(input())
# for i in range(n):
#     a.append(list(map(int, input().split())))
# count=0
# for i in range(n):
#     for j in range(n):
#         if a[i][j] != a[j][i]:
#             count +=1
# if count>0:
#     print("No")
# # else:
# #     print("Yes")
# 9 5.6 Вложенные списки
# Состязания
#
# В метании молота состязается n спортcменов. Каждый из них сделал m бросков. Победителем считается тот спортсмен, у которого сумма результатов по всем броскам максимальна.
# Если перенумеровать спортсменов числами от 0 до n-1, а попытки каждого из них – от 0 до m-1, то на вход программа получает массив A[n][m], состоящий из неотрицательных целых чисел. Программа должна определить максимальную сумму чисел в одной строке и вывести на экран эту сумму и номер строки, для которой достигается эта сумма.
#
# Входные данные
#
# Программа получает на вход два числа n и m, являющиеся числом строк и столбцов в массиве. Далее во входном потоке идет n строк по m чисел, являющихся элементами массива.
#
# Выходные данные
#
# Программа должна вывести  2 числа: сумму и номер строки, для которой эта сумма достигается. Если таких строк несколько, то выводится номер наименьшей из них. Не забудьте, что нумерация строк (спортсменов) начинается с 0.
#
# Sample Input:
#
# 2 2
# 5 4
# 3 5
# Sample Output:
#
# 9
# 0
#
#
# Условие
# задачи, чтобы
# было
# понятнее:
#
# Sample
# Input:
# 2
# 2
# 5
# 4
# 3
# 5
# n, m = map(int, input().split())  # n = кол-во спортсменов, m = кол-во бросков
#
# те
#
# 2
# 2 = 2
# спортсмена, 2
# броска,
#
# далее
# 5
# 4
# и
# 3
# 5
# уже
# идут
# в
# матрицу
# бросков
#
# 5
# 4
#
# 3
# 5
#
# mas = []  # матрица для номеров спортсменов и кол-ва их бросков
# for i in range(n):  # матрица состоит из n спортсменов, ввод данных
#     mas.append(list(map(int, input().split())))  # вводим строку
#
# n, m = map(int, input().split()) # n = кол-во спортсменов, m =  кол-во бросков
# # Победитель тот у кого максимальная сумма по всем броскам
#
# mas = [] # матрица для номеров спортсменов и кол-ва их бросков
# for i in range(n): # матрица состоит из n спортсменов, ввод данных
#      mas.append(list(map(int, input().split()))) # вводим строку
#
# mas2 = [] # матрица с номером спортсмена и суммой бросков
# count = 0
# for i in range(n):
#     a = sum(mas[i]), count
#     count +=1
#     mas2.append(list(map(int, a)))
#
# for i in max(mas2): # вывод на печать строки с максимальной суммой бросков
#     print(i)

# 10.
# 5.6 Вложенные списки
#
# Состязания - 2
#
# В метании молота состязается n спортcменов. Каждый из них сделал m бросков. Победителем соревнований объявляется тот спортсмен, у которого максимален наилучший результат по всем броскам. Таким образом, программа должна найти значение максимального элемента в данном массиве, а также его индексы (то есть номер спортсмена и номер попытки).
#
# Входные данные
#
# Программа получает на вход два числа n и m, являющиеся числом строк и столбцов в массиве. Далее во входном потоке идет n строк по m чисел, являющихся элементами массива.
#
# Выходные данные
#
# Программа выводит значение максимального элемента, затем номер строки и номер столбца, в котором он встречается. Если в массиве несколько максимальных элементов, то нужно вывести минимальный номер строки, в которой встречается такой элемент, а если в этой строке таких элементов несколько, то нужно вывести минимальный номер столбца. Не забудьте, что все строки и столбцы нумеруются с 0.
# Sample Input:
#
# 3 3
# 3 1 2
# 1 3 4
# 3 3 3
# Sample Output:
#
# 4
# 1 2
#
# n,m = map(int,input().split())
# a=[list(map(int, input().split())) for i in range(n)]
# maximum=0
# max_i=0
# max_j=0
# for i in range (n):
#     for j in range (n):
#         if a [i][j] > maximum:
#             maximum=a[i][j]
#             max_i = i
#             max_j = j
# print(maximum)
# print(max_i, max_j)
#
# 11 5.6 Вложенные списки
#
# Состязания - 3
#
# В метании молота состязается n спортcменов. Каждый из них сделал m бросков. Побеждает спортсмен, у которого максимален наилучший бросок. Если таких несколько, то из них побеждает тот, у которого наилучшая сумма результатов по всем попыткам. Если и таких несколько, победителем считается спортсмен с минимальным номером. Определите номер победителя соревнований.
#
# Входные данные
#
# Программа получает на вход два числа n и m, являющиеся числом строк и столбцов в массиве. Далее во входном потоке идет n строк по m чисел, являющихся элементами массива.
#
# Выходные данные
#
# Программа должна вывести одно число - номер победителя соревнований. Не забудьте, что  строки  (спортсмены) нумеруются с 0.
#
#
#
# Sample Input:
#
# 3 3
# 1 2 7
# 1 3 5
# 4 1 6
# Sample Output:
#
# 0

# n,m=map(int, input().split())
# a=[list(map(int, input().split())) for i in range(n)]
# max_score = 0
# max_summa = 0
# max_index = 0
# for i in range(n):
#     max_try = 0
#     s=0
#     for j in range(m):
#         s +=a[i][j]
#         if a[i][j] > max_try:
#             max_try=a[i][j]
#     if max_try>max_score:
#        max_score = max_try
#        max_summa = s
#        max_index = i
#     elif max_try == max_score and s > max_summa:
#         max_score = max_try
#         max_summa = s
#         max_index = i
# print(max_score, max_summa, max_index)
#
#
# 12 5.6 Вложенные списки
#
#
# В метании молота состязается n спортcменов. Каждый из них сделал m бросков. Победитель определяется по лучшему результату. Определите количество участников состязаний, которые разделили первое место, то есть определите количество строк в массиве, которые содержат значение, равное наибольшему.
#
# Входные данные
#
# Программа получает на вход два числа n и m, являющиеся числом строк и столбцов в массиве. Далее во входном потоке идет n строк по m чисел, являющихся элементами массива.
#
# Выходные данные
#
# Программа должна вывести  одно число - количество победителей соревнования.
#
#
#
# Sample Input 1:
#
# 3 3
# 3 1 2
# 1 3 4
# 4 3 3
# Sample Output 1:
#
# 2
#
# n,m = map(int, input().split())
# a=[]
# for i in range(n):
#     a.append(list(map(int, input().split())))
#     maximum=0
#     count=0
# for i in range(n):
#     local_maximum=0
#     for j in range(m):
#         if a [i][j]>local_maximum:
#             local_maximum=a[i][j]
#     if local_maximum>maximum:
#         maximum=local_maximum
#         count=1
#     elif local_maximum == maximum:
#          count +=1
# print(count)
#
# 5.6 Вложенные списки
# 12 из 16 шагов пройдено
# 60 из 87 баллов  получено
# Симпатичный узор
#
# На днях Иван у себя в прихожей выложил кафель, состоящий из квадратных черных и белых плиток. Прихожая Ивана имеет квадратную форму 4х4, вмещающую 16 плиток. Теперь Иван переживает, что узор из плиток, который у него получился, может быть не симпатичным. С точки зрения дизайна симпатичным узором считается тот, который не содержит в себе квадрата 2х2, состоящего из плиток одного цвета.
#
# Примеры возможных узоров:
#
# Симпатичный узор
#
# По заданному расположению плиток в прихожей Ивана требуется определить: является ли выполненный узор симпатичным.
#
# Программе поступает на вход 4 строки по 4 символа «W» или «B» в каждой, описывающие узор из плиток. Символ «W» обозначает плитку белого цвета, а «B» - черного.
#
# Ваша задача вывести «Yes», если узор является симпатичным и «No» в противном случае.
#
# Sample Input 1:
#
# BWBW
# BBWB
# WWBB
# BWWW
# Sample Output 1:
#
# Yes
# Sample Input 2:
#
# BBWB
# BBWB
# WWBW
# BBWB
# Sample Output 2:
#
# No

# lst=[]
# count=1
# for i in range(4):
#     lst.append(input())
# for i in range(4):
#     for j in range(4)
#        if  lst[i][j] == lst[i+1][j] == lst [i][j+1] == lst [i+1][j+1]:
#        count +=1
# if count>0:
# print('No')
# elif count==0:
# print('Yes')
#
# 5.6 Вложенные списки

#
# Миша уже научился хорошо фотографировать и недавно увлекся программированием. Первая программа, которую он написал, позволяет формировать негатив бинарного черно-белого изображения.
#
# Бинарное черно-белое изображение – это прямоугольник, состоящий из пикселей, каждый из которых может быть либо черным, либо белым. Негатив такого изображения получается путем замены каждого черного пикселя на белый, а каждого белого пикселя – на черный.
#
# Миша, как начинающий программист, написал свою программу с ошибкой, поэтому в результате ее исполнения мог получаться некорректный негатив. Для того чтобы оценить уровень несоответствия получаемого негатива исходному изображению, Миша начал тестировать свою программу.
#
# В качестве входных данных он использовал исходные изображения. Сформированные программой негативы он начал тщательно анализировать, каждый раз определяя число пикселей негатива, которые получены с ошибкой.
#
# Требуется написать программу, которая в качестве входных данных использует исходное бинарное черно-белое изображение и полученный Мишиной программой негатив, и на основе этого определяет количество пикселей, в которых допущена ошибка.
#
# Программа сперва считывает числа n и m (1 ≤ n, m ≤ 100) – высоту и ширину исходного изображения (в пикселях). Последующие n строк содержат описание исходного изображения. Каждая строка состоит из m символов «B» и «W». Символ «B» соответствует черному пикселю, а символ «W» – белому. Далее следует пустая строка, а после нее – описание выведенного Мишиной программой изображения в том же формате, что и исходное изображение.
#
# Необходимо вывести на экран число пикселей негатива, которые неправильно сформированы Мишиной программой.
#

#
# Sample Input 1:
#
# 3 4
# WBBW
# BBBB
# WBBW
#
# BWWW
# WWWB
# BWWB
# Sample Output 1:
#
# 2
# Sample Input 2:
#
# 2 2
# BW
# BB
#
# WW
# BW
# Sample Output 2:
#
# 2
#
# n,m = map(int, input().split())
# start=[]
# for i in  range (n):
#     start.append(input())
# input()
# finish=[]
# for i in range (n):
#     finish.append(input())
# count=0
# for i in range(n):
#     for j in range(m):
#         if start[i][j]==finish[i][j]:
#             count +=1
# print(count)
#
#
# 13 5.6 Вложенные списки
# 13 из 16 шагов пройдено
# 67 из 87 баллов  получено
# Поздравляем! Вы набрали достаточно баллов для получения сертификата. Сертификат появится в вашем профиле в течение суток.
# A. Таблица умножения
#
# Рассмотрим таблицу из n строк и n столбцов. Известно, что в клетке, образованной пересечением i-й строки и j-го столбца, записано число i × j. Строки и столбцы нумеруются с единицы.
#
# Дано целое положительное число x. Требуется посчитать количество клеток таблицы, в которых находится число x.
#
# Входные данные
#
# В единственной строке находятся числа n и x (1 ≤ n ≤ 105, 1 ≤ x ≤ 109) — размер таблицы и число, которое мы ищем в таблице.
#
# Выходные данные
#
# Выведите единственное число: количество раз, которое число x встречается в таблице.
#
# Решение задачи Youtube Patreon Boosty
#
# Sample Input 1:
#
# 10 5
# Sample Output 1:
#
# 2
# Sample Input 2:
#
# 6 12
# Sample Output 2:
#
# 4
# Sample Input 3:
#
# 5 13
# Sample Output 3:
#
# 0

n, x = map(int, input().split())
count=0
i=1
while i*i<=x:
    if x%i==0 and i<=n and  x//i <=n:
        if i!=x//i:
            count +=2
        else:
            count +=1
    i +=1
print(count)