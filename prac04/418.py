x_a, y_a = map(float, input().split())
x_c, y_c = map(float, input().split())

t = y_a / (y_a + y_c)
x_r = x_a + t * (x_c - x_a)
y_r = 0.0

print(f"{x_r:.10f} {y_r:.10f}")
