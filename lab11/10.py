sequence = [int(input()) for _ in range(18)]

even_list = []
for x in sequence:
    if x % 2 == 0:
        even_list.append(x)

if even_list:
    print("Список четных чисел:", even_list)
else:
    print("Четных чисел нет")