import sys
import json
import re

data = json.loads(sys.stdin.readline().strip())

q = int(sys.stdin.readline().strip())

for _ in range(q):
    query = sys.stdin.readline().strip()
    
    current = data
    found = True
    parts = re.split(r'\.', query)
    
    for part in parts:
        tokens = re.findall(r'([a-zA-Z_]\w*)|\[(\d+)\]', part)
        
        for key, index in tokens:
            if key: 
                if isinstance(current, dict) and key in current:
                    current = current[key]
                else:
                    found = False
                    break
            elif index:  
                idx = int(index)
                if isinstance(current, list) and 0 <= idx < len(current):
                    current = current[idx]
                else:
                    found = False
                    break
        
        if not found:
            break
    
    if found:
        print(json.dumps(current, separators=(',', ':')))
    else:
        print("NOT_FOUND")