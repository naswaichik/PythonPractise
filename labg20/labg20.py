from PIL import Image, ImageDraw

# Создаем новое изображение
image = Image.new("RGB", (2000, 2000), "white")
draw = ImageDraw.Draw(image)

# Рисуем букву V
draw.line([(100, 100), (200, 300)], fill="blue", width=30)
draw.line([(100, 100), (0, 300)], fill="blue", width=30)

# Рисуем букву A
draw.line([(300, 300), (400, 100)], fill="red", width=30)
draw.line([(400, 100), (500, 300)], fill="red", width=30)
draw.line([(350, 200), (450, 200)], fill="red", width=30)

# Рисуем букву N
draw.line([(600, 100), (600, 300)], fill="cyan", width=30)
draw.line([(600, 100), (700, 300)], fill="cyan", width=30)
draw.line([(700, 100), (700, 300)], fill="cyan", width=30)

# Рисуем букву I
draw.line([(800, 100), (800, 300)], fill="black", width=30)

# Рисуем букву A
draw.line([(900, 300), (1000, 100)], fill="darkorange", width=30)
draw.line([(1000, 100), (1100, 300)], fill="darkorange", width=30)
draw.line([(950, 200), (1050, 200)], fill="darkorange", width=30)

# Сохраняем изображение
image.show()