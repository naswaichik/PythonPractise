import numpy as np
initial_population = 1
hours = np.arange(3, 25, 3)
num_divisions = hours / 3
populations = initial_population * (2 * num_divisions)
for hour, population in zip(hours, populations):
    print(f"Через {hour} часов будет {population} амеб")