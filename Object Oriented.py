# Подвиг 4. Используя замыкания функций, объявите внутреннюю функцию, которая заключает строку s (s - строка, параметр внутренней функции) в произвольный тег, содержащийся в переменной tag - параметре внешней функции.
#
# Далее, на вход программы поступают две строки: первая с тегом, вторая с некоторым содержимым. Вторую строку нужно поместить в тег из первой строки с помощью реализованного замыкания. Результат выведите на экран.
#
# P. S. Пример добавления тега h1 к строке "Python": <h1>Python</h1>
#
#
# def counter_add(tag):
#     def counter_in(s):
#         return f'<{tag}>{s}</{tag}>'
#     return counter_in
#
# tag = input()
# s = input()
#
# print(counter_add(tag)(s))
# ______________________________________________
# Подвиг 5. Используя замыкания функций, объявите внутреннюю функцию, которая преобразует строку из списка целых чисел, записанных через пробел, либо в список, либо в кортеж. Тип коллекции определяется параметром tp внешней функции. Если tp = 'list', то используется список, иначе (при другом значении) - кортеж.
#
# Далее, на вход программы поступают две строки: первая - это значение для параметра tp; вторая - список целых чисел, записанных через пробел. С помощью реализованного замыкания преобразовать эти данные в соответствующую коллекцию. Результат вывести на экран командой (lst - ссылка на коллекцию):
#
# print(lst)

# def counter_add(tp):
#     def counter_in(s):
#         if tp == "list":
#             return list(s)
#         else:
#             return tuple(s)
#     return counter_in
#
# tp = input()
# s = list(map(int, input().split()))
# print(counter_add(tp)(s))

# ___________________________
# def func_show (func):
#     def wraper (*args, **kwargs):
#         print(f"Площадь прямоугольника: {s}")
#     return wraper()
#
#
# @func_show
# def get_sq(width, height):
#     s = 0
#     s = width * height
#     return s
#
# n, m  = map(int, input().split())
# res = get_sq(n,m)
# print(res)
# _________________________________
# Подвиг 1. Объявите функцию с именем get_sq, которая вычисляет площадь прямоугольника по двум параметрам: width и height - ширина и высота прямоугольника. И возвращает результат (сама ничего на экран не выводит). То есть, функция имеет сигнатуру:
#
# def get_sq(width, height): ...
#
# Определите декоратор func_show для этой функции, который отображает результат на экране в виде строки (без кавычек):
#
# "Площадь прямоугольника: <значение>"
#
# Вызывать функцию и декоратор не нужно, только объявить. Применять декоратор к функции также не нужно.
#
# Sample Input:
#
# 8 11
#
#
# def func_show(func):
#     def wrapper(*args):
#         func(*args)
#         print(f'Площадь прямоугольника: {func(*args)}')
#
#     return wrapper
#
# def get_sq(width, height):
#     s = width * height
#     return s
#
# # w, h = map(int, input().split())
#
# # get_sq = func_show(get_sq)
# get_sq(8, 11)
# _________________________________________________
#
# Подвиг 3. На вход программы поступает строка из целых чисел, записанных через пробел. Напишите функцию get_list, которая преобразовывает эту строку в список из целых чисел и возвращает его. Определите декоратор для этой функции, который сортирует список чисел по возрастанию. Результат сортировки должен возвращаться при вызове декоратора.
#
# Вызовите декорированную функцию get_list и отобразите полученный отсортированный список lst командой:
#
# print(*lst)
#
# Sample Input:
#
# 8 11 -5 4 3 10
# Sample Output:
#
# -5 3 4 8 10 11
#
# def show_menu(func):
#     def wrapper(*args):
#         func()
#     return wrapper
#
# def get_menu(s):
#     a = []
#     b = 1
#     for i in s.split():
#         a.append(f'{b}. {i}')
#         b +=1
#     print(*a, sep='\n')
#
#
# # n = input()
# # print(get_menu(n))
# # get_sq = func_show(get_sq)
# # get_menu(n)
# get_menu('Главная Добавить Удалить Выйти')
#
# _____________________________________________
# Подвиг 3. На вход программы поступает строка из целых чисел, записанных через пробел. Напишите функцию get_list, которая преобразовывает эту строку в список из целых чисел и возвращает его. Определите декоратор для этой функции, который сортирует список чисел по возрастанию. Результат сортировки должен возвращаться при вызове декоратора.
#
# Вызовите декорированную функцию get_list и отобразите полученный отсортированный список lst командой:
#
# print(*lst)
#
# Sample Input:
#
# 8 11 -5 4 3 10
# Sample Output:
#
# -5 3 4 8 10 11

# def func_show(func):
#     def wrapper(*args):
#         func(*args)
#         print(*func)
#
#     return wrapper
#
# def get_sq(lst):
#     # l = sorted(n, key=None)
#     print(*sorted(n, key=None))
#     return ""
#
# n = list(map(int, input().split()))
# # print(*(sorted(n, key=None)))
# # get_sq = func_show(get_sq)
# print(get_sq(n))

#
# ________________________________________
#
#
# class Money:
#     def __init__(self,  dollars, cents):
#         self.dollars = dollars
#         self.cents = cents
#
#
#     def total_cents(self):
#         self.dollars = dollars
#         self.cents = cents
#
#     def get_dollars(self):
#         return self.dollars
#
#     def set_dollars(self, num):
#         if isinstance(num, int) and num >= 0:
#            self.total_dollars = self.total_dollars + num
#         else:
#             print("Error dollars")
#
#     def get_cents(self):
#         return self.cents
#
#     def set_cents(self, num):
#         if 100 < num > 0:
#            self.total_cents = self.total_cents + num
#         else:
#             print("Error cents")
#
#     def __str__(self,dollars, cents, total_cents ):
#         print(f'Ваше состояние составляет {self.dollars} долларов {self.cents} центов')
#
#
# Bill = Money(101, 99)
# print(Bill)  # Ваше состояние составляет 101 долларов 99 центов
# print(Bill.dollars, Bill.cents)  # 101 99
# Bill.dollars = 666
# print(Bill)  # Ваше состояние составляет 666 долларов 99 центов
# Bill.cents = 12
# print(Bill)  # Ваше состояние составляет 666 долларов 12 центов
# ________________________
#
# class Robot:
#
#      population = 0
#
#      def __init__(self, name):
#          self.name = name
#          Robot.population += 1
#          print(f"Робот {self.name} был создан")
#
#      def destroy (self):
#          Robot.population -= 1
#          print(f"Робот {self.name} был уничтожен")
#
#      def say_hello(self):
#          print(f"Робот {self.name} приветствует тебя, особь человеческого рода")
#
#      @classmethod
#      def how_many(cls):
#          print(f"{cls.population}, вот сколько нас еще осталось")
#
# r2 = Robot("R2-D2") # печатает "Робот R2-D2 был создан"
# r2.say_hello() # печатает "Робот R2-D2 приветствует тебя, особь человеческого рода"
# Robot.how_many() # печатает "1, вот сколько нас еще осталось"
# r2.destroy() # печатает "Робот R2-D2 был уничтожен"
# _________________________________________

# Создайте класс Person, у которого есть:
#
# конструктор __init__, принимающий 3 аргумента: name, surname, gender. Атрибут gender может принимать только 2 значения: "male" и "female", по умолчанию "male". Если в атрибут gender передается любое другое значение, печатать сообщение: "Не знаю, что вы имели ввиду? Пусть это будет мальчик!" и проставить атрибут gender значением "male"
# переопределить метод __str__ следующим образом:
# если объект - мужчина (атрибут gender = "male"), возвращать строку "Гражданин <Фамилия> <Имя>
# если объект - женщина (атрибут gender = "female"), возвращать строку "Гражданка <Фамилия> <Имя>
#
#
#
# class Person:
#     def __init__(self, name, surname, gender = "male" ):
#         self.name = name
#         self.surname = surname
#         if gender == "male" or gender == "female":
#             self.gender = gender
#         else:
#             print("Не знаю, что вы имели ввиду? Пусть это будет мальчик!")
#             self.gender = "male"
#     def __str__(self):
#         if self.gender == "female":
#             return f"Гражданка {self.surname} {self.name}"
#         elif self.gender == "male":
#             return f"Гражданин {self.surname} {self.name}"
#
#
# p1 = Person('Chuck', 'Norris')
# print(p1) # печатает "Гражданин Norris Chuck"
# p2 = Person('Mila', 'Kunis', 'female')
# print(p2) # печатает "Гражданка Kunis Mila"
# p3 = Person('Оби-Ван', 'Кеноби', True)# печатает "Не знаю, что вы имели ввиду? Пусть это будет мальчик!"
# print(p3) # печатает "Гражданин Кеноби Оби-Ван"

# ____________________________
#   Создайте класс Vector, который хранит в себе вектор целых чисел.  У класса Vector есть:
#
# конструктор __init__, принимающий произвольное количество аргументов. Среди всех переданных аргументов необходимо оставить только целые числа и сохранить их в атрибут values в виде списка;
# переопределить метод __str__ так, чтобы экземпляр класса Vector выводился следующим образом:
# "Вектор(<value1>, <value2>, <value3>, ...)", если вектор не пустой. При этом значения должны быть упорядочены по возрастанию (будьте аккуратнее с пробелами, они стоят только после запятых, см. пример ниже);
# "Пустой вектор", если наш вектор не хранит в себе значения


# class Vector:
#     def __init__(self, *args, **kwargs):
#         values = list(''.join([str(i) for i in args if isinstance(i, int)]))
#         self.values = values
#
#     def __str__(self):
#         if self.values != 0:
#             # result = ', '.join(map(str, sorted(self.values)))
#             # return str(f'Вектор({result})')
#             return f'Вектор{(*sorted(self.values),)}'
#         else:
#             return "Пустой вектор"
#
# v1 = Vector(1,2,3)
# print(v1) # печатает "Вектор(1, 2, 3)"
# v2 = Vector()
# print(v2) # печатает "Пустой вектор"
#
#

# __________________________________________
# args = (4,2,3)
# values = list(', '.join([str(i) for i in args if isinstance(i, int)]))
# result = ', '.join(map(str, sorted(values)))
# print(values)
# print(result)


# args = (4,2,3)
# values = sorted([x for x in args if isinstance(x, int)])
# values = sorted(list(''.join([str(i) for i in args if isinstance(i, int)])))
# print(*sorted(values),)
# print(values)

# ______________________________________________

# class Vector:
#     def __init__(self, *args, **kwargs):
#         values = sorted([x for x in args if isinstance(x, int)])
#         self.values = values
#
#     def __str__(self):
#         if self.values != 0:
#             return f'Вектор{(*(self.values),)}'
#         else:
#             return "Пустой вектор"
#
#     def __add__(self, other):
#         if isinstance(other, Vector):
#             new = []
#             if len(self.values) == len(other):
#                 new =[self.values[i] + other[i] for i in range(len(self.values))]
#                 return Vector(*[i for i in new])
#             else:
#                 print('Сложение векторов разной длины недопустимо')
#             if isinstance(other, int):
#                 for i in range(len(self.values)):
#                     new.append(self.values[i] + other)
#                 return Vector(*[i for i in new])
#             if not isinstance(other, (Vector, int)):
#                 print(f'Вектор нельзя сложить с {other}')
#
#
# v1 = Vector(1,2,3)
# print(v1) # печатает "Вектор(1, 2, 3)"
#
# v2 = Vector(3,4,5)
# print(v2) # печатает "Вектор(3, 4, 5)"
# v3 = v1 + v2
# print(v3) # печатает "Вектор(4, 6, 8)"
# v4 = v3 + 5
# _________________________________________
# И так, ваша задача реализовать класс ChessPlayer, который состоит из:
#
# метода инициализации, принимающего аргументы name, surname, rating;
# магического  метода __eq__, который будет позволять сравнивать экземпляры класса ChessPlayer с числами и другими экземплярами этого класса. Если сравнение происходит с целым числом и атрибут rating с ним совпадает, то необходимо вернуть True, в противном случае - False. Если же сравнение идет с другим шахматистом(экземпляром класса ChessPlayer)  и значения атрибутов rating равны, то возвращается True, в противном случае - False. А если же сравнивается с другим типом данных, верните ‘Невозможно выполнить сравнение’;
# магического  метода __gt__. Если сравнение происходит с целым числом и атрибут rating больше его, необходимо вернуть значение True, в противном же случае - False. Если сравнение происходит с другим шахматистом(экземпляром класса ChessPlayer) и атрибут rating у нашего экземпляра больше, то верните True, в противном случае - False. В случае если сравнение идет с остальными типами данных, верните ‘Невозможно выполнить сравнение’
# магического  метода __lt__. Если сравнение происходит с целым числом и атрибут rating меньше его, необходимо вернуть значение True, в противном же случае - False. Если сравнение происходит с другим шахматистом(экземпляром класса ChessPlayer) и атрибут rating у нашего экземпляра меньше, то верните True, в противном случае - False. В случае если сравнение идет с остальными типами данных, верните ‘Невозможно выполнить сравнение’.

# class ChessPlayer:
#     def __init__(self, name, surname, rating):
#         self.name = name
#         self.surname = surname
#         self.rating = rating
#
#     def __eq__(self, other):
#         if isinstance(other, (int, float)):
#             return self.rating == other
#         elif isinstance(other, ChessPlayer):
#             return self.rating == other.rating
#         else:
#             return "Невозможно выполнить сравнение"
#
#     def __gt__(self, other):
#         if isinstance(other, (int, float)):
#             return self.rating > other
#         elif isinstance(other, ChessPlayer):
#             return self.rating > other.rating
#         else:
#             return "Невозможно выполнить сравнение"
#
#     def __lt__(self, other):
#         if isinstance(other, (int, float)):
#             return self.rating < other
#         elif isinstance(other, ChessPlayer):
#             return self.rating < other.rating
#         else:
#             return "Невозможно выполнить сравнение"
#
# class ChessPlayer:
#     def __init__(self, name, surname, rating):
#         self.name = name
#         self.surname = surname
#         self.rating = rating
#
#     def __eq__(self, other):
#         if isinstance(other, (int, float)):
#             return self.rating == other
#         elif isinstance(other, ChessPlayer):
#             return self.rating == other.rating
#         else:
#             return "Невозможно выполнить сравнение"
#
#     def __gt__(self, other):
#         if isinstance(other, (int, float)):
#             return self.rating > other
#         elif isinstance(other, ChessPlayer):
#             return self.rating > other.rating
#         else:
#             return "Невозможно выполнить сравнение"
#
#     def __lt__(self, other):
#         if isinstance(other, (int, float)):
#             return self.rating < other
#         elif isinstance(other, ChessPlayer):
#             return self.rating < other.rating
#         else:
#             return "Невозможно выполнить сравнение"
#
#
# magnus = ChessPlayer('Carlsen', 'Magnus', 2847)
# ian = ChessPlayer('Ian', 'Nepomniachtchi', 2789)
# print(magnus == 4000) # False
# print(ian == 2789) # True
# print(magnus == ian) # False
# print(magnus > ian) # True
# print(magnus < ian) # False
# print(magnus < [1, 2]) # печатает "Невозможно выполнить сравнениe"
#
# _____________________________

# Создайте класс City, у которого есть:
#
# конструктор __init__, принимающий единственный аргумент - название города. Вам необходимо сохранить его в качестве атрибута экземпляра name, причем вам нужно преобразовать переданное имя города таким образом, чтобы первая буква каждого слова была заглавной, а остальные оказались строчными (пример "new york" - > "New York")
# переопределить метод __str__ таким образом, чтобы он возвращал имя города
# переопределить метод __bool__ так, чтобы он возвращал False ,если название города заканчивается на любую гласную букву латинского алфавита (a, e, i, o, u), в противном случае True
# class City:
#     def __init__(self, name):
#         self.name = name.title()
#
#     def __str__(self):
#        return self.name
#
#     def __bool__(self):
#         return self.name[-1] not in 'aeiou'
#
#
# p1 = City('new york')
# print(p1)  # печатает "New York"
# print(bool(p1))  # печатает "True"
# p2 = City('SaN frANCISco')
# print(p2)  # печатает "San Francisco"
# print(p2 == True)  # печатает "False"
#
# ________________________________-

# class Quadrilateral:
#     def __init__(self, *args):
#         if len(args) == 1:
#             self.width = args[0]
#             self.height = args[0]
#         else:
#             self.width = args[0]
#             self.height = args[1]
#
#     def __str__(self):
#         if self.width == self.height:
#            return f'Куб размером {self.width}х{self.height}'
#         else:
#             return f'Прямоугольник размером {self.width}х{self.height}'
#
# q1 = Quadrilateral(10)
# print(q1)  # печатает "Куб размером 10х10"
# print(bool(q1))  # печатает "True"
# q2 = Quadrilateral(3, 5)
# print(q2)  # печатает "Прямоугольник размером 3х5"
# print(q2 == True)  # печатает "False"

# _____________________________________

#
# class Vehicle:
#     def __init__(self):
#         pass
#
# class Car(Vehicle):
#     def __init__(self):
#         pass
#
# class RaceCar(Car):
#        pass
#
# class Plane(Vehicle):
#     def __init__(self):
#         pass
#
# class Boat(Vehicle):
#     def __init__(self):
#         pass
#
#
# print(RaceCar.mro())

# _____________________________
# Создайте класс NewInt, который унаследован от целого типа int, то есть мы будем унаследовать поведение целых чисел и значит экземплярам нашего класса будут поддерживать те же операции, что и целые числа.
#
# Дополнительно в классе NewInt нужно создать:
#
# метод repeat, который принимает одно целое положительное число n (по умолчанию равное 2), обозначающее сколько раз нужно продублировать данное число. Метод repeat должен возвращать новое число, продублированное n раз (см пример ниже);
# метод to_bin, который возвращает двоичное представление числа в виде числа (может пригодиться функция bin)

# class Newlnt(int):
#
#     def repeat(self, n = 2):
#         return int(str(self)*n)
#
#     def to_bin(self):
#         return int(bin(self)[2:])
#
#
# p = Newlnt(54)
# print(p.repeat(5))

# _________________________________

class Transport:

class Car(Transport):


class Boat(Transport):
class Transport: