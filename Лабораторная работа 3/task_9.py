salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

money_capital = 0  # количество денег, чтобы прожить 10 месяцев

delta = spend - salary  # Долг за первый месяц
money_capital = delta
for i in range(2, months + 1):  # Перебираем каждый месяц
    spend *= 1 + increase  # Траты с учетом роста цен
    delta = spend - salary  # Долги за последующие месяцы
    money_capital += delta
print(round(money_capital))
