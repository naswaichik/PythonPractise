строка = input("Введите ненормированную строку: ")
строка = строка.strip()
строка = " ".join(строка.split())
print(строка)