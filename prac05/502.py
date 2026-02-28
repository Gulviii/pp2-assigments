import re
S = input().strip()
P = input().strip()
if re.search(P, S):
    print("Yes")
else:
    print("No")
 
 