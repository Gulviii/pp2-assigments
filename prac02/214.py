n = int(input())
arr = list(map(int, input().split()))
freq = {}
for x in arr:
    freq[x] = freq.get(x, 0) + 1
max_freq = max(freq.values())
candidates = [key for key, val in freq.items() if val == max_freq]
result = min(candidates)

print(result)
