import sys
n = int(sys.stdin.readline())
document = {}
out = []  
for _ in range(n):
    parts = sys.stdin.readline().split()
    if parts[0] == "set":
        key, value = parts[1], parts[2]
        document[key] = value
    else:  # get
        key = parts[1]
        if key in document:
            out.append(document[key])
        else:
            out.append(f"KE: no key {key} found in the document")
sys.stdout.write("\n".join(out))
