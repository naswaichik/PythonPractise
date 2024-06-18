stipend = int(input("Введите размер стипендии: "))
expenses = int(input("Введите размер расходов на проживание: "))
growth_rate = 3
months = 10
total_expenses = expenses * (1 + growth_rate / 100) ** months
deficit = total_expenses - stipend * months
print("Необходимая сумма для единовременной просьбы у родителей:", deficit)