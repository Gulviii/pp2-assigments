n = int(input())
numbers = [input().strip() for _ in range(n)]
freq = {}
for num in numbers:
    freq[num] = freq.get(num, 0) + 1
count = sum(1 for val in freq.values() if val == 3)

print(count)