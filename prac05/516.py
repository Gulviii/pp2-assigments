import re
S = input().strip()
pattern = r'Name:\s*(.+?),\s*Age:\s*(\d+)'
match = re.search(pattern, S)
if match:
    name = match.group(1)
    age = match.group(2)
    print(name, age)
else:
    print("Invalid input format")
