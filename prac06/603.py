n = int(input())
g = list(map(str, input().split()))
for i in range(0,n):
    print(f"{i}:{g[i]}", end=' ')