
# --- Beginner Level: Basic Type Conversion ---

# Converting int to float
num = 10
num_float = float(num)
print(f"Integer: {num}, as float: {num_float}")

# Converting float to int (truncates the decimal part)
decimal = 19.99
decimal_int = int(decimal)
print(f"Float: {decimal}, as int: {decimal_int}")

# Converting int to str
count = 5
count_str = str(count)
print(f"Integer: {count}, as string: '{count_str}'")

# Converting bool to int
flag = True
flag_int = int(flag)
print(f"Boolean: {flag}, as int: {flag_int}")



# --- Intermediate Level: Converting Between Types and Handling Errors ---

# Converting str to int (when possible)
s = "42"
s_int = int(s)
print(f"String: '{s}', as int: {s_int}")

# Attempting invalid conversion (uncomment to see error)
#invalid_s = "abc"
#invalid_int = int(invalid_s)  # ValueError

# Converting input (always string) to other types
user_age_str = "23"
user_age = int(user_age_str)
print(f"User age string: '{user_age_str}', as int: {user_age}")

# Using bool() to evaluate truthiness
empty_string = ""
print(f"Empty string as bool: {bool(empty_string)}")
zero_num = 0
print(f"Zero as bool: {bool(zero_num)}")
nonzero_num = 7
print(f"Nonzero number as bool: {bool(nonzero_num)}")

# Converting between list, tuple, and set
numbers_list = [1, 2, 2, 3]
numbers_set = set(numbers_list)
print(f"List: {numbers_list}, as set (unique values): {numbers_set}")
numbers_tuple = tuple(numbers_list)
print(f"List: {numbers_list}, as tuple: {numbers_tuple}")



# --- Advanced Level: Custom Conversion and Type Checking ---

# Using isinstance() before conversion
data = "123"
if isinstance(data, str):
    data_num = int(data)
    print(f"Converted '{data}' (str) to {data_num} (int) safely")

# Automatic type conversion in expressions
result = 10 + 3.5  # int + float -> float
print(f"10 (int) + 3.5 (float) = {result} ({type(result)})")

# Converting dictionary keys & values to list
my_dict = {"a": 1, "b": 2}
keys_list = list(my_dict.keys())
values_list = list(my_dict.values())
print(f"Dict: {my_dict}, keys as list: {keys_list}, values as list: {values_list}")

# Custom conversion function
def to_int_safe(val):
    try:
        return int(val)
    except (ValueError, TypeError):
        return None

tests = ["123", "abc", 45.6, None]
for t in tests:
    print(f"Value: {t}, to_int_safe: {to_int_safe(t)}")

# Using map() for batch conversion
str_numbers = ["10", "20", "30"]
int_numbers = list(map(int, str_numbers))
print(f"str_numbers: {str_numbers}, converted to ints: {int_numbers}")


# --- Mini Project: Simple Data Entry & Conversion Dashboard ---

"""
Mini project: Data Entry & Conversion Dashboard

Demonstrates type conversion, input, and validation for beginner/intermediate learners.
"""

def get_number(prompt, number_type=float):
    """Safely get a number (int or float) from user input."""
    while True:
        inp = input(prompt)
        try:
            return number_type(inp)
        except ValueError:
            print(f"Please enter a valid {number_type.__name__} value.")

def get_bool(prompt):
    """Get boolean input from user: yes/y/true/1 means True, else False."""
    val = input(prompt).strip().lower()
    return val in ['yes', 'y', 'true', '1']

def main():
    print("#--- Data Entry & Conversion Dashboard ---#")

    name = input("Enter your name: ")
    age = get_number("Enter your age: ", int)
    height = get_number("Enter your height in cm: ", float)
    is_student = get_bool("Are you a student? (yes/no): ")

    # Store all in a dict
    profile = {
        "name": name,
        "age": age,
        "height": height,
        "is_student": is_student
    }

    print("\n#--- Profile Entered ---#")
    print(f"Raw data: {profile}")
    print("Types per field:")
    for k, v in profile.items():
        print(f"  {k}: {v} -> {type(v)}")

    # Type conversions demonstration
    print("\n#--- Type Conversion Demos ---#")
    age_str = str(age)
    print(f"Age as string: '{age_str}' (type: {type(age_str)})")
    height_int = int(height)
    print(f"Height as integer: {height_int} (type: {type(height_int)})")
    student_str = str(is_student)
    print(f"is_student as string: '{student_str}' (type: {type(student_str)})")

    # List/Tuple/Set demo with hobbies
    hobbies_raw = input("Enter some hobbies (comma-separated): ")
    hobbies_list = [h.strip() for h in hobbies_raw.split(",") if h.strip()]
    hobbies_set = set(hobbies_list)
    hobbies_tuple = tuple(hobbies_list)
    print(f"\nHobbies as list: {hobbies_list}")
    print(f"Hobbies as set (unique only): {hobbies_set}")
    print(f"Hobbies as tuple: {hobbies_tuple}")

    # Safe string-to-int conversion for challenge
    fav_num_str = input("Enter your favorite number (as string): ")
    try:
        fav_num = int(fav_num_str)
        print(f"Converted to int: {fav_num}")
    except ValueError:
        print(f"'{fav_num_str}' is not a valid integer!")

    # Bool conversion trap
    answer = input("Type the word 'False' and see what bool('False') is: ")
    print(f"bool('{answer}') --> {bool(answer)} (remember, any non-empty string is True!)")

if __name__ == "__main__":
    main()

'''
    # --- Interview Q&A: Type Conversion in Python ---

    Q: What is type conversion in Python?
    A: Type conversion is the process of changing the data type of a variable or value, for example converting an integer to a float, or a string to an integer.

    Q: What are the two kinds of type conversion in Python?
    A: Implicit (automatic) and explicit (manual). Implicit happens when Python converts types in expressions automatically; explicit is when you use functions like int(), float(), str(), etc.

    Q: What happens if you try to convert a string with non-numeric characters to int?
    A: Python raises a ValueError.

    Q: How can you safely convert a string to an int if you're not sure about its content?
    A: Use a try-except block to handle potential ValueError (and TypeError) during conversion.

    Q: Does bool('False') return False? Why or why not?
    A: No, bool('False') returns True because non-empty strings are always True in Python, regardless of their content.

    Q: Can you convert a list to a set? What happens to duplicate items?
    A: Yes, you can. Duplicates are removed because sets only contain unique items.

    Q: Give an example of implicit type conversion in Python.
    A: When you add int and float (e.g., 5 + 2.0), Python converts int to float automatically, resulting in 7.0.

    Q: How do you convert a dictionary's keys to a list?
    A: Use list(my_dict.keys()).

    Q: Is it always safe to convert data between types?
    A: No, converting incompatible types (like 'abc' to int) raises exceptions. Always ensure proper type and value before conversion.
'''

