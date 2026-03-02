n = int(input())
numbers = list(map(int, input().split()))
s = list(map(lambda x: x >= 0, numbers))
result = all(s)
if result:
    print("Yes")    
else:
    print("No")