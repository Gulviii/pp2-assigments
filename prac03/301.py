def is_valid_number(n: int) -> str:
    for digit in str(n):
        if int(digit) % 2 != 0:
            return "Not valid"
    return "Valid"
n = int(input())
print(is_valid_number(n))