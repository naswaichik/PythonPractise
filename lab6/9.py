n = 40
sum = 0
for i in range(1, n + 1):
    square = (2 * i - 1) * 2
    sum += square
print("Сумма квадратов первых", n, "нечетных чисел равна", sum)