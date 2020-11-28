2.6
1.
Программа
запрашивает
у
пользователя
курс
доллара - вещественное
число, и
также
количество
долларов(целое
число), которое
пользователь
хочет
приобрести.В
итоге
программа
должна
вывести
следующее
сообщение:

"Current dollar rate is <курс доллара>. You want buy <количество долларов> dollars
You
must
pay < стоимость > "

Sample
Input:

56.77
11
Sample
Output:

Current
dollar
rate is 56.77.You
want
buy
11
dollars
You
must
pay
624.47

r = float(input())
c = int(input())
z = r * c
print(f'Current dollar rate is {r}. You want bye {c} dollars\nYou must pay {z}')

2.
77
лет
Напишите
программу, которая
запрашивает
имя
пользователя
и
его
год
рождения.Программа
должна
вывести
на
экран
сообщение
"<Имя пользователя>, вам исполнится 77 лет в <год>"

Разбор
Youtube
Patreon
Boosty

Sample
Input
1:

Геннадий
1990
Sample
Output
1:

Геннадий, вам
исполнится
77
лет
в
2067
Sample
Input
2:

Rich
2010
Sample
Output
2:

Rich, вам
исполнится
77
лет
в
2087

name = input()
year_of_birth = int(input())
print(f'{name}, вам исполнится 77 лет в {year_of_birth + 77}')

3.
Программа
получает
на
вход
список
из
целых
чисел.Ваша
задача
вывести
True
в
случае, если
в
данном
списке
встречается
значение
777.
В
противном
случае
вывести
False

Sample
Input
1:

8
11
Sample
Output
1:

False
Sample
Input
2:

7
8
9
777
56
777
Sample
Output
2:

True

a = input().split()
print("777" in a)
