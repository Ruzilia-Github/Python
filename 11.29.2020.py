3.2
1. Даны три целых числа, каждое записано в отдельной строке.

Нужно вывести значение наибольшего из данных чисел

Sample Input:

5
7
21
Sample Output:

21

2. На свой день рождения Петя купил красивый и вкусный торт, который имел идеально круглую форму. Петя не знал, сколько гостей придет на его день рождения, поэтому вынужден был разработать алгоритм, согласно которому он сможет быстро разрезать торт на N равных частей. Следует учесть, что разрезы торта можно производить как по радиусу, так и по диаметру.

Помогите Пете решить эту задачу, определив наименьшее число разрезов торта по заданному числу гостей.

Входные данные

Программа получает на вход натуральное число N – число гостей, включая самого виновника торжества

Выходные данные

Выведите минимально возможное число разрезов торта.

n=int(input())
if n%2==0:
    print(n//2)
else:
    if n==1:
        print(0)
    else:
        print(n)


a=int(input())
b=int(input())
c=int(input())
if a>b:
    if a>c:
        print(a)
    else:
        print(c)
else:
    if b>c:
        print(b)
    else:
        print(c)

3.  В данной задаче необходимо сравнить два целых числа A и B. Они поступают на вход программе отдельно в каждой строке.

Ваша задача вывести символ "<", если A меньше B, ">", если A больше B и "=", если A=B.

Sample Input 1:

5
9
Sample Output 1:

<
Sample Input 2:

2
1
Sample Output 2:

>
Sample Input 3:

7
7

a=int(input())
b=int(input())
if a<b:
    print('<')
else:
    if a>b:
        print('>')
    else:
        print('=')



4. Кнопочные гонки

Двое решили посоревноваться в набирании текстов на сайте «Кнопочные гонки». Во время соревнования необходимо ввести текст из s символов. Первый участник набирает один символ за v1 миллисекунд и имеет пинг t1 миллисекунд. Второй участник набирает один символ за v2 миллисекунд и имеет пинг t2 миллисекунд.

При соединении с пингом (задержкой) в t миллисекунд соревнование проходит для участника следующим образом:

Ровно через t миллисекунд после начала соревнования участник получает текст, который необходимо ввести.
Сразу после этого он начинает вводить этот текст.
Ровно через t миллисекунд после того, как он перепечатал весь текст, сайт получает информацию об этом.
Победителем в соревновании является тот участник, информация об успехе которого пришла раньше. Если информация пришла от обоих участников одновременно, считается, что произошла ничья.

По данной длине текста и информации об участниках, определите исход игры.

Входные данные

Первая строка содержит пять целых чисел s, v1, v2, t1, t2 (1 ≤ s, v1, v2, t1, t2 ≤ 1000) — количество символов в тексте, скорость набора текста первым участником, скорость набора текста вторым участником, пинг первого участника и пинг второго участника.

Выходные данные

Если выиграет первый участник, выведите «First». Если выиграет второй участник, выведите «Second». В случае ничьей выведите «Friendship».

Разбор Youtube Boosty Patreon

Sample Input 1:

5 1 2 1 2
Sample Output 1:

First
Sample Input 2:

3 3 1 1 1
Sample Output 2:

Second
Sample Input 3:

4 5 3 1 5
Sample Output 3:

Friendship

s,v1,v2,t1,t2=map(int,input().split())
time1 = s*v1 + t1*2
time2 = s*v2 + t2*2
if time1>time2:
    print('Second')
elif time1<time2:
    print('First')
else:
    print('Friendship')

 5. При игре в "Города" игроки по очереди называют названия городов так, чтобы первая буква каждого нового слова совпадала с последней буквой предыдущего. При этом считают, что если последняя буква предыдущего слова — мягкий знак, то с первой буквой следующего слова надо сравнивать букву, предшествующую мягкому знаку.

Напишите программу, которая считывает подряд две строки, после чего выводит «Good», если последний символ первой строки совпадает с первым символом второй (с учётом правила про мягкий знак), и «Bad» в противном случае.

Sample Input 1:

Лондон
Норильск
Sample Output 1:

Good
Sample Input 2:

Тверь
Роттердам
Sample Output 2:

Good
Напишите програ

a=input().lower()
b=input().lower()
if a[-1] == b[0]:
    print('Good')
elif a[-1] == 'ь':
    if a[-2] == b[0]:
        print('Good')
    else:
        print('Bad')
else:
    print('Bad')

6. Даны три целых числа, записанных в отдельных строках. Определите, сколько среди них совпадающих.

Программа должна вывести одно из чисел: 3 (если все совпадают), 2 (если два совпадают) или 0 (если все числа различны).


Sample Input 1:

6
6
6
Sample Output 1:

3
Sample Input 2:

7
8
7
Sample Output 2:

2

a=int(input())
b=int(input())
c=int(input())
if a == b and a == c and b == c:
    print('3')
elif a == b  or  a == c or  b == c:
    print('2')
else:
    print('0')

7. Программа определяет наименование месяца по его номеру n.

Программа получает на вход номер месяца - натуральное число N (N<=12) и в зависимости от его значения вывод название месяца

Sample Input 1:

4
Sample Output 1:

Апрель
Sample Input 2:

9
Sample Output 2:

Сентябрь

n=int(input())
if n==1:
    print('Январь')
elif n==2:
    print('Февраль')
elif n==3:
    print('Март')
elif n==4:
    print('Апрель')
elif n==5:
    print('Май')
elif n==6:
    print('Июнь')
elif n==7:
    print('Июль')
elif n==8:
    print('Август')
elif n==9:
    print('Сентябрь')
elif n==10:
    print('Октябрь')
elif n==11:
    print('Ноябрь')
else:
    print('Декабрь')


____________________________
n = int(input())
month = ['Январь', 'Февраль', 'Март', 'Апрель',
         'Май', 'Июнь', 'Июль', 'Август',
         'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
print(month[n-1])
____________________________

user_input = int(input())
months = [0,"Январь", "Февраль",
          "Март", "Апрель", "Май",
          "Июнь", "Июль", "Август",
          "Сентябрь", "Октябрь", "Ноябрь",
          "Декабрь"]

print(months[user_input])


8.  Ваша программа получает на вход возраст человека. Вам необходимо вывести на экран сообщение:

"Младенец", если возраст меньше 2х лет;
"Малыш", если возраст от 2, но меньше 4;
"Ребенок", если возраст от 4 лет, но меньше 12;
"Подросток", когда возраст от 12 лет, но меньше 19;
"Взрослый человек", когда возраст от 19 лет, но меньше 65;
"Пожилой человек", если возраст 65 и более.
Sample Input 1:

4
Sample Output 1:

Ребенок
Sample Input 2:

65
Sample Output 2:

Пожилой человек


a=int(input())
if a<2:
    print("Младенец")
elif a>=2  and a<4:
    print("Малыш")
elif a>=4  and a<12:
    print("Ребенок")
elif a>=12  and a<19:
    print("Подросток")
elif a>=19  and a<65:
    print("Взрослый человек")
elif a>=65:
    print("Пожилой человек")

________________________
age = int(input())
print('Младенец' if age < 2 else 'Малыш' if age < 4 else 'Ребенок' if age < 12 else 'Подросток' if age < 19 else 'Взрослый человек' if age < 65 else 'Пожилой человек')
_______________________
a = int(input())
if a < 2: print('Младенец')
elif a < 4: print('Малыш')
elif a < 12: print('Ребенок')
elif a < 19: print('Подросток')
elif a < 65: print('Взрослый человек')
else: print('Пожилой человек')
