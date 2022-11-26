salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

money_capital = 0  # количество денег, чтобы прожить 10 месяцев

while months > 0:
    delta = spend - salary  # Определяем долг
    spend *= 1 + increase  # Траты с учетом роста цен
    money_capital += delta
    months -= 1  # Перебираем месяцы
print(round(money_capital))
