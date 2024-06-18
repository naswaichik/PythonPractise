n = 15
numbers = []
import random
for i in range(n):
    numbers.append(random.randint(1, 100))
sum = 0
for num in numbers:
    sum += num
product = 1
for num in numbers:
    product *= num
print("Сумма:", sum)
print("Произведение:", product)