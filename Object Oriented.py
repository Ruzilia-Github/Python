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
# В этой задаче у нас будет один родительский класс Transport и три дочерних класса (Car, Boat, Plane).
#
# В классе Transport должны быть реализованы:
#
# метод __init__, который создает атрибуты brand, max_speed и kind. Значения атрибутов brand, max_speed, kind поступают при вызове метода __init__. При этом значение kind не является обязательным и по умолчанию имеет значение None;
# метод __str__, который будет возвращать строку формата: "Тип транспорта <kind> марки <brand> может развить скорость <максимальная скорость> км/ч".
# В классе Car должны быть реализованы:
#
# метод __init__, создающий у экземпляра атрибуты brand, max_speed, mileage и приватный атрибут gasoline_residue. Все значения этих атрибутов передаются при вызове класса Car. Внутри инициализации делегируйте создание атрибутов brand, max_speed, kind родительскому классу Transport, при этом атрибуту kind передайте значение "Car";
# свойство-геттер gasoline, который будет возвращать строку: "Осталось бензина на <gasoline_residue> км";
# свойство-сеттер gasoline, которое должно принимать ТОЛЬКО целое число value, увеличивает уровень топлива gasoline_residue на переданное значение и затем вывести фразу 'Объем топлива увеличен на <value> л и составляет <gasoline_residue> л'. Если в значение value подается не целое число, вывести 'Ошибка заправки автомобиля'.
# В классе Boat должны быть реализованы:
#
# метод __init__, создающий у экземпляра атрибуты brand, max_speed, kind, owners_name. Все значения этих атрибутов передаются при вызове класса Boat. Внутри инициализации делегируйте создание атрибутов brand, max_speed, kind родительскому классу Transport, при этом атрибуту kind передайте значение "Boat";
# метод __str__, который будет возвращать строку: 'Этой лодкой марки <brand> владеет <owners_name>'.
# В классе Plane должны быть реализованы:
#
# метод __init__, создающий у экземпляра атрибуты brand, max_speed, capacity. Внутри инициализации делегируйте создание атрибутов brand, max_speed, kind родительскому классу Transport, при этом атрибуту kind передайте значение "Plane";
# метод __str__, который будет возвращать строку: 'Самолет марки <brand> вмещает в себя <capacity> людей'.
#
# class Transport:
#
#     def __init__(self, brand, max_speed, kind=None):
#         self.brand = brand
#         self.max_speed = max_speed
#         self.kind = kind
#
#     def __str__(self):
#         return f"Тип транспорта {self.kind} марки {self.brand} может развить скорость {self.max_speed} км/ч"
#
#
# class Car(Transport):
#
#     def __init__(self, brand, max_speed,  mileage, gasoline_residue):
#         super().__init__(brand, max_speed, kind='Car')
#         self.mileage = mileage
#         self.__gasoline_residue = gasoline_residue
#
#     @property
#     def gasoline(self):
#         return f"Осталось бензина на {self.__gasoline_residue} км"
#
#     @gasoline.setter
#     def gasoline(self, value):
#         if isinstance(value, int):
#             self.__gasoline_residue += value
#             print(f"Объем топлива увеличен на {value} л и составляет {self.__gasoline_residue} л")
#         else:
#             print("Ошибка заправки автомобиля")
#
# class Boat(Transport):
#
#     def __init__(self, brand, max_speed, owners_name):
#         super().__init__(brand, max_speed, kind='Boat')
#         self.owners_name = owners_name
#
#     def __str__(self):
#         return f"Этой лодкой марки {self.brand} владеет {self.owners_name}"
#
#
# class Plane(Transport):
#
#     def __init__(self, brand, max_speed, capacity):
#         super().__init__(brand, max_speed, kind='Plane')
#         self.capacity = capacity
#
#     def __str__(self):
#         return f"Самолет марки {self.brand} вмещает в себя {self.capacity} людей"
#
#
#
# transport = Transport('Telega', 10)
# print(transport)  # Тип транспорта None марки Telega может развить скорость 10 км/ч
# bike = Transport('shkolnik', 20, 'bike')
# print(bike)  # Тип транспорта bike марки shkolnik может развить скорость 20 км/ч
#
# first_plane = Plane('Virgin Atlantic', 700, 450)
# print(first_plane)  # Самолет марки Virgin Atlantic вмещает в себя 450 людей
# first_car = Car('BMW', 230, 75000, 300)
# print(first_car)  # Тип транспорта Car марки BMW может развить скорость 230 км/ч
# print(first_car.gasoline)  # Осталось бензина на 300 км
# first_car.gasoline = 20  # Печатает 'Объем топлива увеличен на 20 л и составляет 320 л'
# print(first_car.gasoline)  # Осталось бензина на 320 км
# second_car = Car('Audi', 230, 70000, 130)
# second_car.gasoline = [None]  # Печатает 'Ошибка заправки автомобиля'
# first_boat = Boat('Yamaha', 40, 'Petr')
# print(first_boat)  # Этой лодкой марки Yamaha владеет Petr

# __________________________
#
# Давайте представим, что в 2020 году в Москве проводили опрос и выявили, к какому классу люди себя относят. По результатам опроса все люди разделились на сладкоежек, вегетарианцев и любителей мяса. Давайте напишем программу, которая поможет нам подвести итоги опроса. Для создания программы нужно:
#
# 1. Создать родительский класс Initialization, который состоит из:
#
#  метода инициализации, в который поступают аргументы: capacity - целое число, food - список из строковых названий еды. Если в значение capacity  передается не целое число, вывести надпись ‘Количество людей должно быть целым числом’ и не создавать для таких экземпляров атрибуты capacity и food.
# 2. Создать дочерний класс Vegetarian от класса Initialization, который состоит из:
#
# метода инициализации, принимающего аргументы capacity, food. Нужно создать одноименные атрибуты через вызов родительского метода __init__.
# метода __str__, который возвращает строку формата "<capacity> людей предпочитают не есть мясо! Они предпочитают <food>"
# 3. Создать дочерний класс MeatEater от класса Initialization, который состоит из:
#
# метода инициализации, принимающего аргументы capacity, food. Нужно создать одноименные атрибуты через вызов родительского метода __init__.
# метода __str__, который возвращает строку формата "<capacity> мясоедов в Москве! Помимо мяса они едят еще и <food>"
# 4. Создать дочерний класс SweetTooth от класса Initialization, который состоит из:
#
# метода инициализации, принимающего аргументы capacity, food. Нужно создать одноименные атрибуты через вызов родительского метода __init__.
# магического метода __str__, который возвращает строку формата ‘Сладкоежек в Москве <capacity>. Их самая любимая еда: <food>’;
# магического  метода __eq__, который будет позволять сравнивать экземпляры класса SweetTooth  с числами и другими нашими классами. Если сравнение происходит с целым числом и атрибут capacity с ним совпадает, то необходимо вернуть True, в противном случае - False. Если же сравнение идет с другим нашим классом(Vegetarian или MeatEater) и значения атрибутов capacity равны, то возвращается True, в противном случае - False. А если же сравнивается с другим типом данных, верните ‘Невозможно сравнить количество сладкоежек с <значение>’;
# магического  метода __lt__. Если сравнение происходит с целым числом и количество сладкоежек (атрибут capacity) меньше, необходимо вернуть True, в противном случае - False. Если сравнение происходит с экземпляром одного из наших классов Vegetarian или MeatEater и сладкоежек меньше, то верните True, в противном случае верните False. В случае если сравнение идет с остальными типами данных, верните ‘Невозможно сравнить количество сладкоежек с <значение>’
# магического  метода __gt__. Если сравнение происходит с целым числом и количество сладкоежек больше, необходимо вернуть значение True, в противном же случае - False. Если сравнение происходит с другим нашим классом Vegetarian или MeatEater и сладкоежек больше, то верните True, в противном случае - False. В случае если сравнение идет с остальными типами данных, верните ‘Невозможно сравнить количество сладкоежек с <значение>’
# class Initialization:
#     def __init__(self, capacity, food):
#         if isinstance(capacity, int):
#             self.capacity = capacity
#             self.food = food
#         return 'Количество людей должно быть целым числом'
#
# class Vegetarian(Initialization):
#      def __init__(self, capacity, food ):
#          super().__init__(capacity, food)
#
#      def __str__(self):
#          return f"{self.capacity} людей предпочитают не есть мясо! Они предпочитают {self.food}"
#
# class MeatEater(Initialization):
#     def __init__(self, capacity, food):
#         super().__init__(capacity, food)
#
#     def __str__(self):
#         return f"{self.capacity} мясоедов в Москве! Помимо мяса они едят еще и {self.food}"
#
# class SweetTooth(Initialization):
#     def __init__(self, capacity, food):
#         super().__init__(capacity, food)
#
#     def __str__(self):
#         return f"Сладкоежек в Москве {self.capacity}. Их самая любимая еда: {self.food}"
#
#     def __eq__(self, other):
#         if isinstance(other, int):
#             return self.capacity == other
#         elif isinstance(other, (Vegetarian, MeatEater)):
#             return self.capacity == other.capacity
#         else:
#             return f"Невозможно сравнить количество сладкоежек с {other}"
#
#     def __lt__(self, other):
#         if isinstance(other, int):
#             return self.capacity < other
#         elif isinstance(other, (Vegetarian, MeatEater)):
#             return self.capacity < other.capacity
#         else:
#             return f"Невозможно сравнить количество сладкоежек с {other}"
#
#     def __gt__(self, other):
#         if isinstance(other, int):
#             return self.capacity > other
#         elif isinstance(other, (Vegetarian, MeatEater)):
#             return self.capacity > other.capacity
#         else:
#             return f"Невозможно сравнить количество сладкоежек с {other}"
#
#
# v_first = Vegetarian(10000, ['Орехи', 'овощи', 'фрукты'])
# print(v_first)  # 10000 людей предпочитают не есть мясо! Они предпочитают ['Орехи', 'овощи', 'фрукты']
# v_second = Vegetarian([23], ['nothing'])  # Количество людей должно быть целым числом
# m_first = MeatEater(15000, ['Жареную картошку', 'рыба'])
# print(m_first)  # 15000 мясоедов в Москве! Помимо мяса они едят еще и ['Жареную картошку', 'рыба']
# s_first = SweetTooth(30000, ['Мороженое', 'Чипсы', 'ШОКОЛАД'])
# print(s_first)  # Сладкоежек в Москве 30000. Их самая любимая еда: ['Мороженое', 'Чипсы', 'ШОКОЛАД']
# print(s_first > v_first)  # True
# print(30000 == s_first)  # True
# print(s_first == 25000)  # False
# print(100000 < s_first)  # False
# print(100 < s_first)  # True

# ________________________
# class Wallet:
#     def __init__(self, currency, balance):
#         try:
#             isinstance(currency, str)
#         except TypeError:
#             print("Неверный тип валюты")
#         try:
#             len(str(currency)) == 3
#         except NameError:
#             print("Неверная длина названия валюты")
#         try:
#             currency == str(currency).upper()
#         except ValueError:
#             print("Название должно состоять только из заглавных букв")
#         else:
#             self.currency = currency
#             self.balance = balance
#
#     def __eq__(self, other):
#         try:
#             other.currrncy == self.currency
#         except ValueError:
#             print("Нельзя сравнить разные валюты")
#         try:
#             isinstance(other, self.balance)
#         except TypeError:
#             print(f"Wallet не поддерживает сравнение с {self.balance}")
#         else:
#             return self.balance == other.balance
#
#
#     def __add__(self, other):
#         try:
#             other.currency == self.currency and isinstance(other.balance, Wallet)
#         except ValueError:
#             print("Данная операция запрещена")
#         else:
#             return self.balance+other.balance
#
#     def __add__(self, other):
#         try:
#             other.currency == self.currency and isinstance(other.balance, Wallet)
#         except ValueError:
#             print("Данная операция запрещена")
#         else:
#             return self.balance * other.balance
# _______________________________________________

# class Wallet:
#     def __init__(self, currency, balance):
#         if not isinstance(currency, str):
#             raise TypeError('Неверный тип валюты')
#         if len(currency) != 3:
#             raise NameError('Неверная длина названия валюты')
#         if not currency.isupper():
#             raise ValueError('Название должно состоять только из заглавных букв')
#         self.currency = currency
#         self.balance = balance
#
#     def __eq__(self, other):
#         if not isinstance(other, Wallet):
#             raise TypeError(f'Wallet не поддерживает сравнение с {other}')
#         if self.currency != other.currency:
#             raise ValueError('Нельзя сравнить разные валюты')
#         return self.balance == other.balance
#
#     def __add__(self, other):
#         if not isinstance(other, Wallet) and self.currency != other.currency:
#             raise ValueError('Данная операция запрещена')
#         return Wallet(self.currency, self.balance + other.balance)
#
#     def __sub__(self, other):
#         if not isinstance(other, Wallet) and self.currency != other.currency:
#             raise ValueError('Данная операция запрещена')
#         return Wallet(self.currency, self.balance - other.balance)
#
# wallet1 = Wallet('USD', 50)
# wallet2 = Wallet('RUB', 100)
# wallet3 = Wallet('RUB', 150)
# # wallet4 = Wallet(12, 150)  # исключение TypeError('Неверный тип валюты')
# wallet5 = Wallet('qwerty', 150)  # исключение NameError('Неверная длина названия валюты')
# wallet6 = Wallet('abc', 150)  # исключение ValueError('Название должно состоять только из заглавных букв')
# print(wallet2 == wallet3)  # False
# print(wallet2 == 100)  # TypeError('Wallet не поддерживает сравнение с 100')
# print(wallet2 == wallet1)  # ValueError('Нельзя сравнить разные валюты')
# wallet7 = wallet2 + wallet3
# print(wallet7.currency, wallet7.balance)  # печатает 'RUB 250'
# wallet2 + 45  # ValueError('Данная операция запрещена')
#

# def  longest_word_in_file(file_name):
#     file = open(file_name,"r", encoding='utf-8')
#     max_words = ""
#     for i in file:
#         words = i.split()
#         for w in words:
#             word_without = remove_punc(w)
#             if len(word_without) >= len(max_words):
#                 max_words = word_without
#     file.close()
#     return word_without
#
# def remove_punc(w):
#     from string import punctuation
#     for p in punctuation:
#         if p in w:
#             w = w.replace(p, '')
#     return w
#
# print(longest_word_in_file("file.txt"))
import random

# _______________________________
# Реализуйте класс MoneyBox, для работы с виртуальной копилкой.
#
# Каждая копилка имеет ограниченную вместимость, которая выражается целым числом – количеством монет, которые можно положить в копилку. Класс должен поддерживать информацию о количестве монет в копилке, предоставлять возможность добавлять монеты в копилку и узнавать, можно ли добавить в копилку ещё какое-то количество монет, не превышая ее вместимость.
#
# Класс должен иметь следующий вид
#
#
# class MoneyBox:
#     def __init__(self, capacity):
#        self.capacity = capacity
#
#     def can_add(self, v):
#         if self.capacity - v >= 0:
#             return True
#             self.v = v
#         else:
#             return False
#
#     def add(self, v):
#         self.capacity = self.capacity - v
#
#
# x = MoneyBox(10)
#
# x.add(5)
#
# x.add(5)
#
# print(x.can_add(1))
#
# _____________________________
# Вам дается последовательность целых чисел и вам нужно ее обработать и вывести на экран сумму первой пятерки чисел из этой последовательности, затем сумму второй пятерки, и т. д.
#
# Но последовательность не дается вам сразу целиком. С течением времени к вам поступают её последовательные части. Например, сначала первые три элемента, потом следующие шесть, потом следующие два и т. д.
#
# Реализуйте класс Buffer, который будет накапливать в себе элементы последовательности и выводить сумму пятерок последовательных элементов по мере их накопления.
#
# Одним из требований к классу является то, что он не должен хранить в себе больше элементов, чем ему действительно необходимо, т. е. он не должен хранить элементы, которые уже вошли в пятерку, для которой была выведена сумма.
#
#
#
# class Buffer:
#     def __init__(self):
#         self.buffer = []
#
#     def add(self, *args):
#         self.aftor = []
#         self.buffer += list(args)
#         repetit = len(self.buffer) // 5
#         number = len(self.buffer) % 5
#         a = 0
#         b = 5
#         for i in range(repetit):
#             self.aftor.append(sum(self.buffer[a:b]))
#             a += b + 1
#             b += a
#         self.buffer = list(self.buffer[-number:])
#         if len(self.buffer) == 5:
#             # self.aftor.append(sum(self.buffer))
#             self.buffer = []
#
#
#     def get_current_part(self):
#         print(*self.aftor, sep="\n")
#         print(self.buffer)
#         return self.buffer
#
#
# buf = Buffer()
# buf.add(1, 2, 3)
# buf.get_current_part() # вернуть [1, 2, 3]
# buf.add(4, 5, 6) # print(15) – вывод суммы первой пятерки элементов
# buf.get_current_part() # вернуть [6]
# buf.add(7, 8, 9, 10) # print(40) – вывод суммы второй пятерки элементов
# buf.get_current_part() # вернуть []
# buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1) # print(5), print(5) – вывод сумм третьей и четвертой пятерки
# buf.get_current_part() # вернуть [1]
#
#
# # buf = Buffer()
# # buf.add(1, 2, 3)
# # pr(buf.get_current_part()) # вернуть [1, 2, 3]
# # buf.add(4, 5, 6) # print(15) – вывод суммы первой пятерки элементов
# # print(buf.get_current_part()) # вернуть [6]
# # buf.add(7, 8, 9, 10) # print(40) – вывод суммы второй пятерки элементов
# # print(buf.get_current_part()) # вернуть []
# # buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1) # print(5), print(5) – вывод сумм третьей и четвертой пятерки
# # print(buf.get_current_part()) # вернуть [1]
# #

# class NonPositiveError:
#     pass
#
# class PositiveList(list):
#     pass
#
#     def append(self, x):
#         try:
#             x > 0
#         except:
#             raise NonPositiveError
#         else:
#             super().append(x)
# ______________________________________
#
# class NonPositiveError:
#     pass
#
# class PositiveList(list):
#     pass
#
#     def append(self, x):
#         try:
#             x > 0
#         except:
#             raise NonPositiveError
#         else:
#             super().append(x)
#
#
# a = PositiveList()
# a.append(1)
# print(a)
# a.append(0)
# print(a)
# a.append(-41)
# print(a)

# _________________________
# Задание 16.9.1
# Создайте класс любых геометрических фигур, где на выход мы получаем характеристики фигуры. Каждый экземпляр должен иметь атрибуты, которые зависят от выбранной фигуры. Например, для прямоугольника это будут аргументы x, y, width и height.
#
# class GeometricFigure():
#     def __init__(self,width, height ):
#         self.x = width
#         self.y = height
#
#     def Parameters(self):
#         return f"width = {self.x} height = {self.y}"
#
# n = GeometricFigure(5, 9)
# print(n.Parameters())
# # _______________________________________
# # Задание 16.9.3
# # В проекте «Дом питомца» скоро появится новая услуга: электронный кошелек. То есть система будет хранить данные о своих клиентах и об их финансовых операциях.
# #
# # Вам нужно написать программу, обрабатывающую данные, и на выходе в консоль получить следующее: Клиент "Иван Петров". Баланс: 50 руб.
#
# class Wallet():
#     def __init__(self, name, surname, balance):
#         self. name = name
#         self.surname = surname
#         self.balance = int(balance)
#
#     def Parameters(self):
#        return f"Клиент {self. name} {self. surname}. Баланс: {self.balance} руб."
#
#     def IncreaseBalance(self, sum):
#         self.balance += int(sum)
#
#     def DecreaseBalance(self, sum):
#         self.balance += int(sum)
#
# n = Wallet("Иван", "Петров", 50)
# print(n.Parameters())
# print(n.IncreaseBalance(100))
# print(n.Parameters())
# # _________________________________________
# # Задание 16.9.4
#
# # Команда проекта «Дом питомца» планирует большой корпоратив для своих волонтеров. Вам необходимо написать программу, которая позволяла бы составлять список нескольких гостей. Решите задачу с помощью метода конструктора и примените один из принципов наследования.
# #
# # При выводе в консоль вы должны получить:  “Иван Петров, г.Москва, статус "Наставник"
#
# class Corporate():
#     def __init__(self, name, city, status):
#         self.name = name
#         self.city = city
#         self.status = status
#
#     def Parameters(self):
#         return f"{self. name}, г.{self.city},статус '{self.status}'"
#
# n = Corporate("Иван Петров","Москва" ,"Наставник")
# print(n.Parameters())









