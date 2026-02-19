import math

R = float(input().strip())
x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

dx, dy = x2 - x1, y2 - y1
L = math.hypot(dx, dy)

A = dx*dx + dy*dy
B = 2*(x1*dx + y1*dy)
C = x1*x1 + y1*y1 - R*R

disc = B*B - 4*A*C
t_list = [0.0, 1.0]

if disc >= 0:
    sqrt_disc = math.sqrt(disc)
    t1 = (-B - sqrt_disc) / (2*A)
    t2 = (-B + sqrt_disc) / (2*A)
    if 0 <= t1 <= 1: t_list.append(t1)
    if 0 <= t2 <= 1: t_list.append(t2)

t_list.sort()

length_inside = 0.0
for i in range(len(t_list)-1):
    mid_t = (t_list[i] + t_list[i+1]) / 2
    mx, my = x1 + dx*mid_t, y1 + dy*mid_t
    if mx*mx + my*my <= R*R + 1e-9:
        length_inside += (t_list[i+1] - t_list[i]) * L

print(f"{length_inside:.10f}")