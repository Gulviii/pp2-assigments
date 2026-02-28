import re
S = input().strip()
pattern = r'^\d+$'
if re.match(pattern, S):
    print("Match")
else:
    print("No match")