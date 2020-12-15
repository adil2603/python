earnings = int(input("Введите выручку фирмы: "))
expense = int(input("Введите убыток фирмы: "))

if earnings > expense:
    profit = earnings - expense
    print(f"Ваша фирма в прибыле. Ваш прибыль: {profit} рублей")
    employee = int(input("Введите количество сотрудников: "))
    averageprofit = profit / employee
    print(f"Прибыль фирмы в расчете на одного сотрудника: {averageprofit} рублей")

else:
    print("Ваша фирма убыточная")
