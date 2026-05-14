"""
Python String: Concepts, Methods, Examples, Mini-project, and Interview Q&A

Definition:
------------
A string in Python is an immutable sequence of Unicode characters. It's one of the core data types widely used for text processing.

String Methods and Concepts:
---------------------------
- Creation
- Indexing & Slicing
- Concatenation (+), Repetition (*)
- Built-in Functions: len(), str(), etc.
- String Methods: .lower(), .upper(), .title(), .capitalize(), .find(), .replace(), .split(), .join(), .strip(), .startswith(), .endswith(), .format(), f-strings, .count(), .isdigit(), .isalpha(), etc.
- String Immutability
- Iterating Strings
- Encoding/Decoding

Syntax:
-------
# Creation
s = "Hello, World!"

# Slicing
substr = s[0:5]

# Concatenation
greet = "Hello" + " " + "Sai"

# Join/Split
",".join(['a', 'b', 'c'])
'1,2,3'.split(',')

# Advanced Formatting
f"Name: {name}, Age: {age}"

-----------------------------------------------
Beginner Level Examples
-----------------------------------------------
"""

# Creation & Initialization
s1 = "Hello"
s2 = 'World'
s3 = """This is a
multi-line string."""

# Indexing
print(s1[0])        # H
print(s1[-1])       # o


# Slicing
print(s2[1:4])      # orl

# Concatenation
greet = s1 + " " + s2
print(greet)        # Hello World

# Repetition
echo = s1 * 3
print(echo)         # HelloHelloHello

# Length
print(len(s3))   # 11

# Iteration
for char in "hi":
    print(char)

# Membership
print('H' in s1)    # True

# String methods: lower, upper, title, capitalize
print(greet.lower())
print(greet.upper())
print(greet.title())
print(greet.capitalize())

# strip, lstrip, rstrip
messy = "   hello  \n"
print(messy.strip())    # 'hello'


"""
-----------------------------------------------
Intermediate Level Examples
-----------------------------------------------
"""

# split and join
csv = "red,green,blue"
colors = csv.split(',')
print(colors)
restored = ';'.join(colors)
print(restored)      # red;green;blue

# find and replace
sentence = "the cat sat on the mat"
print(sentence.find('cat'))      # 4
print(sentence.replace('cat', 'dog'))

# startswith and endswith
url = "https://sai.ai"
print(url.startswith("https"))
print(url.endswith(".ai"))

# count, isalpha, isdigit, isnumeric
sample = "abc123"
print(sample.isalpha())  # False
print(sample.isdigit())  # False
print("1234".isdigit())  # True
print("abcabc".count("a"))   # 2

# Formatting strings: format, f-strings, % formatting
name = "Sai"
age = 20
print("My name is {} and I am {} years old".format(name, age))
print(f"My name is {name.upper()} and I am {age+5} years old.")

# encode and decode (bytes/string)
b = "café".encode("utf-8")
print(b)
s = b.decode("utf-8")
print(s)

"""
-----------------------------------------------
Advanced Level Examples
-----------------------------------------------
"""

# Reversing a string
message = "Python"
rev = message[::-1]
print("Reversed:", rev)

# Palindrome check
def is_palindrome(text: str) -> bool:
    text = text.lower().replace(" ", "")
    return text == text[::-1]

print(is_palindrome("Ma dam"))         # True
print(is_palindrome("Sai"))           # False
print(is_palindrome("A man a plan a canal Panama"))  # True


# Frequency count of characters using dict & string methods
from collections import Counter
txt = "banana"
freq = Counter(txt)
print(freq)

# Remove vowels using join & list comprehension
s = "Hello World"
result = ''.join([c for c in s if c.lower() not in "aeiou"])
print(result)

# Advanced: Find and extract substrings using slicing and advanced logic
email = "User: sai@email.com | Name: Sai"
user_email = email[email.find(":")+2 : email.find("|")].strip()
print(user_email)

"""
-----------------------------------------------
Mini Project: Basic String Analyzer
-----------------------------------------------

Features:
- Take user input.
- Print stats: length, vowel count, consonant count, word count.
- Normalize (lowercase, strip spaces).
- Check palindrome.
- Print string in reverse.

"""

def string_analyzer(s: str):
    # Clean input
    norm = s.strip().lower()
    print(f"Normalized: '{norm}'")
    print(f"Length: {len(norm)}")
    print(f"Word count: {len(norm.split())}")
    # Count vowels & consonants
    vowels = "aeiou"
    vcount = sum(1 for c in norm if c in vowels)
    ccount = sum(1 for c in norm if c.isalpha() and c not in vowels)
    print(f"Vowels: {vcount}, Consonants: {ccount}")
    # Palindrome
    alphanum = ''.join(c for c in norm if c.isalnum())
    print("Palindrome:", alphanum == alphanum[::-1])
    # Reversed
    print("Reverse:", norm[::-1])

if __name__ == "__main__":
    prompt = "Enter a string to analyze: "
    try:
        sample = input(prompt)
    except EOFError:
        # No stdin (e.g. Run Code in OUTPUT panel, some CI); use a demo string.
        sample = ""
    if not sample.strip():
        sample = "Hello Sai"
        print(f"(no text entered — using demo: {sample!r})")
    string_analyzer(sample)

"""
--------------------------------------------------------------
INTERVIEW QUESTIONS & ANSWERS (PYTHON STRING)
--------------------------------------------------------------

Q1: Is a Python string mutable? What happens if you try to change one character?
A1: No, strings are immutable in Python. Any attempt to change an individual character (e.g., s[0] = 'X') raises a TypeError.

Q2: How does Python store strings internally? Explain Unicode support.
A2: Strings are sequences of Unicode codepoints, stored as UTF-8 (internally optimized but exposed as Unicode). This enables Python to support multilingual text.

Q3: Given a string with repeated patterns, how would you remove all duplicate letters, only keeping the first occurrence?
A3:
''.join(dict.fromkeys(s))
  Example: s = "banana" -> "ban"

Q4: Describe some differences between .split() and .partition().
A4: .split() divides a string at all occurrences of the separator and returns a list. .partition() splits into three parts: before, the separator, after, returning a tuple.

Q5: How do you reverse the order of words in a sentence string?
A5:
rev = ' '.join(s.split()[::-1])

Q6: Given a string, how to count how many times each vowel occurs using a dictionary comprehension?
A6:
s = "Hello World"
vowel_counts = {c: s.lower().count(c) for c in "aeiou"}

Q7: What's the difference between .isnumeric() and .isdigit()?
A7:
- .isdigit() is True for characters that are digits (0-9, even superscripts).
- .isnumeric() is True for numbers like fractions, subscripts, unicode numerals.
  Generally, .isnumeric() is more permissive.

Q8: Write a one-liner that checks if a string is a pangram (contains every alphabet letter at least once).
A8:
import string
all(c in s.lower() for c in string.ascii_lowercase)

Q9: How would you extract an email from a messy string using regular expressions?
A9:
import re
re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', messy_string)

Q10: How to efficiently join a list of 100,000 short strings into one?
A10:
Use ''.join(list_of_strings) as it is O(n) and avoids quadratic concatenation.

------------------------------------------------------------------
"""
