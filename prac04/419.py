import math
R = float(input().strip())
x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())
def dist(x,y): return math.hypot(x,y)
def segment_intersects(x1,y1,x2,y2,R):
    dx, dy = x2-x1, y2-y1
    A = dx*dx+dy*dy
    B = 2*(x1*dx+y1*dy)
    C = x1*x1+y1*y1-R*R
    disc = B*B-4*A*C
    if disc < 0: return False
    sqrt_disc = math.sqrt(disc)
    t1 = (-B - sqrt_disc)/(2*A)
    t2 = (-B + sqrt_disc)/(2*A)
    return (0<=t1<=1) or (0<=t2<=1)

if not segment_intersects(x1,y1,x2,y2,R):
    ans = dist(x2-x1,y2-y1)
else:
    def tangents(px,py):
        d = math.hypot(px,py)
        ang = math.atan2(py,px)
        alpha = math.acos(R/d)
        return [(R*math.cos(ang+alpha), R*math.sin(ang+alpha)),
                (R*math.cos(ang-alpha), R*math.sin(ang-alpha))]
    ta_list = tangents(x1,y1)
    tb_list = tangents(x2,y2)
    best = 1e100
    for ta in ta_list:
        for tb in tb_list:
            d1 = dist(ta[0]-x1, ta[1]-y1)
            d2 = dist(tb[0]-x2, tb[1]-y2)
            ang1 = math.atan2(ta[1], ta[0])
            ang2 = math.atan2(tb[1], tb[0])
            diff = abs(ang1-ang2)
            diff = min(diff, 2*math.pi-diff)
            arc = R*diff
            total = d1 + arc + d2
            best = min(best, total)
    ans = best

print(f"{ans:.10f}")