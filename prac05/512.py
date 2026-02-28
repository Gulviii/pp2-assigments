import re
S = input().strip()
pattern = r'\d{2,}'
matches = re.findall(pattern, S)
print(' '.join(matches))