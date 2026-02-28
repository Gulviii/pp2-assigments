S = input().strip()
count = 0
for i in S:
    if i.isupper():
        count += 1
print(count)