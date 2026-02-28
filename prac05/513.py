import re
S = input().strip()
pattern = r'\w+'
matches = re.findall(pattern, S)
print(len(matches))