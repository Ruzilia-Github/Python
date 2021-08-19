# Напишите программу, которая рисует прямоугольник.
# Примечание. Программу нужно оформить в виде функции rectangle(width, height), где width, height – ширина и высота прямоугольника.

# import turtle
#
# def rectangle(width, height):
#     for i in range(2):
#         turtle.forward(width)
#         turtle.left(90)
#         turtle.forward(height)
#         turtle.left(90)
#
# w = int(input('Введити ширину = '))
# h = int(input('Введити высоту = '))
#
# rectangle(w, h)

#
# ____________________________________________________________________
# Примечание 1. Программу нужно оформить в виде функции triangle(side), где side – длина стороны треугольника в пикселях.

# import turtle
# def triangle(side):
#
#     for i in range(3):
#         turtle.forward(side)
#         turtle.left(120)
#
#
# n = int(input('Введите длину стороны = '))
#
# triangle(n)


# Напишите программу, которая рисует изображенную фигуру, состоящую из трех квадратов.
#
# import turtle
#
#
# def square(side):
#     """
#     Рисует три квадрата, side: сторона квадрата
#     """
#     direction = 20  # начальное угловое направление
#     for _ in range(3):
#         turtle.setheading(direction)
#         for _ in range(4):
#             turtle.forward(side)
#             turtle.left(90)
#
#         direction += 20
#
# square(300)
#
# ____________________________________________________________________
# Напишите программу, которая рисует изображенную фигуру из восьми квадратов.
#
# def square(side, angle=45):
#     import turtle
#
#     while turtle.heading() != 180:
#         for _ in range(4):
#             turtle.forward(side)
#             turtle.left(90)
#         turtle.left(angle)
#     while turtle.heading() != 0:
#         for _ in range(4):
#             turtle.forward(side)
#             turtle.left(90)
#         turtle.left(angle)
#
#
# n = int(input('Введити длину стороны = '))
#
# square(n)
# ______________________________
#
# import turtle
# def square(side):
#     """
#     Рисует 8 квадратов
#     """
#     direction = 0  # начальное угловое направление
#     for _ in range(8):
#         turtle.setheading(direction)
#
#         for _ in range(4):
#             turtle.forward(side)
#             turtle.left(90)
#
#         direction += 45
#
# square(200)
# ____________________________________________________________
# Напишите программу, которая рисует правильный шестиугольник.

# import turtle
# def hexagon(side):
#     """
#     Рисует 6 угольник
#     """
#     for _ in range(7):
#
#         direction =0  # начальное угловое направление
#         for _ in range(6):
#              turtle.setheading(direction)
#              turtle.forward(side)
#              direction += 60
#
#
# hexagon(200)
#
# _____________________________________________________________________
# Напишите программу, которая рисует ромб с углами 6060 и 120120 градусов.
#
# import turtle
#
# import turtle as t
#
# def rhomb(side):
#     t.forward(side)
#     t.left(60)
#     t.forward(side)
#     t.left(120)
#     t.forward(side)
#     t.left(60)
#     t.forward(side)
#
#
# rhomb(200)
#
#
# import turtle as t
# from random import choice
#
#
# def rhomb(side):
#     colors = ['green', 'red', 'blue', 'orange', 'black', 'cyan', 'purple', 'magenta', 'yellow', 'brown']
#     t.color(choice(colors))
#     for i in [60, 120] * 2:
#         t.backward(side)
#         t.left(i)
#
# def snowflake(side, count = 10):
#     for _ in range(count):
#         rhomb(side)
#         t.right(360 / count)
#
# t.pensize(2)
# # rhomb(150)
# snowflake(50) # вторым параметром можно передать количество
# t.done()
#
# _______________
# import turtle
#
#
# def r(side):
#     for _ in range(2):
#         for _ in range(5):
#             turtle.forward(side)
#             turtle.left(60)
#             turtle.forward(side)
#             turtle.left(120)
#             turtle.forward(side)
#             turtle.left(60)
#             turtle.forward(side)
#             turtle.left(120)
#             turtle.right(72)
#         turtle.left(36)
#
#
# s = int(input())
# r(s)
# ________________________________________________________________________

# Напишите программу, которая рисует лучи звезды, показанной на рисунке.

# import turtle
#
# def sneg(size):
#     for i in ['red', 'yellow', 'green', 'orange', 'blue', 'purple'] * 2:
#         turtle.color(i)
#         turtle.forward(size)
#         turtle.left(180)
#         turtle.forward(size)
#         turtle.left(30)
#
#
# sneg(200)
# __________________________________________________________________________
# Напишите программу, которая рисует правильную пятиконечную звезду.

# import turtle as t
#
# t.ht()
# t.color("yellow")
# def paint(side=100):
#     t.begin_fill()
#     for _ in range(5):
#         t.fd(side)
#         t.right(144)
#     t.color("red")
#     t.end_fill()
# paint()
#
# __________________________________________________________________________
# import turtle as t
#
# colors = ['red', 'blue', 'white', 'green', 'orange', 'black', 'cyan', 'purple', 'magenta', 'yellow', 'brown']
#
# t.pu()
# t.fd(100)
# t.right(90)
# t.fd(100)
# t.left(90)
# t.pd()
# for i in range(1, 21):
#     q = i-1
#     while q >= len(colors):
#         q -= len(colors)
#     t.color(colors[q])
#     t.begin_fill()
#     for _ in range(4):
#         t.left(90)
#         t.fd(220 - i*10)
#     t.end_fill()
#
# _____________________________________________________________________________
# Напишите программу, которая рисует пунктирную линию
# import turtle
#
# turtle.shape('turtle')
# turtle.pensize(15)
# stamp_dot = [turtle.stamp, turtle.dot]
#
#
# def line(num):
#     for _ in range(num):
#         for i in range(2):
#             stamp_dot[i]()
#             turtle.penup()
#             turtle.forward(30)
#             turtle.pendown()
#
#
# line(8)
# ____________________________________________________________________________
# import turtle, random
#
# # Перемещение пера к левому верхнему углу
# turtle.Screen().setup(1000, 1000)
# turtle.penup()
# turtle.right(180)
# turtle.forward(350)
# turtle.right(90)
# turtle.forward(400)
# turtle.right(90)
# turtle.pendown()
# # ---------------------------------------
# Напишите программу, которая рисует узор в соответствии с образцом.
# side = 250  # Начальная длина
# step_side = side * (4 / 100)        # 4%
# pensize = side * (15 / 100)         # 15%
# step_pensize = pensize * (3 / 100)  # 3%
#
# while (side > 0):
#   turtle.pencolor(random.randint(0, 255),
#                   random.randint(0, 255),
#                   random.randint(0, 255))
#   turtle.pensize(pensize)
#   turtle.forward(side)
#   turtle.right(60)
#   pensize -= step_pensize
#   side -= step_sid
# _________________________________________________
# Напишите программу, которая рисует звезду, показанную на рисунке. Такую звезду можно создать из двух треугольников. Однако их невозможно нарисовать непрерывной линией, поэтому перо нужно будет поднять для перехода ко второму треугольнику.

# import turtle
#
#
# def star_of_david(length):
#     """draws the star of David"""
#     turtle.speed(15)
#     turtle.goto(-(length / 2), 0)
#     for _ in range(3):
#         turtle.forward(length)
#         turtle.left(120)
#
#     turtle.penup()
#     turtle.goto(-(length / 2), length / 3 * 1.7)
#     turtle.pendown()
#
#     for _ in range(3):
#         turtle.forward(length)
#         turtle.right(120)
#
#
# star_of_david
# ______________________________________________________________________________________-
# Напишите программу, которая рисует изображение в соответствии с образцом.
# import turtle
# turtle.pencolor('green')
# for i in range(-90, 91, 20):
#   turtle.goto(i, -100)
#   turtle.pencolor('blue')
#   turtle.dot()
#   turtle.pencolor('green')
#   turtle.goto(0, 0)
# turtle.pencolor('red')
# turtle.dot()
#
# _________________________________________________________________________________________
# Напишите программу, которая рисует изображение символа олимпиады в соответствии с образцом.
# import turtle
#
# r = 50
# pensize = 12
# turtle.Screen().setup(600, 1000)
# turtle.pensize(pensize)
#
# points = {1: {"pos": (0, 0), "color": "cyan"},
#           3: {"pos": (r * 2, 0), "color": "black"},
#           4: {"pos": (r * 4, 0), "color": "red"},
#           5: {"pos": (r, -r), "color": "yellow"},
#           2: {"pos": (r * 3, -r), "color": "chartreuse"}}
#
# for i in range(1, 6):
#     turtle.penup()
#     turtle.pencolor(points[i]["color"])
#     turtle.goto(points[i]["pos"])
#     turtle.pendown()
#     turtle.circle(r - pensize / 2)
#
# _____________________________________________________________________________________________
# Напишите программу, которая рисует изображение мишки в соответствии с образцом.
#
# mport
# turtle
#
# size = int(input())  # Размер головы (радиус большого круга)
# pensize = size * 0.1  # Размер пера
# turtle.Screen().setup(600, 1000)
# turtle.hideturtle()
# turtle.pensize(pensize)
# turtle.speed(0)
#
# parts = {1: {"pos": (0, 0), "size": size,  # Голова
#              "circle": True, "color": "brown"},
#          2: {"pos": (0, 0), "size": size * 0.6,  # Нос
#              "circle": True, "color": "orange"},
#          3: {"pos": (0, size * 0.3), "size": size * 0.3,  # Ноздри
#              "circle": False, "color": "gray"},
#          4: {"pos": (0, size * 0.6), "size": size * 0.1,  # Кончик
#              "circle": True, "color": "yellow"},  # носа
#          5: {"pos": (size * -0.5, size * 1.2), "size": size * 0.1,  # Левый
#              "circle": True, "color": "black"},  # глаз
#          6: {"pos": (size * 0.5, size * 1.2), "size": size * 0.1,  # Правый
#              "circle": True, "color": "black"},  # глаз
#          7: {"pos": (size * -0.85, size * 1.8), "size": size * 0.3,  # Левое
#              "circle": True, "color": "red"},  # ухо
#          8: {"pos": (size * 0.85, size * 1.8), "size": size * 0.3,  # Правое
#              "circle": True, "color": "red"}}  # ухо
#
#
# def bear(pos, size, circle, color):
#     turtle.penup()
#     turtle.goto(pos)
#     turtle.pencolor(color)
#     turtle.pendown()
#     if circle:
#         turtle.setheading(0)
#         ycor = pos[1]
#         while (size > 0):
#             turtle.circle(size)
#             size -= pensize - 1
#             ycor += pensize - 1
#             turtle.goto(pos[0], ycor)
#     else:
#         turtle.setheading(90)
#         turtle.forward(size)
#
#
# for i in range(1, 9):
#     bear(parts[i]["pos"], parts[i]["size"], parts[i]["circle"], parts[i]["color"])
#
# ______________
# import turtle as t
# t.speed(0)
# r = 100
# t.penup()
# t.goto(0, -r)
# t.pendown()
# t.circle(r)
# t.circle(r/2)
# t.penup()
# t.goto(0, -r + r*0.2)
# t.pendown()
# t.goto(0, -r + r*0.7)
# t.circle(r/12)
# t.pensize(r*0.1)
# t.penup()
# t.goto(-r/2, 0)
# t.pendown()
# #t.circle(r/12)
# t.dot()
# t.penup()
# t.goto(r/2, 0)
# t.pendown()
# t.dot()
# t.pensize(1)
# t.penup()
# t.goto(-r + r*0.2, r - r*0.3)
# t.pendown()
# t.circle(r/4)
# t.penup()
# t.goto(r - r*0.2, r - r*0.3)
# t.pendown()
# t.circle(r/4)
# ____________________________________________________________
# Напишите программу, которая случайным образом рисует снежинки разного цвета и размера в соответствии с образцом.
import turtle, random

# Глобальные переменные ------------------------------------------------------------
SCREEN_SIZE = 400  # Размер квадратного холста
ACCESS_X = set(range(-SCREEN_SIZE // 2, SCREEN_SIZE // 2 + 1))  # Доступные точки
ACCESS_Y = set(range(-SCREEN_SIZE // 2, SCREEN_SIZE // 2 + 1))  # по "x" и "y"
# ----------------------------------------------------------------------------------

# Общие настройки черепашки --------------------------------------------------------
turtle.Screen().setup(SCREEN_SIZE, SCREEN_SIZE)  # Размер холста
turtle.Screen().bgcolor("cyan")  # Цвет холста
turtle.pencolor("blue")  # Цвет пера
turtle.speed(0)  # Скорость анимации черепашки
turtle.hideturtle()  # Видимость черепашки выключена


# ----------------------------------------------------------------------------------

# Функция для рисования случайной снежинки -----------------------------------------
# def star():
#     global ACCESS_X, ACCESS_Y
#
#     max_size = 0.4  # Макс. значение интервала для выбора размера снежинки
#     while (max_size >= 0.2):
#         size = random.uniform(SCREEN_SIZE * 0.02, SCREEN_SIZE * max_size)
#         x0 = random.choice(tuple(ACCESS_X))  # Выбор коор. "x" из доступных точек
#         y0 = random.choice(tuple(ACCESS_Y))  # Выбор коор. "y" из доступных точек
#         xcors = set(range(int(x0 - size / 2), int(x0 + size / 2)))  # Множества занятых
#         ycors = set(range(int(y0 - size / 2), int(y0 + size / 2)))  # точек "x" и "y"
#
#         # Если область свободна, приступаем к рисованию
#         if (len(xcors - ACCESS_X) == 0 and len(ycors - ACCESS_Y) == 0):
#             turtle.penup()
#             turtle.goto(x0, y0)  # Центр снежинки с выбранными выше координатами
#             turtle.pendown()
#
#             quarter = size / 2 / 4  # Четвертая часть луча снежинки
#             for _ in range(8):  # Цикл для рисования восьми лучей
#                 for _ in range(4):  # Цикл для рисования четырех веточек на данном луче
#                     turtle.left(30)
#                     turtle.forward(quarter)
#                     turtle.backward(quarter)
#                     turtle.right(60)
#                     turtle.forward(quarter)
#                     turtle.backward(quarter)
#                     turtle.left(30)
#                     turtle.forward(quarter)
#                 turtle.backward(size / 2)
#                 turtle.left(45)
#
#             ACCESS_X -= xcors  # Занятые снежинкой точки
#             ACCESS_Y -= ycors  # убираем из доступных
#             print(len(ACCESS_X), len(ACCESS_Y))  # Кол-во доступных точек
#             break
#         else:  # Если область занята, то уменьшаем макс. значение
#             max_size -= 0.1  # интервала для выбора размера снежинки
#
#
# # ----------------------------------------------------------------------------------
#
# # Вызов функции до тех пор, пока есть доступные точки ------------------------------
# while (len(ACCESS_X) > SCREEN_SIZE * 0.2 and
#        len(ACCESS_Y) > SCREEN_SIZE * 0.2):
#     star()
# # ----------------------------------------------------------------------------------
#
# print("DONE!")

# {{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{_________________________}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}
# import turtle, random
# turtle.Screen().bgcolor('cyan')
# turtle.speed(0)
#
# spos = [i for i in range(-180, 180)]
# scolors = ['blue', 'darkblue', 'darkgrey', 'violet', 'darkviolet']
#
# def sflake(ray):
#   turtle.penup()
#   turtle.goto(random.sample(spos, 2))
#   turtle.pendown()
#   turtle.color(random.choice(scolors))
#   for _ in range(8):
#     turtle.forward(ray)
#     for _ in range(3):
#       turtle.backward(ray / 4)
#       turtle.left(45)
#       turtle.forward(ray / 4)
#       turtle.backward(ray / 4)
#       turtle.right(90)
#       turtle.forward(ray / 4)
#       turtle.backward(ray / 4)
#       turtle.left(45)
#     turtle.backward(ray / 4)
#     turtle.left(45)
#
# for i in range(10):
#   sflake(random.randint(15, 50))
#
# turtle.hideturtle()
# ___________________________________________________________________________
# Напишите программу, которая рисует изображение домика по образцу.
# import turtle
# turtle.Screen().setup(300, 400)
# turtle.speed(10)
#
# turtle.hideturtle()
# turtle.fillcolor('beige')
# turtle.begin_fill()
# turtle.goto(100, 0)
# turtle.goto(100, 100)
# turtle.goto(0, 100)
# turtle.goto(0, 0)
# turtle.end_fill()
#
# turtle.penup()
# turtle.goto(-20, 100)
# turtle.pendown()
# turtle.fillcolor('brown')
# turtle.begin_fill()
# turtle.goto(50, 180)
# turtle.goto(120, 100)
# turtle.goto(-20, 100)
# turtle.end_fill()
# ___________________________________________________________________________
# Напишите программу, которая рисует изображение светофора по образцу.
# import turtle
#
# colors = ["red", "yellow", "green"]
# turtle.speed(0)
#
# turtle.goto(-30.0, -120.0)
# turtle.fillcolor("black")
# turtle.begin_fill()
# for _ in range(2):
#     turtle.forward(60)
#     turtle.left(90)
#     turtle.forward(180)
#     turtle.left(90)
# turtle.end_fill()
#
# x, y = 0, 0
#
# for col in colors:
#     turtle.penup()
#     turtle.goto(x, y)
#     turtle.pendown()
#     turtle.fillcolor(col)
#     turtle.begin_fill()
#     turtle.circle(20)
#     turtle.end_fill()
#     y -= 50
#
# turtle.goto(x - 30, y + 30)
# print(turtle.pos())
# ___________________________________________________
# Напишите программу, которая рисует оптическую иллюзию по образцу.
#
# import turtle as t
# t.Screen().setup(350, 400)
# t.speed(0)
# t.hideturtle()
#
# def triangle(side):
#   for _ in range(3):
#     t.forward(side)
#     t.left(120)
#
# s = 150
# k = ((s / 3 * 2) ** 2 - (s / 3) ** 2) ** 0.5
# y3 = ((s / 2) * (s / 6)) ** 0.5
# x0 = [0, s, s / 2]
# y0 = [k, k, -y3]
#
# triangle(s)
#
# for i in range(3):
#   t.penup()
#   t.goto(x0[i%3], y0[i%3])
#   t.pendown()
#   t.pensize(25)
#   t.dot()
#
# t.penup()
# t.goto(0, k)
# t.right(60)
# t.color('white')
# t.begin_fill()
# triangle(s)
# t.end_fill()
# ________________________________________________________________________
# Напишите программу, которая рисует изображение радуги по образцу.
# import turtle
#
#
# def rainbow_circle(radius):
#     """draws rainbow circle of custom size"""
#
#     colors = ("#FF0000", "#FFA600", "#FFFF00", "#62FF00", "#89F590", "#69C5FF",
#               "#1E56FC", "#4800FF", "#CC00FF", "#FF5099")
#     turtle.hideturtle()
#
#     for i in range(10):
#         turtle.dot(radius - (radius / 10) * i, colors[i])
#
#
# rainbow_circle(300)
# _________________________________________________________________________
#
# import turtle as t
#
# begin, end, color = t.begin_fill, t.end_fill, t.fillcolor
# t.up()
# t.Screen().bgcolor('blue')
# for i in [('yellow', 0), ('blue', 50)]:
#   t.goto(i[-1], -130)
#   color(i[0])
#   begin()
#   t.circle(130)
#   end()

# _____________________________________________________________________________
# Напишите программу, которая рисует анимированное изображение фаз луны по образцу.
# import turtle
# turtle.Screen().bgcolor('blue')
# moon = turtle.Turtle()
# moon.hideturtle()
# moon.pencolor('orange')
# moon.dot(200)
# shadow = {0: turtle.Turtle(), 5: turtle.Turtle()}
# for i in [0, 5]:
#   shadow[i].hideturtle()
#   shadow[i].pencolor('blue')
#   shadow[i].penup()
# while 1:
#   for i in range(200, -201, -5):
#     shadow[i % 10].goto(i, 0)
#     shadow[i % 10].dot(200)
#     shadow[(i + 5) % 10].clear()
#
# ___________________________________________________________________________
# Напишите программу, которая рисует изображение по образцу. Звезды должны быть рассыпаны случайно, иметь разный размер и цвет.
# import turtle, random
#
# turtle.speed(0)
# turtle.Screen().bgcolor('black')
# turtle.up()
# def star(size, x, y):
#   turtle.goto(x, y)
#   turtle.left(random.randint(0, 360))
#   for _ in range(5):
#     turtle.forward(size)
#     turtle.right(144)
#
# def play():
#   for i in range(random.randint(50, 200)):
#     side = random.randint(5, 20)
#     x, y = (random.randint(-150, 150) for _ in '12')
#     color = tuple(random.randint(0, 255) for _ in '123')
#     turtle.fillcolor(color)
#     turtle.begin_fill()
#     star(side, x, y)
#     turtle.end_fill()
#
# play()
#
# ________________________________________________________________________________
# import turtle as t
# import math as m
# import random as r
#
#
# def figure(n, square):
#     size = (square * 4 * m.tan(m.radians(180 / n)) / n) ** 0.5
#     color = tuple((r.randint(0, 255) for _ in range(3)))
#     t.fillcolor(color)
#     t.begin_fill()
#
#     t.forward(size / 2)
#     t.left(360 / n)
#     for i in range(n - 1):
#         t.forward(size)
#         t.left(360 / n)
#     t.forward(size / 2)
#     t.end_fill()
#
#
# def main():
#     t.speed(0)
#     t.hideturtle()
#     for y in range(130, -200, -75):
#         for x in range(-150, 170, 75):
#             t.penup()
#             t.goto(x, y)
#             t.pendown()
#             figure(r.randint(3, 6), 1800)
#
#
# main()
# __________________________________________________________________________________
# Напишите программу, которая рисует изображение шахматной доски по образцу.

# import turtle as t
# def chess():
#   y = 0
#   t.left(90)
#   for i in range(5):
#     for j in range(5):
#      if (i + j) % 2 == 0:
#        color = 'black'
#      else:
#        color = 'white'
#      t.fillcolor(color)
#      t.begin_fill()
#      for _ in range(3):
#       t.forward(20)
#       t.right(90)
#      t.forward(20)
#      t.end_fill()
#      t.backward(20)
#      t.right(90)
#     y += 20
#     t.penup()
#     t.goto(0, y)
#     t.pendown()
# chess()
#
# __________________________________________________________________________
# Напишите программу, которая рисует изображение компаса по образцу.
#
# import turtle as t
# t.hideturtle()
# f = ('Times New Roman', 11, 'normal')
# lst = ['Восток', 'Запад', 'Север', 'Юг']
# arr = [[(80, 0), (100, -5)], [(-80, 0), (-140, -5)],
# [(0, 80), (-20, 100)], [(0, -80), (-10, -100)]]
# i = 0
# for a, b in arr:
#   t.goto(a)
#   t.up()
#   t.goto(b)
#   t.write(lst[i], font=f)
#   t.goto(0, 0)
#   t.down()
#   i += 1
#
# t.goto(0, -20)
# t.down()
# t.circle(20)

# ___________________________________________________________________________
#
# Напишите программу, которая рисует солнечную систему по образцу.
# import turtle as t, math
#
# t.Screen().bgcolor('black')
# colors = ['#ffff66','#ad5a00','#fd5a0A', 'cyan',
# '#FF6347','#ad5a00','#ad5a00','#20B2AA', '#4169E1','#ad5a00']
# f = ('Times New Roman', 11, 'normal')
# lst = [[(-150, 0), (-170, -20)], [(-80, 80), (-100, 60)],
# [(-40, 20), (-60, 5)], [(-80, -100), (-100, -120)], [(0, -120), (-10, -135)],
# [(60, 60), (40, 40)], [(110, -100), (90, -120)]]
#
# circ = [50, 10, 20, 15, 12, 40, 45]
# plan = ['Солнце', 'Меркурий', 'Венера', 'Эемля', 'Марс', 'Юпитер', 'Сатурн']
# i = 0
# t.up()
# for a, b in lst:
#   t.goto(a)
#   t.fillcolor(colors[i])
#   t.begin_fill()
#   t.circle(circ[i])
#   t.end_fill()
#   t.goto(b)
#   t.fillcolor('white')
#   t.write(plan[i], font=f)
#   i += 1
#
# t.goto(110, -85)
# t.pensize(5)
# t.down()
# t.pencolor('blue')
# a, b = 70, 30
# dx = t.xcor()
# dy = t.ycor()
# for deg in range(361):
#     rad = math.radians(deg)
#     x = a * math.sin(rad) + dx
#     y = -b * math.cos(rad) + b + dy
#     t.goto(x, y)

# _____________________________________________________
# Напишите программу, которая рисует знак STOP по образцу.
# import turtle
#
#
# def stop(side, n):
#     angl = 360 // n
#     turtle.pensize(3)
#     for _ in range(n):
#         turtle.forward(side)
#         turtle.right(angl)
#     turtle.penup()
#     turtle.goto(side * 0.05, -side * 0.12)
#     turtle.fillcolor('red')
#     turtle.begin_fill()
#     for _ in range(n):
#         turtle.forward(side - side * 0.1)
#         turtle.right(angl)
#     turtle.end_fill()
#     turtle.goto(side * 0.5, -1.45 * side)
#     turtle.fillcolor('white')
#     turtle.begin_fill()
#     turtle.write('STOP', align='center', font=('Arial', 25, 'normal'))
#     turtle.end_fill()
#
#
# turtle.speed(0)
# stop(50, 8)
#
# ___________________________________________________________________________
# Напишите программу, которая рисует силуэты многоэтажек по образцу. Разделите программу на функции:
#
# рисования контуров зданий;
# рисования нескольких окон в зданиях;
# рисования случайно разбросанных звезд в виде точек (убедитесь, что звезды появляются на небе, а не на зданиях).
#
# mport turtle as t, random as r
# t.Screen().setup(400, 400)
# t.Screen().bgcolor('midnightblue')
# t.speed(0)
# t.ht()
#
# def draw_stars():
#   t.fillcolor('yellow')
#   for _ in range(40):
#     x = r.randint(-200, 200)
#     y = r.randint(-200, 200)
#     t.setposition(x, y)
#     t.begin_fill()
#     t.circle(r.randint(1, 3))
#     t.end_fill()
#
# def draw_buildings():
#   t.setposition(-200, -200)
#   for _ in range(14):
#     t.fillcolor('black')
#     t.begin_fill()
#     a = r.randint(30, 60)
#     b = r.randint(120, 250)
#     for i in range(2):
#       t.forward(a)
#       t.left(90)
#       t.forward(b)
#       t.left(90)
#     t.end_fill()
#     rb = r.randint(0, 4)
#     for i in range(0, rb):
#       x = t.xcor()
#       y = t.ycor()
#       if a < 48:
#         sx = a // 2 - 6
#       else:
#         sx = r.choice([6, 30])
#       t.setposition(x + sx, y + r.randrange(y + 9, b - 21, 30))
#       t.pendown()
#       t.fillcolor('gold')
#       t.begin_fill()
#       for i in range(4):
#         t.forward(12)
#         t.left(90)
#       t.end_fill()
#       t.up()
#       t.goto(x, y)
#     t.forward(a)
#
# t.up()
# t.tracer(25, 0)
# draw_stars()
# draw_buildings()
# ________________________________________________
# Напишите программу, которая рисует изображение сердца по образцу.
# import turtle, math
#
# turtle.up()
#
#
# def dart():
#     turtle.goto(0, -50)
#     turtle.down()
#     turtle.pensize(5)
#     turtle.left(45)
#     turtle.forward(150)
#     turtle.left(180)
#     turtle.forward(50)
#     turtle.left(180)
#     for _ in range(5):
#         x, y = turtle.pos()
#         turtle.left(45)
#         turtle.forward(15)
#         turtle.goto(x, y)
#         turtle.right(90)
#         turtle.forward(15)
#         turtle.goto(x, y)
#         turtle.left(45)
#         turtle.forward(10)
#     turtle.up()
#     turtle.goto(-56, -106)
#     turtle.left(180)
#     turtle.down()
#     turtle.forward(60)
#     turtle.shape('arrow')
#     turtle.stamp()
#
#
# def heart():
#     turtle.fillcolor('red')
#     turtle.begin_fill()
#     for t in range(630):
#         t *= 0.01
#         x = 128 * math.sin(t) ** 3
#         y = 8 * (13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t) - 5)
#         turtle.goto(x, y)
#     turtle.end_fill()
#
#
# heart()
# dart()






