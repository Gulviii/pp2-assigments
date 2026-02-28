#string that has an 'a' followed by zero or more 'b''s.
import re
pattern = r'ab*'
tests = ["a", "ab", "abb", "ac", "b"]
for t in tests:
    print(t, bool(re.fullmatch(pattern, t)))

# string that has an 'a' followed by two to three 'b'
import re
pattern = r'ab{2,3}'
tests = ["abb", "abbb", "ab", "abbbb"]
for t in tests:
    print(t, bool(re.fullmatch(pattern, t)))

#find sequences of lowercase letters joined with a underscore.
import re
pattern = r'[a-z]+_[a-z]+'
tests = ["abc_def", "abc_def_ghi", "Abc_def"]
for t in tests:
    print(t, bool(re.fullmatch(pattern, t)))

# find the sequences of one upper case letter followed by lower case letters.
import re
pattern = r'[A-Z][a-z]+'
tests = ["Hello", "World", "HELLO", "hELLO"]
for t in tests:
    print(t, bool(re.fullmatch(pattern, t)))

#matches a string that has an 'a' followed by anything, ending in 'b'
import re
pattern = r'a.*b'
tests = ["ab", "axxxb", "a123b", "ac"]
for t in tests:
    print(t, bool(re.fullmatch(pattern, t)))

#replace all occurrences of space, comma, or dot with a colon.
import re
text = "Python is, great. Really"
print(re.sub(r"[ ,.]", ":", text))

#convert snake case string to camel case string.
def snake_to_camel(s):
    parts = s.split('_')
    return parts[0] + ''.join(p.capitalize() for p in parts[1:])
print(snake_to_camel("hello_world_example"))

#split a string at uppercase letters.
import re
text = "SplitAtUpperCaseLetters"
print(re.split(r'(?=[A-Z])', text))

#insert spaces between words starting with capital letters.
import re
text = "InsertSpacesBetweenWordsStartingWithCapitalLetters"
print(re.sub(r'([A-Z])', r' \1', text).strip())

#convert a given camel case string to snake case.
import re
def camel_to_snake(s):
    return re.sub(r'([A-Z])', r'_\1', s).lower()
print(camel_to_snake("CamelCaseString"))