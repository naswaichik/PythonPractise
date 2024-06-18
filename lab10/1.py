set1 = set(map(int, input("Введите числа в первое множество, разделяя их пробелами: ").split()))
set2 = set(map(int, input("Введите числа во второе множество, разделяя их пробелами: ").split()))

all_numbers = set1.union(set2)
print("Различные числа в обоих множествах:", all_numbers)

intersection = set1.intersection(set2)
print("Числа, которые входят как в первое, так и во второе множества:", intersection)