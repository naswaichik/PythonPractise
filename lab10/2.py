variant = int(input("Введите вариант задания (от 1 до 10): "))
sequence = input("Введите последовательность символов: ")
elements = set()

if variant == 1:
    # Цифры от '0' до '9'
    for char in sequence:
        if '0' <= char <= '9':
            elements.add(char)
elif variant == 2:
    # Буквы от 'A' до 'Z' и цифры от '0' до '5'
    for char in sequence:
        if ('A' <= char <= 'Z') or ('0' <= char <= '5'):
            elements.add(char)
elif variant == 3:
    # Цифры от '5' до '9' и знаки арифметических операций
    for char in sequence:
        if (('5' <= char <= '9') or (char in '+-*/')):
            elements.add(char)
elif variant == 4:
    # Знаки арифметических операций и знаки препинания
    for char in sequence:
        if (char in '+-*/().,;:'):
            elements.add(char)
elif variant == 5:
    # Знаки препинания и операций отношения
    for char in sequence:
        if (char in '().,;:' or char in '<>='):
            elements.add(char)
elif variant == 6:
    # Знаки арифметических операций
    for char in sequence:
        if char in '+-*/':
            elements.add(char)
elif variant == 7:
    # Знаки препинания и буквы от 'E' до 'N'
    for char in sequence:
        if (char in '().,;:' or ('E' <= char <= 'N')):
            elements.add(char)
elif variant == 8:
    # Знаки арифметических операций и операций отношения
    for char in sequence:
        if (char in '+-*/' or char in '<>='):
            elements.add(char)
elif variant == 9:
    # Цифры и знаки арифметических операций
    for char in sequence:
        if (('0' <= char <= '9') or (char in '+-*/')):
            elements.add(char)
elif variant == 10:
    # Буквы от 'A' до 'F' и от 'X' до 'Z'
    for char in sequence:
        if (('A' <= char <= 'F') or ('X' <= char <= 'Z')):
            elements.add(char)

print("Множество элементов, встречающихся в последовательности:", elements)