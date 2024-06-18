start = 5
diff = 4
target = 324
terms = 0
sum = 0
while sum < target:
    sum += start
    terms += 1
    start += diff
print("Количество слагаемых для получения суммы, равной", target, "равно", terms)