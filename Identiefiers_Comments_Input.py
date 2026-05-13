# --- Beginner Level: Identifiers, Comments & Input ---

# Identifiers: naming rules and conventions

name = "Alice"           # Valid identifier
age1 = 30                # Valid (can have numbers, but not start with one)
_user_city = "Chennai"   # Valid (can start with underscore)
# 2nd_place = "Runner-up"  # Invalid, uncomment to see error: cannot start with digit

# Comments: single-line, inline, and block
# This is a single-line comment

height = 160  # Inline comment: height in centimeters

'''
This is a block comment
or multi-line string sometimes used as a comment
but officially comments use the '#' character.
'''

# Input: Take user input from the console
user_name = input("Enter your name: ")
print("Hello,", user_name)


# --- Intermediate Level: Identifiers, Comments & Input ---

# Identifier conventions
student_name = "Raj"         # snake_case (common for variables)
StudentID = 101              # CamelCase (sometimes used, but snake_case preferred)
__private_val = 42           # Double underscore, often for internal use in classes

# Special identifiers (not for variables)
# for, if, def, class, etc. are keywords and NOT valid as identifiers

# Proper use of descriptive comments
# Calculate area of a circle
radius = float(input("Enter circle radius: "))
area = 3.14159 * radius ** 2
print("Area of circle:", area)  # Output area

# Multi-line comment to explain next code block
'''
The next section asks for two numbers from the user,
adds them together, and prints the sum.
'''
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("Sum is:", num1 + num2)


# --- Advanced Level: Identifiers, Comments & Input ---

# Using input, type conversion, and identifier best practices
def get_int_input(prompt):
    """Request integer input from the user, with validation."""
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Please enter a valid integer.")

first_value = get_int_input("Enter an integer: ")
second_value = get_int_input("Enter another integer: ")
print("Product is:", first_value * second_value)

# Idiosyncratic identifier: Using underscore _ as a temporary value (accepted by convention)
for _ in range(2):
    print("Loop iteration with throwaway variable _.")

# Using comments to temporarily disable code
# print("This line is commented and will not execute")

# DOCSTRING as a documentation comment (for functions/classes/modules)
def greet(person):
    """Greets the person whose name is provided as an argument."""
    print(f"Hello, {person}!")

greet("Pranav")

# --- Mini Project: Simple Student Grading System ---

"""
This mini project demonstrates identifiers, comments, input, type conversion,
output, and documentation in Python.

The program asks for a student's name, roll number, and marks in three subjects,
calculates the total and average, and prints the result with proper formatting.
"""

def get_float_input(prompt):
    """Request a float input from the user with validation."""
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Enter a valid number (decimal allowed).")

def main():
    # Student basic info input
    name = input("Enter student's name: ")  # Always a string
    roll_number = input("Enter roll number: ")  # Could be string or int

    # Marks input (converted to float for precision)
    marks_subject1 = get_float_input("Enter marks for Subject 1: ")
    marks_subject2 = get_float_input("Enter marks for Subject 2: ")
    marks_subject3 = get_float_input("Enter marks for Subject 3: ")

    # Calculate total and average
    total = marks_subject1 + marks_subject2 + marks_subject3  # float addition
    average = total / 3

    # Assign grade based on average mark
    if average >= 90:
        grade = "A+"
    elif average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "F"
    
    # Output formatted student result
    print("\n#--- Student Report ---#")
    print(f"Name       : {name}")
    print(f"Roll No    : {roll_number}")
    print(f"Subjects   : {marks_subject1}, {marks_subject2}, {marks_subject3}")
    print(f"Total Marks: {total}")
    print(f"Average    : {average:.2f}")
    print(f"Grade      : {grade}")

# Uncomment the next line to run the mini-project directly
if __name__ == "__main__":
    main()


'''
    # --- Interview Q&A: Identifiers, Comments & Input in Python ---

    Q: What is an identifier in Python?
    A: An identifier is a name given to variables, functions, classes, etc. It must start with a letter or underscore, followed by letters, digits, or underscores.

    Q: Can you use Python keywords as identifiers?
    A: No, keywords like 'for', 'if', 'class', etc. cannot be used as identifiers.

    Q: Explain the different types of comments in Python.
    A: Single-line comments use '#', block comments use multiple '#' lines, and multi-line strings #('') 
    can be used as documentation or block comments.
'''
'''
    Q: What is the recommended style for naming variables?
    A: Use lowercase letters with underscores (snake_case) for variables and functions by convention.

    Q: How do you take input from a user in Python, and what is its default type?
    A: Use the input() function. The value returned is always a string; you must convert it to int/float if needed.

    Q: What happens if you try to use an identifier starting with a number?
    A: Python will raise a SyntaxError since identifiers can't start with digits.

    Q: Is '_' (underscore) a valid identifier? How is it commonly used?
    A: Yes, '_' is valid and often used for temporary variables or to indicate 'I don't care about this value'.

    Q: Can comments appear on the same line as Python statements?
    A: Yes, anything after '#' on a line is ignored by Python and acts as a comment.

    Q: What is a docstring and how does it differ from a regular comment?
    A: A docstring is a string literal placed right after the definition of a function/class/module and is used for documentation; regular comments use '#'.

    Q: Why should you write comments in your code?
    A: Comments help explain what the code does, making it easier for others (and yourself) to understand and maintain the code in the future.

'''
