import json
import sys

def diff(obj1, obj2, path=""):
    differences = []
    if isinstance(obj1, dict) and isinstance(obj2, dict):
        keys = set(obj1.keys()) | set(obj2.keys())
        for k in keys:
            new_path = f"{path}.{k}" if path else k
            v1 = obj1.get(k, "<missing>")
            v2 = obj2.get(k, "<missing>")
            if v1 == "<missing>" or v2 == "<missing>":
                differences.append((new_path, v1, v2))
            else:
                differences.extend(diff(v1, v2, new_path))
    elif isinstance(obj1, list) and isinstance(obj2, list):
        # массивті тұтас салыстыру
        if obj1 != obj2:
            differences.append((path, obj1, obj2))
    else:
        if obj1 != obj2:
            differences.append((path, obj1, obj2))
    return differences

def serialize(val):
    return val if val == "<missing>" else json.dumps(val, separators=(',', ':'))

def main():
    obj1 = json.loads(sys.stdin.readline().strip())
    obj2 = json.loads(sys.stdin.readline().strip())
    differences = diff(obj1, obj2)
    if not differences:
        print("No differences")
    else:
        for path, v1, v2 in sorted(differences, key=lambda x: x[0]):
            print(f"{path} : {serialize(v1)} -> {serialize(v2)}")

if __name__ == "__main__":
    main()
