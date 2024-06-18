initial_amebas = 1
division_time = 3
amebas = [initial_amebas]
for i in range(division_time, 25, division_time):
    amebas.append(amebas[-1] * 2)
for i, num in enumerate(amebas):
    print(f"Через {i * division_time} часов: {num} амеб")