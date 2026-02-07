# 1. Қарапайым lambda
square = lambda x: x**2
print(square(5))

# 2. map() қолдану
nums = [1, 2, 3, 4]
squares = list(map(lambda x: x**2, nums))
print(squares)

# 3. filter() қолдану
nums = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)

# 4. sorted() қолдану
words = ["apple", "banana", "kiwi"]
sorted_words = sorted(words, key=lambda w: len(w))
print(sorted_words)
