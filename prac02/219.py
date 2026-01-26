n = int(input())
episodes = {}

for _ in range(n):
    s, k = input().split()
    k = int(k)
    if s not in episodes:
        episodes[s] = 0
    episodes[s] += k
for dorama in sorted(episodes.keys()):
    print(dorama, episodes[dorama])
