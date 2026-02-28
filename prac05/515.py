import re
S = input().strip()
pattern = r'\d'
result = re.sub(pattern, lambda x: x.group() * 2, S)
print(result)