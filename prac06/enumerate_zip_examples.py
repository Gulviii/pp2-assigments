names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

# enumerate
for i, name in enumerate(names, start=1):
    print(i, name)

# zip
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")

# type checking & conversions
print(isinstance(25, int))
print(float("3.14"))
