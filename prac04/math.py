import math #Градус → радианға түрлендіру
degree = 15
radian = math.radians(degree)
print("Input degree:", degree)
print("Output radian:", radian)

height = 5 #2Трапецияның ауданын есептеу 
base1 = 5
base2 = 6
area = ((base1 + base2) / 2) * height
print("Expected Output:", area)

import math #Дұрыс көпбұрыштың ауданы
n = 4
s = 25
area = (n * s**2) / (4 * math.tan(math.pi / n))
print("The area of the polygon is:", area)

base = 5 #Параллелограммның ауданы
height = 6
area = base * height
print("Expected Output:", float(area))