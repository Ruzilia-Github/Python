4.1
1. Пользователь вводит числа, и пока введённые числа не равны нулю, программа работает, как только происходит иное –завершает работу.

Sample Input:

80
90
0
Sample Output:

a=int(input())
while a!=0:
       a=int(input())


2. Зимний вечер в Бурсе
Возьмём число. Умножим его на его же первую цифру. Результат умножим на первую цифру результата. И так далее. Например, начнём с 8:

8 \to 8*8=64 \\ 64 \to 6*64=384 \\ 384 \to 3*384 =1152 \\ 1152 \to 1*1152 =11528→8∗8=64
64→6∗64=384
384→3∗384=1152
1152→1∗1152=1152


Очевидно, когда первая цифра очередного числа в такой последовательности становится равной 1, числа перестают изменяться. Но это происходит не при всех начальных числах.

Напишем программу, которая будет хотя бы приблизительно определять судьбу введённого числа n.

Начиная с числа n, умножайте имеющееся число на его первую цифру, пока у получившегося числа первая цифра не станет равной 1, либо пока оно не превысит миллиарда. В качестве ответа выведите результат

Решение youtube patreon boosty

Sample Input:

8
Sample Output:

1152

n=int(input())
f=int(str(n)[0])
while f!=1 and n<=10**9:
    n=n*f
    f=int(str(n)[0])
print(n) 
