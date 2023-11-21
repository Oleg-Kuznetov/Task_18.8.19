tickets = int(input('Введите необходимое количество билетов: ')) # вводим необходимое количество билетов
sum = 0
visitor = 1
for age in range(tickets):
    age = int(input('Введите возраст посетителя № %s: ' % visitor))
    if age < 18:
        print('Цена билета: ', 0)
        sum += 0
    elif 18 <= age <= 25:
        print('Цена билета: ', 990)
        sum += 990
    elif age > 25:
        print('Цена билета: ', 1390)
        sum += 1390
    visitor += 1
if tickets > 3:
    sum = sum * 0.9
    print('Вы заказали более 3-х билетов и получаете скидку 10%')
print('Общая стоимость билетов: ', sum)