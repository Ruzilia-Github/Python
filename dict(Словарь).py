# Дополните приведенный код, чтобы он вывел имена всех пользователей (в алфавитном порядке), чей номер оканчивается на 88.
#
# Примечание. Имена необходимо вывести на одной строке, разделяя символом пробела.


#
# users = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
#          {'name': 'Helga', 'phone': '555-1618', 'email': 'helga@mail.net'},
#          {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
#          {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
#          {'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan.cha@yandex.ru'},
#          {'name': 'John', 'phone': '233-421-32', 'email': ''},
#          {'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'},
#          {'name': 'Alina', 'phone': '+7948-799-2434', 'email': 'ali.ch.b@gmail.com'},
#          {'name': 'Robert', 'phone': '420-2011', 'email': ''},
#          {'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
#          {'name': 'Khabib', 'phone': '+7995-600-9080', 'email': 'kh.nurmag@gmail.com'},
#          {'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
#          {'name': 'Roman', 'phone': '+7459-145-8059', 'email': 'roma988@mail.ru'},
#          {'name': 'Maria', 'phone': '12-129-3148', 'email': 'm.sharapova@gmail.com'},
#          {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
#          {'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}]
# a = []
# for key in users:
#     if key["phone"][-1] == "8":
#         a.append(key["name"])
# print(*(sorted(a)))
# ______________________________________________________________
#
# print(*sorted([x['name'] for x in users if x['phone'][-1] == '8']))


# Дополните приведенный код, чтобы он вывел имена всех пользователей (в алфавитном порядке), у которых нет информации об электронной почте.
#
# Примечание 1. Ключ email может отсутствовать в словаре.
#
# Примечание 2. Имена необходимо вывести на одной строке, разделяя символом пробела.


# /
# __________________________________________________________________________
# # list=[]
# for i in users:
#     if i.get("email")==None or len(i.get("email")) == 0:
#         list.append(i.get("name"))
#
# print(list)
# _______________________________________________________________
# a = []
# for key in users:
#     try:
#         if len(key['email']) == 0:
#             a.append(key["name"])
#     except:
#         if "email" not in users:
#             a.append(key["name"])
#
# print(*(sorted(a)))
# _______________________________________________________________________________
# Напишите программу, которая будет превращать натуральное число в строку, заменяя все цифры в числе на слова:
#
# 00 на zero;
# 11 на one;
# 22 на two;
# 33 на three;
# 44 на four;
# 55 на five;
# 66 на six;
# 77 на seven;
# 88 на eight;
# 99 на nine.
# Формат входных данных
# На вход программе подается натуральное число.
#
# Формат выходных данных
# Программа должна вывести строковое представление числа.
#
# Примечание. Используйте словарь вместо условного оператора.


# my_dict = {'0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'}
# n= input()
# a = []
# for key in n:
#     a.append(my_dict[key])
# print(*a)
# _______________________________________________________________________
# Напишите программу, которая по номеру курса выводит информацию о данном курсе.
#
# Номер курса (ключ)	Номер аудитории (значение)	Преподаватель (значение)	Время (значение)
# CS101	3004	Хайнс	8:00
# CS102	4501	Альварадо	9:00
# CS103	6755	Рич	10:00
# NT110	1244	Берк	11:00
# CM241	1411	Ли	13:00
# Формат входных данных
# На вход программе подается одна строка – номер курса.
#
# Формат выходных данных
# Программа должна вывести номер курса, затем номер аудитории, имя преподавателя и время проведения курса в соответствии с примерами.
#
# Примечание 1. Используйте словарь вместо условного оператора.
#
# Примечание 2. Для удобного вывода используйте строковый метод format() или f-строки.
#
# Sample Input 1:
#
# CS101
# Sample Output 1:
#
# CS101: 3004, Хайнс, 8:00


# d = {
#     "CS101": "CS101: 3004, Хайнс, 8:00",
#     "CS102": "CS102: 4501, Альварадо, 9:00",
#     "CS103": "CS103: 6755, Рич, 10:00",
#     "NT110": "NT110: 1244, Берк, 11:00",
#     "CM241": "CM241: 1411, Ли, 13:00"
# }
#
#
# print(f"{d[input()]}")
#
# ____________
#
# d = {
#     "CS101": "3004, Хайнс, 8:00",
#     "CS102": "4501, Альварадо, 9:00",
#     "CS103": "6755, Рич, 10:00",
#     "NT110": "1244, Берк, 11:00",
#     "CM241": "1411, Ли, 13:00"
# }
# s = input()
# print(f'{s}: {d[s]}')
# ____________________________________________________________________________
# На мобильных кнопочных телефонах текстовые сообщения можно отправлять с помощью цифровой клавиатуры. Поскольку с каждой клавишей связано несколько букв, для большинства букв требуется несколько нажатий клавиш. При однократном нажатии цифры генерируется первый символ, указанный для этой клавиши. Нажатие цифры 2, 3, 42,3,4 или 55 раз генерирует второй, третий, четвертый или пятый символ клавиши.
#
# 1	.,?!:
# 2	ABC
# 3	DEF
# 4	GHI
# 5	JKL
# 6	MNO
# 7	PQRS
# 8	TUV
# 9	WXYZ
# 0	space (пробел)
# Напишите программу, которая отображает нажатия клавиш, необходимые для введенного сообщения.
#
# Формат входных данных
# На вход программе подается одна строка – текстовое сообщение.
#
# Формат выходных данных
# Программа должна вывести нажатия клавиш, необходимых для введенного сообщения.
#
# Примечание 1. Ваша программа должна обрабатывать как прописные, так и строчные буквы.
#
# Примечание 2. Ваша программа должна игнорировать любые символы, не указанные в приведенной выше таблице.
#
# Примечание 3. Nokia 3310, чтобы вспомнить как это было 😄
#
#
#
# Подсказка
# Создайте словарь, в котором каждая буква или символ сопоставляется с нажатиями клавиш, необходимыми для их создания.
#
# Sample Input 1:
#
# Hello, World!
# Sample Output 1:
#
# 4433555555666110966677755531111
#
# d={".":'1', ",":'11', "?":'111', "!":'1111', ":":'11111',
#     "A":'2', "B":'22', "C":'222',
#     "D":'3', "E":'33', "F":'333',
#     "G":'4', "H":'44', "I":'444',
#     "J":'5', "K":'55', "L":'555',
#     "M":'6', "N":'66', "O":'666',
#     "P":'7', "Q":'77', "R":'777', "S": '7777',
#     "T":'8', "U":'88', "V":'888',
#     "W":'9', "X":'99', "Y":'999', "Z": '9999',
#     " ":'0'
# }
#
# a = ''
# for key in input().upper():
#     try:
#         a += d[key]
#     except:
#         if key not in d:
#             continue
#
# print(a)
#
# ________________________________________________________________________
#
# letters = [c for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789']
# morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '-----', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.']
# d = dict(zip(letters, morse))
# a = ''
# for key in input().upper():
#     try:
#         a += d[key] + " "
#     except:
#         if key not in d:
#             continue
#
# print(a)


#
# Дополните приведенный код, чтобы в переменной result хранился словарь, в котором ключи – числа от 11 до 1515 (включительно), а значения представляют собой квадраты ключей.
#
# Примечание. Выводить содержимое словаря result не нужно.

# n = [i for i in range(1,16)]
# n2 = [i**2 for i in range(1,16)]
# d = dict(zip(n, n2))
# print(d)
# _____________
#
# result = {i: i**2 for i in range(1, 16)}
# print(result)
# ______________
# result = {}
# for i in range(1, 16):
#     result.setdefault(i, i**2)
# ____________________________________________________________________________

# dict1 = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}
# dict2 = {'a': 300, 'b': 200, 'd': 400, 't': 777, 'c': 12, 'p': 123, 'w': 111, 'z': 666}
# # result = dict1 | dict2
# dict1.update(dict2)
# result = dict1
# dict1 = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}
# dict2 = {'a': 300, 'b': 200, 'd': 400, 't': 777, 'c': 12, 'p': 123, 'w': 111, 'z': 666}
# for i in result:
#     try:
#       if i in dict1:
#           result[i] = dict1[i] + dict2[i]
#     except:
#         result[i]=result[i]
# print(result)

# _____________________

# dict1 = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}
# dict2 = {'a': 300, 'b': 200, 'd': 400, 't': 777, 'c': 12, 'p': 123, 'w': 111, 'z': 666}
#
# result = {i: dict1.get(i, 0) + dict2.get(i, 0) for i in set(dict1.keys() | dict2.keys())}

# Дополните приведенный код так, чтобы в переменной result хранился словарь, в котором для каждого символа строки text будет подсчитано количество его вхождений.
#
# Примечание. Выводить содержимое словаря result не нужно.

# text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'
# result = {}
# for num in text:
#     result[num] = result.get(num, 0) + 1
# print(result)

# Дополните приведенный код, чтобы он вывел наиболее часто встречающееся слово строки s. Если таких слов несколько, должно быть выведено то, что меньше в лексикографическом порядке.

import collections
s = 'orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana orange barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon strawberry apricot currant currant gooseberry raspberry apricot currant orange lime quince grapefruit barley banana melon pomegranate barley banana orange barley apricot plum banana quince lime grapefruit strawberry gooseberry apple barley apricot currant orange melon pomegranate banana banana orange apricot barley plum banana grapefruit banana quince currant orange melon pomegranate barley plum banana quince barley lime grapefruit pomegranate barley'

# n = [i for i in s.split()]
# result={}
# for j in n:
#     result[j] = result.get(j, 0)+1
# # print(result)
# # print(max(result.values()))
# a = []
# for z in result:
#     try:
#         if result[z] == max(result.values()):
#             a.append(z)
#     except:
#         continue
# print(a[0])
#
# pets = [('Hatiko', 'Parker', 'Wilson', 50),
#         ('Rusty', 'Josh', 'King', 25),
#         ('Fido', 'John', 'Smith', 28),
#         ('Butch', 'Jake', 'Smirnoff', 18),
#         ('Odi', 'Emma', 'Wright', 18),
#         ('Balto', 'Josh', 'King', 25),
#         ('Barry', 'Josh', 'King', 25),
#         ('Snape', 'Hannah', 'Taylor', 40),
#         ('Horry', 'Martha', 'Robinson', 73),
#         ('Giro', 'Alex', 'Martinez', 65),
#         ('Zooma', 'Simon', 'Nevel', 32),
#         ('Lassie', 'Josh', 'King', 25),
#         ('Chase', 'Martha', 'Robinson', 73),
#         ('Ace', 'Martha', 'Williams', 38),
#         ('Rocky', 'Simon', 'Nevel', 32)]
#
# list = []
# dog_owner = {}
# from pprint import pprint
# for i in pets:
#         name=i[1],i[2], int(i[3])
#         dog=i[0]
#         dog_owner.setdefault(name, []).append(dog)
#
# pprint(dog_owner)
#
# for i in pets:
#         name=i[1],i[2], int(i[3])
#         dog=i[0]
#         dog_owner.setdefault(name, []).append(dog)
# result=dog_owner
# ____________________________________________________________________________________________
# На вход программе подается строка текста. Напишите программу, которая выводит слово, которое встречается реже всего, без учета регистра. Если таких слов несколько, выведите то, которое меньше в лексикографическом порядке.
#
# Формат входных данных
# На вход программе подается строка текста.
#
# Формат выходных данных
# Программа должна вывести слово (в нижнем регистре), встречаемое реже всего.
#
# Примечание 1. Программа не должна быть чувствительной к регистру, слова apple и Apple должна воспринимать как одинаковые.
#
# Примечание 2. Слово — последовательность букв. Кроме слов в тексте могут присутствовать пробелы и знаки препинания .,!?:;-, которые нужно игнорировать. Других символов в тексте нет.
#
# Sample Input 1:
#
# home sweet home
# Sample Output 1:
#
# sweet
#
#
#
# import re
# n = input().lower().split()
# a = []
# for i in n:
#     words = re.sub(r'[.,;:-?-!]', '', i)
#     a.append(words)
# result = {}
# for num in a:
#     result[num] = result.get(num, 0) + 1
# lst = [(value, key) for key, value in result.items()]
# lst.sort()
# print(lst[0][1])

# ______________________
# dct = {}
# lst = [word.strip('.,!?:;-') for word in input().lower().split()]
# for word in lst:
#     dct[word] = dct.get(word, 0) + 1
# lst = [(value, key) for key, value in dct.items()]
# print(lst)
# lst.sort()
# print(lst[0][1])
# _______________________________________________________________________________________________
#
# На вход программе подается строка, содержащая строки-идентификаторы. Напишите программу, которая исправляет их так, чтобы в результирующей строке не было дубликатов. Для этого необходимо прибавлять к повторяющимся идентификаторам постфикс _n, где n – количество раз, сколько такой идентификатор уже встречался.
#
# Формат входных данных
# На вход программе подается строка текста, содержащая строки-идентификаторы, разделенные символом пробела.
#
# Формат выходных данных
# Программа должна вывести исправленную строку, не содержащую дубликатов сохранив при этом исходный порядок.
#
# Sample Input 1:
#
# a b c a a d c
# Sample Output 1:
#
# a b c a_1 a_2 d c_1

a=input().split()
for i in range(len(a)):
    if a[i] not in a[:i]:
        print(a[i],end=' ')
    else:
        print(f"{a[i]}_{a[:i].count(a[i])}", end=' ')
___________________
lst = input().split()
res = {}
for c in lst:
    if c in res:
        print(f'{c}_{res[c]}', end=' ')
    else:
        print(c, end=' ')
    res[c] = res.get(c, 0) + 1







