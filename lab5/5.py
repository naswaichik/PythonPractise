n = 25
numbers = []
for i in range(n):
    num = float(input(f"Введите {i + 1}-е число: "))
    numbers.append(num)

sum = 0
for num in numbers:
    sum += num

product = 1
for num in numbers:
    product *= num

print(f"Сумма чисел: {sum}")
print(f"Произведение чисел: {product}")