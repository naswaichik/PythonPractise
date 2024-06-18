initial_distance = 10
increase_rate = 10
days_in_week = 7
distances = [initial_distance]
for i in range(1, days_in_week):
    distances.append(distances[-1] * (1 + increase_rate / 100))
total_distance = sum(distances)
print("Суммарный путь за неделю:", total_distance, "км")