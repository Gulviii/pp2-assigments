#1‑ден N‑ге дейінгі квадраттар
def squares_up_to(n):
    for i in range(1, n+1):
        yield i * i
for val in squares_up_to(5):
    print(val)

#0‑ден n‑ге дейінгі жұп сандарды шығару
def even_numbers(n):
    for i in range(n+1):
        if i % 2 == 0:
            yield i
n = int(input("Enter n: "))
print(",".join(str(x) for x in even_numbers(n)))

#0‑ден n‑ге дейін 3‑ке және 4‑ке бөлінетін сандар
def divisible_by_3_and_4(n):
    for i in range(n+1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

for val in divisible_by_3_and_4(50):
    print(val)

#квадраттар (a‑дан b‑ге дейін)
def squares(a, b):
    for i in range(a, b+1):
        yield i * i

for val in squares(3, 7):
    print(val)