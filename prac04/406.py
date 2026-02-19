def fib_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield str(a)
        a, b = b, a + b
count = int(input())
print(",".join(fib_generator(count)))
