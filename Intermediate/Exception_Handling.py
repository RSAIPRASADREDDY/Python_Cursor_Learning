"""
Exception Handling in Python: Concepts, Methods, Syntax, Examples, Mini-project, and Interview Q&A

Definition:
-----------
Exception handling in Python enables developers to gracefully respond to errors (exceptions) during runtime, 
keeping programs robust and preventing crashes. Python uses try, except, else, finally, 
and raise statements for error handling.

Common Methods / Statements:
---------------------------
- try         : Block of code to attempt (may raise error)
- except      : Block to handle specific (or all) exceptions
- else        : Executes if no exceptions are raised in try
- finally     : Always executes, whether exception occurred or not
- raise       : Explicitly trigger an exception

Syntax:
-------
try:
    # Code that may raise error
except ExceptionType1:
    # Handling for type 1
except ExceptionType2 as e:
    # Handling (e is the exception object)
else:
    # Executes if no exception in try block
finally:
    # Executes always (cleanup code)
"""


# -----------------------------------------------
# Beginner Level Examples
# -----------------------------------------------

# Example 1: Handling ZeroDivisionError

try:
    result = 10 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")


# Example 2: Handling Multiple Exceptions

try:
    #num = int(input("Enter a number: "))
    num = 0
    inv = 10 / num
except ValueError:
    print("That's not a valid integer.")
except ZeroDivisionError:
    print("Number cannot be zero.")
else:
    print(f"Result is {inv}")


# Example 3: Using finally

try:
    file = open('somefile.txt', 'r')
    content = file.read()
except FileNotFoundError:
    print("File not found.")
finally:
    print("This block always executes.")
    if 'file' in locals():
        file.close()




# -----------------------------------------------
# Intermediate Level Examples
# -----------------------------------------------

# Example 4: Catching All Exceptions (not always recommended)

try:
    val = int("10.8")
 
except Exception as e:
    print("Some error occurred:", e)


# Example 5: Accessing Exception Arguments

try:
    lst = [1, 2, 3]
    print(lst[8])
except IndexError as error:
    print("IndexError details:", error)


# Example 6: Using else with try/except

try:
    #age = int(input("Enter age: "))
    age = 0
    pass
except ValueError:
    print("Enter a valid number for age.")
else:
    print("Age accepted:", age)


# -----------------------------------------------
# Advanced Level Examples
# -----------------------------------------------

# Example 7: Custom Exception Classes

class NegativeNumberError(Exception):
    """Raised when a negative number is encountered."""
    pass

def sqrt(num):
    if num < 0:
        raise NegativeNumberError("Cannot take sqrt of negative number!")
    return num ** 0.5

try:
    print(sqrt(5))
except NegativeNumberError as e:
    print("Custom Exception caught:", e)


# Example 8: Nested Exception Handling

try:
    x = int(input("Numerator: "))
    y = int(input("Denominator: "))
    try:
        print("Result:", x / y)
    except ZeroDivisionError:
        print("You tried to divide by zero.")
except ValueError:
    print("Entered value is not an integer.")



# Example 9: Raising Exceptions Manually

def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("Insufficient balance.")
    return balance - amount

try:
    print(withdraw(100, 200))
except ValueError as err:
    print("Withdraw failed:", err)


# -----------------------------------------------
# Mini-Project: Simple Calculator with Exception Handling
# -----------------------------------------------

def calculator():
    print("--- Simple Calculator (with Exception Handling) ---")
    while True:
        try:
            n1 = float(input("Enter first number: "))
            op = input("Enter operator (+, -, *, /): ").strip()
            n2 = float(input("Enter second number: "))

            if op == '+':
                result = n1 + n2
            elif op == '-':
                result = n1 - n2
            elif op == '*':
                result = n1 * n2
            elif op == '/':
                if n2 == 0:
                    raise ZeroDivisionError("Division by zero not allowed.")
                result = n1 / n2
            else:
                raise ValueError("Invalid operator.")
        except ValueError as ve:
            print(f"Value error: {ve}")
        except ZeroDivisionError as zde:
            print(f"Math error: {zde}")
        else:
            print(f"Result: {result}")
        finally:
            cont = input("Do you want to calculate again? (y/n): ").lower()
            if cont != 'y':
                print("Thank you for using the calculator!")
                break

# Uncomment below to run the mini-project
#calculator()

'''
-----------------------------------------------------
Python Exception Handling Interview Questions & Answers
-----------------------------------------------------

Q1: What's the difference between 'except Exception:' and 'except:'? When should each be used?
A1: 
- 'except Exception:' catches all standard exceptions (excluding SystemExit, KeyboardInterrupt, GeneratorExit). 
- 'except:' catches *all* exceptions, including system-exiting exceptions (which are normally best left uncaught). 
It's safer to use 'except Exception:' so as not to hide critical errors or interrupts.

Q2: Why use custom exception classes in Python, and how are they structured?
A2:
Custom exceptions allow you to signal application-specific errors, making error handling clearer and more maintainable.
Example:
class MyError(Exception):
    pass
try:
    raise MyError("Specific failure")
except MyError as e:
    print(e)

Q3: What happens if an exception occurs in both try and finally blocks? Which one is raised?
A3:
- If both try and finally raise exceptions, the exception from finally is the one propagated up, as it overrides the one from try.
Example:
try:
    raise ValueError("Try error")
finally:
    raise RuntimeError("Finally error")
# RuntimeError will be raised.

Q4: How can you ensure resources (like files or DB connections) are cleaned up even if an error occurs?
A4:
Use the 'finally' block or the 'with' context manager. 'finally' guarantees code runs regardless of exceptions. 'with' handles enter/exit automatically.
Example:
try:
    f = open("file.txt")
    # work
finally:
    f.close()

Or:
with open("file.txt") as f:
    # work

Q5: Write code that catches only a "division by zero" error, printing a custom message.
A5:
try:
    result = 10 / 0
except ZeroDivisionError:
    print("You tried dividing by zero.")

Q6: How would you implement retry logic on failure using exception handling?
A6:
import time
for i in range(3):
    try:
        res = 10 / int(input("Enter divisor: "))
        print("Result:", res)
        break
    except Exception as e:
        print("Failed:", e)
        time.sleep(1)  # brief wait
else:
    print("All retries used.")

Q7: Can you access the stack trace of an exception? How?
A7:
Yes, using the traceback module within the except block:
import traceback
try:
    1 / 0
except Exception:
    traceback.print_exc()

Q8: How do raise and assert differ?
A8:
- raise forces an exception (allows custom errors and manual error signaling).
- assert checks a condition and raises AssertionError if false (mainly debugging, often disabled in optimized runs).

# End of Interview Q&A
'''
