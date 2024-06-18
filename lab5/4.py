k = 3
sum = 0
for i in range(1000, 10000):
    if i % k == 0:
        sum += i

print(sum)