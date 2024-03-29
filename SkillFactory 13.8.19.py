# Для онлайн-конференции необходимо написать программу, которая будет подсчитывать общую стоимость билетов. Программа должна работать следующим образом:
#
# 1. В начале у пользователя запрашивается количество билетов, которые он хочет приобрести на мероприятие.
#
# 2. Далее для каждого билета запрашивается возраст посетителя, в соответствии со значением которого выбирается стоимость:
#
# Если посетителю конференции менее 18 лет, то он проходит на конференцию бесплатно.
# От 18 до 25 лет — 990 руб.
# От 25 лет — полная стоимость 1390 руб.
# 3. В результате программы выводится сумма к оплате. При этом, если человек регистрирует больше трёх человек на конференцию, то дополнительно получает 10% скидку на полную стоимость заказа.


num_of_ticket = int(input("Какое количество билетов, вы хочете приобрести на мероприятие?\n"))
age_of_visitor = 0
amount_to_pay = 0
num_of_persons = 0
for i in range(num_of_ticket):
      age_of_visitor = int(input("Укажите пожалуйста возраст посетителя, для  которого приобритате билет:\n"))
      if age_of_visitor < 18:
            amount_to_pay +=0
            num_of_persons += 1
      if 18 <= age_of_visitor < 25:
            amount_to_pay += 990
            num_of_persons += 1
      if  age_of_visitor >= 25:
            amount_to_pay += 1390
            num_of_persons += 1
if num_of_persons > 3:
      print(f"Вам необходимо оплатить {amount_to_pay - amount_to_pay/100*10} руб.")
elif amount_to_pay == 0:
      print(f"Ваше  посещение  будет  бесплатным, так как все посетители моложе 18 лет.")
else:
      print(f"Вам необходимо оплатить {amount_to_pay} руб.")