n = int(input())
numbers = list(map(int, input().split()))
distinct_numbers = sorted(set(numbers))
print(' '.join(map(str, distinct_numbers)))