y = 40
days_to_finish = 10
pages_total = 0

for i in range(days_to_finish):
    pages_total += y
    y = y * 1.05

print(pages_total)