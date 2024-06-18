initial_pages = 40
increase_rate = 5
days = 10
pages_read = [initial_pages]
for i in range(1, days):
    pages_read.append(pages_read[-1] * (1 + increase_rate / 100))
total_pages = sum(pages_read)
print("Общее количество страниц в книге:", total_pages)