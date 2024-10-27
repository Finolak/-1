salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен (в условии задачи 5% а тут 3)
money_capital = 0

for x in range(months):
    money_capital += round(spend - salary)
    spend += spend * increase

print(f"Подушка безопасности, чтобы протянуть 10 месяцев без долгов:", money_capital)
