def среднее_значение(список):
  if len(список) == 0:
    print("Среднее значение: 0")
  else:
    среднее = sum(список) / len(список)
    print("Среднее значение:", среднее)

список_чисел = list(map(int, input("Введите список чисел через пробел: ").split()))
среднее_значение(список_чисел)