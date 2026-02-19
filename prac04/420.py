g = 0
n = 0

q = int(input().strip())
for _ in range(q):
    scope, val = input().split()
    val = int(val)
    if scope == "global":
        g += val
    elif scope == "nonlocal":
        n += val

print(g, n)
