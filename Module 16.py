Задание 16.9.1
Создайте класс любых геометрических фигур, где на выход мы получаем характеристики фигуры. Каждый экземпляр должен иметь атрибуты, которые зависят от выбранной фигуры. Например, для прямоугольника это будут аргументы x, y, width и height.

class GeometricFigure():
    def __init__(self,width, height ):
        self.x = width
        self.y = height

    def Parameters(self):
        return f"width = {self.x} height = {self.y}"

n = GeometricFigure(5, 9)
print(n.Parameters())
# _______________________________________
# Задание 16.9.3
# В проекте «Дом питомца» скоро появится новая услуга: электронный кошелек. То есть система будет хранить данные о своих клиентах и об их финансовых операциях.
#
# Вам нужно написать программу, обрабатывающую данные, и на выходе в консоль получить следующее: Клиент "Иван Петров". Баланс: 50 руб.

class Wallet():
    def __init__(self, name, surname, balance):
        self. name = name
        self.surname = surname
        self.balance = int(balance)

    def Parameters(self):
       return f"Клиент {self. name} {self. surname}. Баланс: {self.balance} руб."

    def IncreaseBalance(self, sum):
        self.balance += int(sum)

    def DecreaseBalance(self, sum):
        self.balance += int(sum)

n = Wallet("Иван", "Петров", 50)
print(n.Parameters())
print(n.IncreaseBalance(100))
print(n.Parameters())
# _________________________________________
# Задание 16.9.4

# Команда проекта «Дом питомца» планирует большой корпоратив для своих волонтеров. Вам необходимо написать программу, которая позволяла бы составлять список нескольких гостей. Решите задачу с помощью метода конструктора и примените один из принципов наследования.
#
# При выводе в консоль вы должны получить:  “Иван Петров, г.Москва, статус "Наставник"

class Corporate():
    def __init__(self, name, city, status):
        self.name = name
        self.city = city
        self.status = status

    def Parameters(self):
        return f"{self. name}, г.{self.city},статус '{self.status}'"

n = Corporate("Иван Петров","Москва" ,"Наставник")
print(n.Parameters())