codes = {
    "ZER": "0", "ONE": "1", "TWO": "2", "THR": "3",
    "FOU": "4", "FIV": "5", "SIX": "6", "SEV": "7",
    "EIG": "8", "NIN": "9"
}
digits = {v: k for k, v in codes.items()}
expr = input().strip()

if "+" in expr:
    a, b = expr.split("+")
    res = int("".join(codes[a[i:i+3]] for i in range(0, len(a), 3))) + \
          int("".join(codes[b[i:i+3]] for i in range(0, len(b), 3)))
elif "-" in expr:
    a, b = expr.split("-")
    res = int("".join(codes[a[i:i+3]] for i in range(0, len(a), 3))) - \
          int("".join(codes[b[i:i+3]] for i in range(0, len(b), 3)))
else:
    a, b = expr.split("*")
    res = int("".join(codes[a[i:i+3]] for i in range(0, len(a), 3))) * \
          int("".join(codes[b[i:i+3]] for i in range(0, len(b), 3)))
print("".join(digits[d] for d in str(res)))