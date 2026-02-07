# 1. Қарапайым функция
def greet(name):
    """Берілген атты қарсы алады"""
    return f"Hello, {name}!"

print(greet("Aman"))

# 2. Аргументтер: default мән
def power(base, exp=2):
    """Берілген санды дәрежеге шығарады"""
    return base ** exp

print(power(3))      # 3^2
print(power(3, 3))   # 3^3

# 3. *args қолдану
def add_all(*nums):
    """Көп сандарды қосады"""
    return sum(nums)

print(add_all(1, 2, 3, 4))

# 4. **kwargs қолдану
def show_info(**info):
    """Кілт-мәліметтерді шығару"""
    for k, v in info.items():
        print(f"{k}: {v}")

show_info(name="Bob", age=20)
