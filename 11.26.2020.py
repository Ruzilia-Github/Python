# 2.4
#  1.Создайте этот прекрасный рисунок
#
# Старайтесь для переноса строк использовать экранированный символ "\n"
#
# Sample Input:
#
# Sample Output:
#
# /\_/\
# >^,^<
#  / \
# (|_|)_/
#
#
# print( '/\_/\ \n>^,^< \n / \   \n(|_|)_/')
#

# print(r"/\_/\ ", r">^,^< ", r" / \  ", r"(|_|)_/", sep="\n")
#
#
# 2.  2.4 Экранированные (служебные символы) в Python
# 3 из 3 шагов пройдено
# 2 из 2 баллов  получено
# Смог нарисовать котика, сможешь и песика!)))
#
# Sample Input:
#
# Sample Output:
#
#   /~~~\
#  //^ ^\\
# (/(_*_)\)
# _/''*''\_
# (/_)^(_\)
#
#
# print("  /~~~\\ \n //^ ^\\\ \n(/(_*_)\\) \n_/''*''\\_ \n(/_)^(_\\) ")
#
# 3. Напишите программу, которая считывает слово, затем выводит:
#
# «Что Вы сказали? [это слово] ? Какое интересное слово».
#
# Sample Input 1:
#
# Конвульсия
# Sample Output 1:
#
# Что Вы сказали? Конвульсия? Какое интересное слово
# Sample Input 2:
#
# выхухоль
# Sample Output 2:
#
# Что Вы сказали? выхухоль? Какое интересное слово
#
# a=input()
# print("""Что Вы сказали? {0}? Какое интересное слово""".format(a))

Программа запрашивает у пользователя имя и фамилию, после чего выводит приветственное сообщение в следующем формате "Здравствуйте, <фамилия> <имя>!"

Sample Input 1:

Петя
Иванов
Sample Output 1:

Здравствуйте, Иванов Петя!
Sample Input 2:

Никита
Рассказов
Sample Output 2:

Здравствуйте, Рассказов Никита!

Программа запрашивает у пользователя имя и фамилию, после чего выводит приветственное сообщение в следующем формате "Здравствуйте, <фамилия> <имя>!"

Sample Input 1:

Петя
Иванов
Sample Output 1:

Здравствуйте, Иванов Петя!
Sample Input 2:

Никита
Рассказов
Sample Output 2:

Здравствуйте, Рассказов Никита!

a=input()
b=input()
print(""" Здрайвствуйте, {1} {0}!""".format())

""""
This is a Pycharm auto send test 12
"""