"""
Python For and While Loops: Concepts, Syntax, Examples, Mini-project, and Interview Q&A

Definition:
-----------
Loops are fundamental control flow statements that allow repeated execution of a block of code as long as a certain condition is met (while loop), or for each item in a sequence (for loop).

Types of Loops in Python:
------------------------
- For Loop: Iterates over elements of a sequence (list, tuple, string, dict, set, etc.).
- While Loop: Repeats a block as long as a condition is True.

Key Methods and Concepts:
-------------------------
- `range(start, stop [, step])`: Useful for iterating a fixed number of times.
- `break`: Exit the nearest enclosing loop prematurely.
- `continue`: Skip the rest of the code inside the current loop iteration.
- `else` clause (optional): Executed after the loop finishes (if not terminated by `break`).

Syntax:
-------
# For loop
for variable in iterable:
    # body

# While loop
while condition:
    # body

# For loop with else
for x in iterable:
    # body
else:
    # runs if not broken out of

# While loop with else
while condition:
    # body
else:
    # runs if not broken by break
"""

# -----------------------------------------------
# Beginner Level For and While Loop Examples
# -----------------------------------------------

# For loop over a list
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)  # apple\nbanana\ncherry

# For loop with range
for i in range(5):
    print(i)      # 0 1 2 3 4

# While loop with counter
count = 0
while count < 3:
    print("Count is", count)
    count += 1

# For loop over a string
for ch in "cat":
    print(ch.upper(), end=' ')
print()

# -----------------------------------------------
# Intermediate Level For and While Loop Examples
# -----------------------------------------------

# For loop with index using range(len())
names = ['Amy', 'Bob', 'Cat']
for i in range(len(names)):
    print(f"Index {i}: {names[i]}")

# While loop with break and continue
n = 10
while n > 0:
    n -= 1
    if n % 2 == 0:
        continue   # Skip even numbers
    if n == 3:
        break      # Stop at 3
    print(n, end=' ')  # 9 7 5

print()

# For loop with else clause
for x in range(3):
    print(x)
else:
    print("Loop finished without break.")

# Nested loops
for i in range(1, 4):
    for j in range(1, 4):
        print(i, "*", j, "=", i*j)
    print("-----")

# -----------------------------------------------
# Advanced Level For and While Loop Examples
# -----------------------------------------------

# Iterating through a dictionary
marks = {'Math': 90, 'Physics': 85, 'Chem': 92}
for subject, score in marks.items():
    print(f"{subject}: {score}")

# While loop for input validation
tries = 0
while True:
    pwd = input("Enter password (type 'quit' to stop): ")
    if pwd == 'quit':
        break
    if len(pwd) < 6:
        print("Too short!")
        tries += 1
        continue
    print("Password accepted!")
    break
print(f"Tries taken: {tries}")

# List comprehension with for (compact looping)
squares = [x*x for x in range(1, 6)]
print(squares)  # [1, 4, 9, 16, 25]

# Infinite loop and breaking on a condition
i = 0
while True:
    if i >= 5:
        print("Done!")
        break
    print(i)
    i += 1

# Looping with enumerate for index and value
colors = ['red', 'green', 'blue']
for idx, color in enumerate(colors):
    print(f"{idx}: {color}")

# -----------------------------------------------
# Mini-Project: Number Guessing Game with Loops
# -----------------------------------------------

def number_guessing_game():
    """A simple console number guessing game illustrating while and for loops."""
    import random
    number_to_guess = random.randint(1, 20)
    attempts_allowed = 5
    print("Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between 1 and 20. You have {attempts_allowed} attempts.")

    for attempt in range(1, attempts_allowed+1):
        guess = int(input(f"Attempt {attempt}. Enter your guess: "))
        if guess == number_to_guess:
            print(f"Correct! You guessed it in {attempt} attempts.")
            break
        elif guess < number_to_guess:
            print("Too low.")
        else:
            print("Too high.")
    else:
        print(f"Sorry! The number was {number_to_guess}.")

# Uncomment the line below to run the mini-project
# number_guessing_game()

'''
------------------------------------------------------------------
INTERVIEW QUESTIONS & ANSWERS (PYTHON LOOPS: FOR and WHILE)
------------------------------------------------------------------

Q1: How does Python’s for loop differ from C’s for loop? Give an example.
A1: In Python, the for loop iterates directly over items of a sequence, not using index-based counting unless you use range().
Example:
for item in [2, 4, 6]:
    print(item)

Q2: Explain the use of else clause in loops with an example.
A2: The else part of a for/while loop is executed only if the loop terminates normally (not by break).
for n in range(5):
    if n == 3:
        break
else:
    print("Completed!")    # This won't print because of break at n==3

Q3: What’s the purpose of continue and break in loops? Provide scenarios.
A3:
- continue skips the rest of the loop for the current iteration.
Example:
for i in range(5):
    if i % 2 == 0:
        continue
    print(i)  # prints only odd numbers

- break exits the nearest enclosing loop immediately.
Example:
while True:
    val = input("Type x to exit: ")
    if val == 'x':
        break

Q4: How can you loop over both index and value for a list in Python?
A4: Use `enumerate()`:
colors = ['red', 'blue']
for idx, color in enumerate(colors):
    print(idx, color)

Q5: Give a real-world example where a while loop is better than a for loop.
A5: When the number of iterations is not known beforehand, e.g., waiting for correct user input:
while True:
    entry = input("Enter password: ")
    if entry == 'secret':
        print("Access granted.")
        break

Q6: Can you nest for and while loops? Give a practical example.
A6: Yes.
Example: Printing a triangle of stars
for i in range(1, 5):
    j = 0
    while j < i:
        print('*', end='')
        j += 1
    print()

Q7: What happens if you modify the sequence you’re iterating over in a for loop?
A7: It may cause unexpected behavior or skipping elements. It's safer to iterate over a copy:
lst = [1, 2, 3]
for x in lst[:]:
    if x == 2:
        lst.remove(x)
# Resulting lst: [1, 3]

Q8: Describe how infinite loops are created and prevented with an example.
A8: An infinite loop occurs when the loop condition always remains True, e.g.,
while True:
    # do something
    if some_condition:
        break

Q9: Can else with loops be used to detect item not found? Show how.
A9: Yes.
nums = [1, 2, 3]
for n in nums:
    if n > 10:
        print("Found!")
        break
else:
    print("No number > 10 found.")

Q10: How would you iterate over two lists in parallel using a for loop?
A10: Use zip().
names = ['A', 'B']
scores = [90, 80]
for name, score in zip(names, scores):
    print(name, score)
------------------------------------------------------------------
'''
