import re
S = input().rstrip("\n")
P = input().rstrip("\n")
pattern = re.escape(P)
count = 0
pos = 0
while True:
    m = re.search(pattern, S[pos:])
    if not m:
        break
    count += 1
    pos += m.start() + len(P) 
print(count)