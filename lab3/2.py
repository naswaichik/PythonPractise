# Вариант 1
a = float(input("Введите число a: "))
b = float(input("Введите число b: "))
c = float(input("Введите число c: "))

if a >= 0:
    a = a*2
else:
    a = a*4
if b >= 0:
    b = b*2
else:
    b = b*4
if c >= 0:
    c = c*2
else:
    c = c*4

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

# Вариант 2
a = float(input("Введите число a: "))
b = float(input("Введите число b: "))

if abs(a) > abs(b):
    a = a / 5

print(f"a = {a}")
print(f"b = {b}")

# Вариант 3
x = float(input("Введите число x: "))
y = float(input("Введите число y: "))

if x < y:
    x = (x + y) / 2
    y = 2 * x * y
else:
    y = (x + y) / 2
    x = 2 * x * y

print(f"x = {x}")
print(f"y = {y}")

# Вариант 4
m = int(input("Введите число m: "))
n = int(input("Введите число n: "))

if m != n:
    if m > n:
        m = n = m
    else:
        m = n = n
else:
    m = n = 0

print(f"m = {m}")
print(f"n = {n}")

# Вариант 5
a = float(input("Введите число a: "))
b = float(input("Введите число b: "))
c = float(input("Введите число c: "))

count_negative = 0
if a < 0:
    count_negative += 1
if b < 0:
    count_negative += 1
if c < 0:
    count_negative += 1

print(f"count_negative = {count_negative}")

# Вариант 6
a = float(input("Введите число a: "))
b = float(input("Введите число b: "))
c = float(input("Введите число c: "))

count_positive = 0
if a > 0:
    count_positive += 1
if b > 0:
    count_positive += 1
if c > 0:
    count_positive += 1

print(f"count_positive = {count_positive}")

# Вариант 7
a = int(input("Введите число a: "))
b = int(input("Введите число b: "))
c = int(input("Введите число c: "))

count_two_digit = 0
if 10 <= a <= 99:
    count_two_digit += 1
if 10 <= b <= 99:
    count_two_digit += 1
if 10 <= c <= 99:
    count_two_digit += 1

print(f"count_two_digit = {count_two_digit}")

# Вариант 8
temperature = float(input("Введите температуру в комнате: "))

if temperature > 60:
    print("Пожароопасная ситуация")

# Вариант 9
m = float(input("Введите массу первого пакета: "))
n = float(input("Введите массу второго пакета: "))

if m > n:
    print("Первый пакет тяжелее")
else:
    print("Второй пакет тяжелее")

# Вариант 10
m = float(input("Введите массу первого пакета: "))
n = float(input("Введите массу второго пакета: "))

if m > n:
    mass_heavier = m
else:
    mass_heavier = n

print(f"Масса более тяжелого пакета: {mass_heavier}")
