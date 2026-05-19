'''
Python Break and Continue Statements
-------------------------------------

Definition:
-----------
- `break` and `continue` are loop control statements in Python used to change the flow of execution within loops.

Methods (Keywords):
-------------------
- `break`     : Exits the nearest enclosing loop immediately.
- `continue`  : Skips the current iteration and moves to the next iteration of the loop.

Syntax:
-------
# Using break
for item in iterable:
    if condition:
        break
    # code

while condition:
    if condition2:
        break
    # code


# Using continue
for item in iterable:
    if condition:
        continue
    # code

while condition:
    if condition2:
        continue
    # code

--------------------------
Beginner Level Examples
--------------------------
'''
# Example 1: Using break in a for loop
for num in range(1, 10):
    if num == 5:
        print("Breaking the loop at", num)
        break
    print(num)  # Output: 1 2 3 4

print('-' * 30)

# Example 2: Using continue in a for loop
for num in range(1, 6):
    if num == 3:
        print("Skipping", num)
        continue
    print(num)  # Output: 1 2 4 5

print('-' * 30)

# Example 3: Using break in a while loop
count = 0
while count < 5:
    print("count is", count)
    if count == 2:
        print("Breaking at count =", count)
        break
    count += 1

print('-' * 30)

# Example 4: Using continue in a while loop
count = 0
while count < 5:
    count += 1
    if count == 3:
        print("Skipping count =", count)
        continue
    print("count is", count)  # Skips printing for 3

print('-' * 30)

#-------------------------------
#Intermediate Level Examples
#-------------------------------

# Example 5: Using break inside nested loops
for i in range(1, 4):
    for j in range(1, 4):
        if j == 2:
            break
        print(f"i={i}, j={j}")
# Output: (i, j) pairs where j is never 2

print('-' * 30)

# Example 6: Using continue to filter even numbers
evens = []
for i in range(1, 11):
    if i % 2 != 0:  # odd number
        continue
    evens.append(i)
print("Even numbers from 1 to 10:", evens)

print('-' * 30)

# Example 7: Using break to search in a list
names = ['Anna', 'Bob', 'Charlie', 'David']
search = 'Charlie'
found = False
for name in names:
    if name == search:
        found = True
        print(f"{search} found!")
        break
if not found:
    print(f"{search} not found.")

print('-' * 30)

# Example 8: Skipping multiples of 3 in a range
for n in range(1, 10):
    if n % 3 == 0:
        continue
    print(n, end=" ")  # Output: 1 2 4 5 7 8
print()

print('-' * 30)

#---------------------------------
#Advanced Level Concepts/Examples
#---------------------------------

# Example 9: Using break with loops-else
for num in range(2, 10):
    for divisor in range(2, num):
        if num % divisor == 0:
            print(f"{num} equals {divisor} * {num // divisor}")
            break
    else:
        print(f"{num} is a prime number")
# Shows how break prevents else from running

print('-' * 30)

# Example 10: Ignoring user input until special word
while True:
    entry = input("Type 'exit' to stop: ")
    if entry == 'exit':
        print("Goodbye!")
        break
    elif entry.strip() == '':
        continue  # ignore empty input
    else:
        print(f"You typed: {entry}")

# (Commented out above interactive code if running automatically)
# Remove comment to test interactively

# print('-' * 30)

# Example 11: Filtering and collecting (skip, stop logic)
nums = [10, -2, 0, 13, -5, 7, 99, -1]
positives = []
for n in nums:
    if n < 0:
        continue  # skip negative numbers
    if n > 50:
        break    # stop if number > 50 encountered
    positives.append(n)
print("Collected positives until >50 encountered:", positives)

print('-' * 30)

# Example 12: Using continue in nested loops
matrix = [
    [1, 2, 0],
    [0, 3, 4],
    [5, 0, 6]
]
for row in matrix:
    for value in row:
        if value == 0:
            continue
        print(value, end=' ')
# Output: Prints all non-zero values in matrix

print('\n' + '-' * 30)

# ---------------------
# Mini-Project Example
# ---------------------
# Project: Simulate a product search with skip and stop features

products = [
    {"name": "Laptop", "price": 800},
    {"name": "Mobile", "price": 300},
    {"name": "Headphones", "price": 0},        # Unavailable
    {"name": "Monitor", "price": 210},
    {"name": "Keyboard", "price": 0},          # Unavailable
    {"name": "Premium Laptop", "price": 1600}, # Too expensive!
    {"name": "Mouse", "price": 50}
]

print("Affordable products with available stock (prices <$1000):")
for product in products:
    if product['price'] == 0:
        # skip unavailable product
        continue
    if product['price'] > 1000:
        # stop search if product too expensive
        print("Found an item over budget; ending search.")
        break
    print(f"{product['name']}: ${product['price']}")

'''
---------------------------------------------------------------
Python Break and Continue Interview Questions and Answers
---------------------------------------------------------------

Q1: What is the difference between `break` and `continue` in Python loops?
A1: 
`break` immediately terminates the nearest enclosing loop (for or while), and control moves to the statement after the loop. 
`continue` skips the rest of the current iteration and moves to the next iteration of the loop.

Example:
for i in range(5):
    if i == 2:
        break
    print(i)
# Prints 0 1

for i in range(5):
    if i == 2:
        continue
    print(i)
# Prints 0 1 3 4

---------------------------------------------------------------

Q2: How does `break` interact with loop-else clauses?
A2:
If a loop is terminated by a `break`, the `else` block is not executed. If it terminates naturally (not via `break`), the `else` runs.

Example:
for n in [1, 2, 3]:
    if n == 2:
        break
else:
    print("Completed without break")
# (No output from else)

for n in [1, 3, 5]:
    if n == 2:
        break
else:
    print("No break occurred")
# Output: "No break occurred"

---------------------------------------------------------------

Q3: Can you use `break`/`continue` inside nested loops? How do they work?
A3:
Yes, but `break` and `continue` only affect the innermost loop in which they are used. 

Example:
for i in range(3):
    for j in range(3):
        if j == 1:
            break
        print(f"i={i}, j={j}")
# For each i, j only prints for j=0

---------------------------------------------------------------

Q4: Real-time: Write a code snippet to process numbers, ignoring negatives (using continue) and stopping at the first number above 100 (using break).
A4:
nums = [2, -5, 13, 55, 106, 7, 8]
for n in nums:
    if n < 0:
        continue
    if n > 100:
        break
    print(n)
# Output: 2 13 55

---------------------------------------------------------------

Q5: What are the consequences of using `break` in a loop when searching for an element?
A5:
- If found, `break` stops further search (efficient).
- It's often used with a flag or with a loop-else to check if the item was never found.

Example:
search = "foo"
lst = ["bar", "baz", "foo", "qux"]
for x in lst:
    if x == search:
        print("Found!")
        break
else:
    print("Not found!")
# Output: Found!

---------------------------------------------------------------

Q6: Can you use `break`/`continue` in a `try-except` block inside a loop? Explain with example.
A6:
Yes. The `break`/`continue` can be used in a try block inside a loop, but they must remain inside the loop's scope.

Example:
for x in [1, 0, 2]:
    try:
        print(10 // x)
    except ZeroDivisionError:
        print("Zero! Skipping.")
        continue
# Output: 10, "Zero! Skipping.", 5

---------------------------------------------------------------

Q7: Deep—What happens if you use both `break` and `continue` in a single iteration? How do you design logic around it?
A7:
If `break` is executed, the loop terminates immediately—`continue` code won’t run after a `break`. Only the first encountered will run. 
Typical design is to use exclusive `if...elif...` blocks.

Example:
for i in range(5):
    if i == 2:
        break
    elif i % 2 == 0:
        continue
    print(i)
# Output: Only 1

---------------------------------------------------------------

Q8: Discuss a pitfall when using `continue` in while loops regarding loop control variables.
A8:
If the continue statement means your increment or update statement is skipped, the loop may never terminate (infinite loop risk).

Bad Example:
i = 0
while i < 5:
    if i == 2:
        continue    # i never increments at i==2, so stuck forever
    print(i)
    i += 1

# Correct: always carefully update loop control variable.

Q9: Can you use break and continue within list comprehensions, lambda, or generator expressions?
A9:
No, `break`/`continue` are only valid in for or while loops, not in comprehensions or lambdas. Use conditional logic instead inside comprehensions.

Example:
# Instead of break/continue:
[x for x in range(10) if x%2==0]  # filters evens; can't use break/continue inside

---------------------------------------------------------------

Q10: Can you simulate break or continue effect in a function with return or similar? Give example.
A10:
Yes, in functions inside loops, `return` can immediately exit the function (like break the whole loop enclosing it if called in main logic),
and `continue`-like effect can be made by returning/`pass` in functions called within loop bodies.

Example:
def process(x):
    if x < 0:
        return  # Simulating continue
    print(x)

for n in [1, -2, 3]:
    process(n)
# Output: 1, 3

---------------------------------------------------------------
'''
