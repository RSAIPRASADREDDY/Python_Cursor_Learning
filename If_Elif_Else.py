"""
Python Conditional Statements: if, elif, else
---------------------------------------------

Definition:
-----------
Conditional statements in Python are used to control the flow of execution based on conditions (expressions that evaluate to True or False). They allow a program to make decisions, executing code blocks selectively.

Key Methods/Keywords:
---------------------
- if       : Used to check a condition
- elif     : (short for "else if") Check additional conditions if previous ones are False
- else     : Executes if all previous conditions are False
- Nested if: Placing if/elif/else inside another if block

Syntax:
-------
if condition1:
    # block executed if condition1 is True
elif condition2:
    # block executed if condition1 is False and condition2 is True
else:
    # block executed if all conditions above are False

# You can use as many elif blocks as needed.
"""

# -----------------------------------------------
# Beginner Level Examples
# -----------------------------------------------

# Simple if statement
num = 10
if num > 5:
    print(f"{num} is greater than 5")  # Output: 10 is greater than 5

# if-else example
age = 17
if age >= 18:
    print("You can vote!")
else:
    print("You are under 18.")  # Output: You are under 18.

# if-elif-else example
marks = 75
if marks >= 90:
    print("A Grade")
elif marks >= 80:
    print("B Grade")
elif marks >= 70:
    print("C Grade")  # Output: C Grade
else:
    print("D Grade")


# -----------------------------------------------
# Intermediate Level Examples
# -----------------------------------------------

# Multiple elif conditions
num = 0
if num > 0:
    print("Positive")
elif num == 0:
    print("Zero")   # Output: Zero
else:
    print("Negative")

# Checking membership
fruits = ['apple', 'banana', 'cherry']
item = 'banana'
if item in fruits:
    print(f"{item} is in the list.")    # Output: banana is in the list.
else:
    print(f"{item} is not in the list.")

# Combining conditions with and/or
a, b = 12, 5
if a > 10 and b < 10:
    print("a > 10 and b < 10")          # Output: a > 10 and b < 10

# Nested if statements
x = 13
if x > 0:
    print("x is positive")
    if x % 2 == 0:
        print("x is even")
    else:
        print("x is odd")               # Output: x is positive \n x is odd

# -----------------------------------------------
# Advanced Level Examples
# -----------------------------------------------

# Nested if-elif with user input (commented out for direct execution)
# user_input = int(input("Enter a number: "))
# if user_input == 0:
#     print("Zero")
# elif user_input > 0:
#     if user_input % 2 == 0:
#         print("Positive Even")
#     else:
#         print("Positive Odd")
# else:
#     print("Negative")

# Short-hand if (single line)
status = "PASS" if marks >= 40 else "FAIL"
print(status)    # Output: PASS (since marks=75 above)

# Multiple conditions in one line (all true/any true)
x, y, z = 5, 10, 15
if x < y < z:
    print("x < y < z")          # Output: x < y < z

# Use with collections & checks
person = {'name': 'Sai', 'age': 21}
if 'name' in person and person['age'] > 18:
    print(f"{person['name']} is an adult.")   # Output: Sai is an adult.

# Ternary operator (conditional expression)
odd_even = "Even" if x % 2 == 0 else "Odd"
print(odd_even)        # Output: Odd

# -----------------------------------------------
# Mini Project: Simple ATM-like Menu with Conditionals
# -----------------------------------------------

def simple_atm():
    print("=== Welcome to Simple ATM ===")
    balance = 1000
    while True:
        print("\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. Exit")
        choice = input("Select option (1-4): ")
        if choice == '1':
            print(f"Your balance: {balance}")
        elif choice == '2':
            amount = float(input("Enter amount to deposit: "))
            if amount > 0:
                balance += amount
                print(f"Deposited. New balance: {balance}")
            else:
                print("Invalid deposit amount.")
        elif choice == '3':
            amount = float(input("Enter amount to withdraw: "))
            if amount > balance:
                print("Insufficient funds.")
            elif amount <= 0:
                print("Invalid withdraw amount.")
            else:
                balance -= amount
                print(f"Withdrawn. New balance: {balance}")
        elif choice == '4':
            print("Thank you for using ATM. Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

# Uncomment below to run the miniproject
# simple_atm()

'''
--------------------------------------------------------------------
INTERVIEW QUESTIONS & ANSWERS (PYTHON CONDITIONAL STATEMENTS)
--------------------------------------------------------------------

Q1: What is the difference between if, elif, and else? When is each used?
A1:
- if: Checks the FIRST condition. If True, executes its block.
- elif: Checks subsequent conditions if previous ones were False.
- else: Executes if all preceding conditions were False.
Example:
x = 5
if x > 10:
    print("Big")
elif x > 0:
    print("Small Positive")   # This runs for x=5
else:
    print("Zero or Negative")

Q2: Can you have multiple elif in a conditional chain? What gets executed?
A2: Yes, you can have multiple elif. Python checks them top to bottom; only the FIRST match executes, then control exits the chain.

Q3: Explain the difference between nested if statements and chained elifs.
A3:
- Nested if: One if inside another. Useful for checking "if this AND if-that" with blocks inside blocks.
- Chained elif: Multiple separate conditions at the same indentation.
Example:
age = 21
if age > 18:
    if age < 65:
        print("Adult but not senior")
    else:
        print("Senior")
elif age == 18:
    print("Just turned adult")
else:
    print("Minor")

Q4: How do logical operators (and, or, not) interact with conditionals?
A4:
They combine/complement multiple conditions.
- and: Both must be True
- or: Any one True is enough
- not: Reverses condition (True <-> False)
Example:
x = 8
if x > 0 and x % 2 == 0:
    print("Positive Even")  # This runs

Q5: How would you perform an action only if a variable exists in a dictionary *and* its value is in a list?
A5:
d = {'name': 'Amy', 'city': 'Mumbai'}
cities = ['Delhi', 'Mumbai']
if 'city' in d and d['city'] in cities:
    print("The city is allowed.")   # Output: The city is allowed.

Q6: What is a ternary conditional (conditional expression)? Where is it used?
A6:
- Syntax: <result_if_true> if <condition> else <result_if_false>
Used for compact "if/else" in a single line, usually for assignment or return.
Example:
num = 7
parity = "Even" if num % 2 == 0 else "Odd"
print(parity)  # Odd

Q7: What happens if no else is given and no if/elif condition matches?
A7:
Nothing happens; program just continues to next statement. No error.

Q8: Can you use conditionals inside list comprehensions? Give an example.
A8:
Yes! Very powerful.
Example:
evens = [x for x in range(10) if x % 2 == 0]  # [0,2,4,6,8]

Q9: How do you avoid deeply nested ifs (the so-called "arrow code")?
A9:
- Use elif chains where possible.
- Use guard clauses (early returns in functions).
- Sometimes break complex logic into functions.

Q10: Give a real-world scenario: You have to assign ticket prices based on age: 0-12 (child), 13-59 (adult), 60+ (senior). Implement with conditionals.
A10:
def price_for_age(age):
    if age <= 12:
        return "Child Price"
    elif age <= 59:
        return "Adult Price"
    else:
        return "Senior Citizen Price"

print(price_for_age(7))   # Child Price
print(price_for_age(25))  # Adult Price
print(price_for_age(61))  # Senior Citizen Price

--------------------------------------------------------------------
'''
