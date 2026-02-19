def prime_generator(n):
    def is_prime(x):
        if x < 2:
            return False
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                return False
        return True
    for num in range(2, n+1):
        if is_prime(num):
            yield str(num)
a = int(input())
print(" ".join(prime_generator(a)))
