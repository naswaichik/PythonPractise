k = 3
start = 1000
end = 9999
sum = 0
for num in range(start, end + 1):
    if num % k == 0:
        sum += num

print("Сумма 4-значных чисел, кратных", k, "равна:", sum)