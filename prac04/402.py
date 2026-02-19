n = int(input())

for i in range(n + 1):
    if n == 1:
        print(0)
        break
    elif n == 0:
        print(0)
        break
    if n % 2 == 0:
        if i % 2 == 0 and n > 1 and i != n:
            print(i, end=',')
        elif i == n:
            print(n)
    if n % 2 != 0:
        if i % 2 == 0 and n > 1 and i != n - 1:
            print(i, end=',')
        elif i % 2 == 0 and i == n - 1:
            print(n - 1)