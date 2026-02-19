import json
def patch(source, patch_obj):
    for k, v in patch_obj.items():
        if v is None:
            source.pop(k, None) 
        elif isinstance(v, dict) and isinstance(source.get(k), dict):
            patch(source[k], v)        
        else:
            source[k] = v 
    return source
src = json.loads(input().strip())
p = json.loads(input().strip())
res = patch(src, p)
print(json.dumps(res, sort_keys=True, separators=(',', ':')))
