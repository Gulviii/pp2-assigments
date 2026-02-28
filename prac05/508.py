import re
S = input().strip()
P = input().strip()
parts = re.split(P, S)
print(','.join(parts))