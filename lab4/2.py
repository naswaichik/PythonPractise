import math

# Вариант 1
def func1(t):
    if 0.5 <= t <= 1:
        return math.cos(2 * math.pi * t)
    else:
        return math.log(7) / 7

t = float(input("Введите t: "))
y = func1(t)
print(f"y = {y}")

# Вариант 2
def func2(x):
    return 1.5 * x*2 + 1.3 * x - 1.3

x = float(input("Введите x: "))
y = func2(x)
print(f"y = {y}")

# Вариант 3
def func3(x):
    return (1.2 * x*2 + 1.2 * x + 1.2) / (1 + x*2 + x*4)

x = float(input("Введите x: "))
y = func3(x)
print(f"y = {y}")

# Вариант 4
def func4(x):
    return 0.3 * x*2 + 2.8 * x - 4

x = float(input("Введите x: "))
y = func4(x)
print(f"y = {y}")

# Вариант 5
def func5(x):
    return math.exp(2.5 * x) * math.cos(math.pi * x) - math.sin(3 * math.pi * x)

x = float(input("Введите x: "))
y = func5(x)
print(f"y = {y}")

# Вариант 6
def func6(x):
    return math.exp(x) * math.sin(2.8 * x) / (1 + math.cos(6 * math.pi * x))

x = float(input("Введите x: "))
y = func6(x)
print(f"y = {y}")

# Вариант 7
def func7(i):
    return 20.5 * i*2 + 1.8 * i - 2.1

i = int(input("Введите i: "))
y = func7(i)
print(f"y = {y}")

# Вариант 8
def func8(t):
    return math.cos(2 * math.pi * t) * math.sin(2 * math.pi * t) / (1 + math.cos(2 * math.pi * t) * math.sin(2 * math.pi * t))

t = float(input("Введите t: "))
y = func8(t)
print(f"y = {y}")

# Вариант 9
def func9(x):
    return math.log(1 + x) / (1 - x)

x = float(input("Введите x: "))
y = func9(x)
print(f"y = {y}")

# Вариант 10
def func10(x):
    return (math.cos(2 * math.pi * x) * math.sin(2 * math.pi * x)) / (1 / (math.log(x + 1)) + x*2 + x*3)

x = float(input("Введите x: "))
y = func10(x)
print(f"y = {y}")
