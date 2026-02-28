import re
S = input().strip()
pattern = r'\b\d{2}/\d{2}/\d{4}\b'
matches = re.findall(pattern, S)
print(len(matches))
