# Вариант 1
def variant_1():
  """Выводит слова с дефисами между буквами в верхнем регистре."""
  text = input("Введите строку: ")
  words = text.split()
  result = []
  for word in words:
    result.append('-'.join(word.upper()))
  print("Результат:", ' '.join(result))

# Вариант 2
def variant_2():
  """Выводит максимальное количество повторений символа в строке."""
  text = input("Введите строку: ")
  char_counts = {}
  for char in text:
    char_counts[char.lower()] = char_counts.get(char.lower(), 0) + 1
  max_count = max(char_counts.values())
  print("Максимальное количество повторений:", max_count)

# Вариант 3
def variant_3():
  """Вычисляет сумму чисел в диапазоне."""
  numbers = [int(x) for x in input("Введите числа через пробел: ").split()]
  start, end = map(int, input("Введите начальный и конечный индексы (через пробел): ").split())
  sum_numbers = sum(numbers[start:end+1])
  print("Сумма:", sum_numbers)

# Вариант 4
def variant_4():
  """Вычисляет произведение чисел в диапазоне."""
  numbers = [int(x) for x in input("Введите числа через пробел: ").split()]
  start, end = map(int, input("Введите начальный и конечный индексы (через пробел): ").split())
  product = 1
  for i in range(start, end+1):
    product *= numbers[i]
  print("Произведение:", product)

# Вариант 5
def variant_5():
  """Вычисляет сумму квадратов чисел в диапазоне."""
  numbers = [int(x) for x in input("Введите числа через пробел: ").split()]
  start, end = map(int, input("Введите начальный и конечный индексы (через пробел): ").split())
  sum_squares = sum([number*2 for number in numbers[start:end+1]])
  print("Сумма квадратов:", sum_squares)

# Вариант 6
def variant_6():
  """Находит длину самого короткого слова."""
  text = input("Введите строку: ")
  words = text.split()
  min_length = len(words[0])
  for word in words:
    if len(word) < min_length:
      min_length = len(word)
  print("Длина самого короткого слова:", min_length)

# Вариант 7
def variant_7():
  """Выводит слова в обратном порядке с плюсами между буквами."""
  text = input("Введите строку: ")
  words = text.split()
  result = []
  for word in words[::-1]:
    result.append('+'.join(word))
  print("Результат:", ' '.join(result))

# Вариант 8
def variant_8():
  """Находит длину самого длинного слова."""
  text = input("Введите строку: ")
  words = text.split()
  max_length = len(words[0])
  for word in words:
    if len(word) > max_length:
      max_length = len(word)
  print("Длина самого длинного слова:", max_length)

# Вариант 9
def variant_9():
  """Выводит буквы слов в алфавитном порядке."""
  text = input("Введите строку: ")
  letters = ''.join(text.lower().split())
  result = ':'.join(sorted(letters))
  print("Результат:", result)

# Вариант 10
def variant_10():
  """Выводит максимальное количество повторений символа в строке."""
  text = input("Введите строку: ")
  char_counts = {}
  for char in text:
    char_counts[char] = char_counts.get(char, 0) + 1
  max_count = max(char_counts.values())
  print("Максимальное количество повторений:", max_count)

variant_number = int(input("Введите номер варианта задания (1-10): "))

if variant_number == 1:
  variant_1()
elif variant_number == 2:
  variant_2()
elif variant_number == 3:
  variant_3()
elif variant_number == 4:
  variant_4()
elif variant_number == 5:
  variant_5()
elif variant_number == 6:
  variant_6()
elif variant_number == 7:
  variant_7()
elif variant_number == 8:
  variant_8()
elif variant_number == 9:
  variant_9()
elif variant_number == 10:
  variant_10()
else:
  print("Неверный номер варианта.")
