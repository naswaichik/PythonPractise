start = 6
end = 36
sum = 0
for i in range(start, end + 1, 2):
    cube = i * 3
    sum += cube
print("Сумма кубов четных чисел от", start, "до", end, "равна", sum)