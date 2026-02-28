S = input().strip()
words = S.split()
count = sum(1 for word in words if len(word) == 3)
print(count)