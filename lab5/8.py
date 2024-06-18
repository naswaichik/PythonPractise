start = 7
end = 37
sum = 0
for i in range(start, end + 1, 2):
    # Куб нечетного числа
    cube = i ** 3
    sum += cube
print("Сумма кубов нечетных чисел от", start, "до", end, "равна", sum)