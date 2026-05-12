"""Topic 01: variables


#def main() -> None:
name = "Sai"
count = 3
price = 19.99
active = True

print("Hello,", name)
print(type(name), type(count), type(price), type(active))

# Uncomment locally for interactive practice:
#user = input("Enter your city: ")
#print("You entered:", user)

# --- More examples: variable assignment and types ---
age = 25             # int
temperature = 36.6   # float
city = "Bangalore"   # str
is_student = False   # bool
empty_value = None   # NoneType

print(f"Age: {age}, Temperature: {temperature}, City: {city}, Student?: {is_student}, Empty: {empty_value}")
print(f"My name is {name}")
# Type checking and changing
print("Type of age:", type(age))
print("Type of temperature:", type(temperature))
print("Type of city:", type(city))
print("Type of is_student:", type(is_student))
print("Type of empty_value:", type(empty_value))

# Explicit conversion
age_str = str(age)
price_int = int(price)
active_str = str(active)
print(f"age_str: {age_str}, type: {type(age_str)}")
print(f"price_int: {price_int}, type: {type(price_int)}")
print(f"active_str: {active_str}, type: {type(active_str)}")

# Multiple assignment
x, y, z = 1, 2.0, "three"
print(f"x={x} ({type(x)}), y={y} ({type(y)}), z={z} ({type(z)})")

# Swapping variables (classic Python trick)
a, b = 10, 20
a, b = b, a
print(f"After swap: a={a}, b={b}")

# Variable overwrite and type change
thing = "apple"
print("thing (as str):", thing, type(thing))
thing = 42
print("thing (as int):", thing, type(thing))

# Using isinstance for type-safe code
value = "123"
if isinstance(value, str):
    num = int(value)
    print(f"Converted '{value}' (str) to {num} (int)")

# Example: Why types matter
value1 = "5"
value2 = "6"
print("String addition:", value1 + value2)   # Concatenates: '56'
print("Integer addition:", int(value1) + int(value2))  # Adds: 11





#if __name__ == "__main__":
 #   main()
# --- More Complex Concepts of Variables ---

# 1. Mutable vs Immutable Types
# Immutable types: int, float, str, tuple, bool, NoneType
a = 100
print("Before changing, a id:", id(a))
a = 200
print("After changing, a id (immutable):", id(a))  # id changes because int is immutable

# Mutable types: list, dict, set, etc.
my_list = [1, 2, 3]
print("Before change, my_list id:", id(my_list))
my_list.append(4)
print("After change, my_list id (mutable):", id(my_list))  # id stays same

# 2. Variable Scope (Global vs Local)
msg = "Global variable" 

def test_scope():
    msg = "Local variable" 
    print("Inside function:", msg) 

test_scope()
print("Outside function:", msg)

# 3. Global Keyword
counter = 0
def increment():
    global counter 
    counter += 1 
    print("Inside increment():", counter)

increment()
print("After increment():", counter)

# 4. Constants (by convention; Python does not enforce)
PI = 3.14159  # naming in ALL CAPS signals "should not change"
print("Constant PI:", PI)

# 5. Dynamic Typing Example
box = 10
print("box is:", box, type(box))
box = "A string now"
print("box is now:", box, type(box))
box = [1, 2, 3]
print("box is now a list:", box, type(box))

# 6. Multiple variables referencing the same object
list1 = [100, 200]
list2 = list1   # Both point to the same list object
list1.append(300)
print("list2 after modifying list1:", list2)  # list2 shows the change

# 7. Deleting a variable
temp = 123
print("temp exists:", temp)
del temp
try:
    print(temp)
except NameError:
    print("temp is deleted and does not exist anymore.")
