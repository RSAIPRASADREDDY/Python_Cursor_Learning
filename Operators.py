# --- Python Operators: Concepts, Syntax, Examples, Mini-Project, and Interview Q&A ---

# Definition:
# In Python, an "operator" is a special symbol or keyword that is used to perform operations
# on values or variables. Operators are the constructs which can manipulate the value of operands.

# --- Types of Operators in Python ---
# 1. Arithmetic Operators:        +, -, *, /, %, //, **
# 2. Comparison/Relational:       ==, !=, >, <, >=, <=
# 3. Assignment Operators:        =, +=, -=, *=, /=, //=, %=, **=
# 4. Logical Operators:           and, or, not
# 5. Bitwise Operators:           &, |, ^, ~, <<, >>
# 6. Membership Operators:        in, not in
# 7. Identity Operators:          is, is not

# --- Syntax ---
# operator usage depends on type, for example:
a = 10
b = 5
print(a + b)      # Arithmetic: addition
print(a > b)      # Comparison: greater than
a += 2            # Assignment: add then assign
print(a)
print(a == b)     # Comparison: equal to
print(a is b)     # Identity: same object?
lst = [1, 2, 3]
print(2 in lst)   # Membership

# --- Beginner Level Examples ---

# 1. Arithmetic Operators
x = 12
y = 4
print("x + y =", x + y)
print("x - y =", x - y)
print("x * y =", x * y)
print("x / y =", x / y)      # division (float result)
print("x % y =", x % y)      # modulus
print("x // y =", x // y)    # integer division
print("x ** y =", x ** y)    # exponentiation


# 2. Comparison Operators
print("x == y:", x == y)
print("x != y:", x != y)
print("x > y:", x > y)
print("x < y:", x < y)
print("x >= y:", x >= y)
print("x <= y:", x <= y)

# 3. Assignment Operators
val = 7
val += 3    # val = val + 3
print("val after += 3:", val)
val *= 2
print("val after *= 2:", val)
val //= 4
print("val after //= 4:", val)

# 4. Logical Operators
a = True
b = False
print("a and b:", a and b)
print("a or b:", a or b)
print("not a:", not a)


# --- Intermediate Level Examples ---

# 5. Bitwise Operators (operate on bits)
p = 5        # 0b0101
q = 3        # 0b0011
print("p & q (AND):", p & q)          # 1
print("p | q (OR):", p | q)           # 7
print("p ^ q (XOR):", p ^ q)          # 6
print("~p (NOT):", ~p)                # -6 (inverts all bits)
print("p << 1 (left shift):", p << 1) # 10 (shift bits left)
print("q >> 1 (right shift):", q >> 1) # 1
# Bitwise operators perform operations on the binary (bit-level) representations of integers.
# Common ones: & (AND), | (OR), ^ (XOR), ~ (NOT), << (left shift), >> (right shift)
# Example: 5 & 3 -> 0b0101 & 0b0011 = 0b0001 (which is 1)



# 6. Membership Operators
char_list = ['a', 'b', 'c']
print("'a' in char_list?", 'a' in char_list)
print("'d' not in char_list?", 'd' not in char_list)

# 7. Identity Operators
foo = [1, 2, 3]
bar = foo
baz = [1, 2, 3]
print("foo is bar:", foo is bar)     # True (same object)
print("foo is baz:", foo is baz)     # False (same content, different objects)
print("foo == baz:", foo == baz)     # True (values are equal)

# --- Advanced Level Examples: Combining Operators ---

# Chained comparisons
n = 8
print(5 < n < 10)  # True; equivalent to (5 < n) and (n < 10)

# Using arithmetic with assignment
result = 2
result **= 6   # result = result ** 6
print("result after exponent assignment:", result)

# Bitwise not with masks
mask = 0b1111
data = 0b1010
print("Data after masking (data & mask):", data & mask)

# Combining logical, membership, and comparison operators
names = ['alice', 'bob', 'carol']
name = "bob"
if name in names and len(name) == 3:
    print("Accepted name:", name)

# --- Mini Project: Operator Practice Console ---

def operator_practice_console():
    print("\n--- Welcome to the Python Operator Practice Console ---")

    # User enters two numbers for arithmetic practice
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print(f"{a} + {b} = {a + b}")
    print(f"{a} - {b} = {a - b}")
    print(f"{a} * {b} = {a * b}")
    print(f"{a} / {b} = {a / b if b != 0 else 'undefined (div by 0)'}")
    print(f"{a} ** {b} = {a ** b}")

    # Now, comparison example
    print("\nComparison:")
    print(f"{a} == {b}? {'Yes' if a == b else 'No'}")
    print(f"{a} > {b}? {'Yes' if a > b else 'No'}")

    # Logical operation practice
    is_even = (a % 2 == 0) and (b % 2 == 0)
    print(f"Are both numbers even? {'Yes' if is_even else 'No'}")

    # Membership - check if a letter is in a string
    s = input("\nEnter a word: ")
    c = input("Enter a character to check if it's in the word: ")
    print(f"Is '{c}' in '{s}'?", c in s)

    # Identity - check if two small objects are the same object
    print("\nIdentity Check:")
    x = 5
    y = 5
    print("x is y:", x is y)
    lst1 = [1,2]
    lst2 = [1,2]
    print("lst1 is lst2:", lst1 is lst2)
    print("lst1 == lst2:", lst1 == lst2)

# Uncomment to run the mini project:
# if __name__ == "__main__":
#     operator_practice_console()

'''
    # --- Interview Q&A: Python Operators ---

    Q: What is an operator in Python?
    A: An operator is a symbol or keyword that performs an operation on one or more operands.

    Q: What are the major types of operators in Python?
    A: Arithmetic, Comparison, Assignment, Logical, Bitwise, Membership, and Identity operators.

    Q: What is the difference between '==' and 'is'?
    A: '==' checks for value equality, while 'is' checks whether two variables refer to the same object in memory.

    Q: How do logical operators work in Python?
    A: 'and' returns True if both operands are True, 'or' returns True if at least one is True, and 'not' negates the logical value.

    Q: What does the // operator do?
    A: '//' performs floor division, returning the largest integer less than or equal to the result.

    Q: How can you chain comparison operators?
    A: Python allows expressions like 3 < x < 7, equivalent to (3 < x) and (x < 7).

    Q: Give an example of a bitwise operator and its usage.
    A: The '&' operator does a bitwise AND, e.g. 5 & 3 gives 1, since 0b0101 & 0b0011 = 0b0001.

    Q: How is the 'in' operator used?
    A: 'in' checks for membership, e.g. 'a' in ['a', 'b'] returns True.

    Q: What happens if you divide by zero with '/' or '//' or '%'?
    A: Python raises ZeroDivisionError.

    Q: Can you override the behavior of operators?
    A: Yes, by defining special methods in classes, e.g. __add__ for '+', __eq__ for '=='.

'''
