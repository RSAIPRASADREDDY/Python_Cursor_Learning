"""
Encapsulation in Python
# ------------------------

Definition:
# -----------
Encapsulation is an OOPS concept that restricts direct access to some of an object's attributes and 
methods, protecting the internal state and requiring interactions only via public methods. 
This improves the security, integrity, and modularity of code.

Why is Encapsulation Used?
# --------------------------
- Prevents accidental modification of data.
- Protects sensitive information.
- Enforces controlled access using getters/setters.
- Encourages modularity and maintenance.

How is Encapsulation Achieved in Python?
# ----------------------------------------
1. Using single underscore (_) for 'protected' (convention).
2. Using double underscore (__) for 'private' attributes/methods (name mangling).
3. Providing public methods (getters/setters/properties) to interact with internal state.

Syntax Example:
# ---------------
class MyClass:
    def __init__(self, value):
        self._protected = value       # 'Protected' attribute (convention)
        self.__private = value * 2    # Private attribute (name mangling)

    def get_private(self):
        return self.__private

    def set_private(self, val):
        if val > 0:
            self.__private = val

# -----------------------------------
# Beginner Level Encapsulation Examples
# -----------------------------------
"""

# Example 1: Basic Encapsulation with Private Attribute
class Person:
    def __init__(self, name, age):
        self.__name = name        # private attribute
        self.__age = age          # private attribute

    def get_name(self):
        return self.__name

    def set_name(self, name):
        if isinstance(name, str):
            self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if 0 < age < 150:
            self.__age = age

# Testing
# p1 = Person("Alice", 25)
# print(p1.get_name())      # Output: Alice
# p1.get_age()
# p1.set_name("Sai")
# p1.set_age(-6)
# print(p1.get_age())       # Output: 30
# print(p1.get_name()) 


# -----------------------------------
# Error Handling with Encapsulated Methods
# -----------------------------------

class SafeList:
    def __init__(self, data=None):
        self.__items = list(data) if data is not None else []

    def get(self, index):
        """Safely get item at index, with error handling."""
        try:
            return self.__items[index]
        except IndexError:
            print(f"Error: Index {index} is out of range.")
            return None

    def add(self, item):
        self.__items.append(item)

    def remove(self, item):
        """Safely remove item, with error handling."""
        try:
            self.__items.remove(item)
        except ValueError:
            print(f"Error: {item} not found in the list.")

    def __str__(self):
        return str(self.__items)

    def reverse(self):
        """Reverses the internal list in-place."""
        self.__items.reverse()

    def reversed_copy(self):
        """Returns a reversed copy, does not alter original list."""
        return list(reversed(self.__items))

# Example usage:
# sl = SafeList([1, 2, 3])
# print(sl.get(1))         # 2
# print(sl.get(7))         # Error handled
# sl.add(4)
# sl.remove(2)
# sl.remove(10)            # Error handled
# print(sl)
# sl.reverse()
# print(sl)
# print(sl.reversed_copy())
# print(sl)                # Original not modified by reversed_copy

# -----------------------------------
# How reverse methods work & why use error handling
# -----------------------------------
# - sl.reverse() changes the internal list in-place (like list.reverse())
# - sl.reversed_copy() gives you a new reversed list (like list(reversed(X)))
# - Error handling in get/remove ensures the object never throws, but gives informational output.
#   This is good encapsulation: all errors/warnings are managed at the interface!




# Direct access fails:
# print(p1.__name)        # AttributeError

# Example 2: Protected Attribute Convention
class Demo:
    def __init__(self):
        self._x = 10  # protected (convention only)
    def show(self):
        print(self._x)

# d = Demo()
# d.show()  # 10
# print(d._x)  # Discouraged, but works in Python


# -----------------------------------
# Intermediate Encapsulation Examples
# -----------------------------------

# Example 3: Using @property Getter and Setter
class Account:
    def __init__(self, balance):
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, amount):
        if amount >= 0:
            self.__balance = amount

acct = Account(500)
print(acct.balance)     # 500
acct.balance = 700
print(acct.balance)     # 700
# acct.__balance = 1000 # AttributeError



# Example 4: Private Method
class Machine:
    def __init__(self):
        self.__status = "OFF"
    def __toggle(self):
        self.__status = "ON" if self.__status == "OFF" else "OFF"
    def operate(self):
        self.__toggle()
        print(f"Machine is now {self.__status}")

# mac = Machine()

# mac.operate()  # Machine is now ON
# mac.operate()  # Machine is now OFF
# # mac.__toggle()  # AttributeError

# try:
#     mac.__toggle()
# except AttributeError as e:
#     print("Read the error:",e)

# -----------------------------------
# Advanced Level Encapsulation Example
# -----------------------------------

# Example 5: Enforcing Immutability Using Property (Read-only Value)
class ImmutablePoint:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

p = ImmutablePoint(3, 4)
print(p.x, p.y)     # 3 4
# p.x = 10          # AttributeError

# Example 6: Encapsulation in Inheritance and Name Mangling

class Base:
    def __init__(self):
        self.__secret = "base secret"
        self._protected = "base protected"

class Derived(Base):
    def __init__(self):
        super().__init__()
        self.__secret = "derived secret"
        self._protected = "derived Protected"
    def show(self):
        # print(self.__secret)  # Prints own Derived's secret
        # print(self._protected)
        # print(self._Base__secret) # Access base's private attribute
        print("Derived secret:", self.__secret)
        print("Base secret:", self._Base__secret)
        print("Base protected:", self._protected)
        #print("Base protecteed:", self._Base_protected)     #Not accessible becuase name mangling not works for protected attributes
        
        
d = Derived()
d.show()
# Output:
# Derived secret: derived secret
# Base secret: base secret
# Base protected: base protected


# -----------------------------------
# Mini-project: Bank Vault - Encapsulation Example
# -----------------------------------

class BankVault:
    def __init__(self, owner, pin):
        self.__owner = owner
        self.__balance = 0
        self.__pin = pin

    def deposit(self, amount, pin):
        if pin == self.__pin and amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance is {self.__balance}")
        else:
            print("Invalid pin or amount.")

    def withdraw(self, amount, pin):
        if pin == self.__pin and 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance is {self.__balance}")
        else:
            print("Invalid pin, amount, or insufficient funds.")

    def get_balance(self, pin):
        if pin == self.__pin:
            return self.__balance
        else:
            print("Invalid pin.")
            return None

    def change_pin(self, old_pin, new_pin):
        if old_pin == self.__pin and isinstance(new_pin, int) and 1000 <= new_pin <= 9999:
            self.__pin = new_pin
            print("PIN changed successfully.")
        else:
            print("PIN change failed.")

# Mini-project Usage Example
vault = BankVault("Alice", 1234)
vault.deposit(1000, 1234)
vault.withdraw(500, 1234)
print("Current Balance:", vault.get_balance(1234))
vault.change_pin(1234, 4321)
vault.get_balance(4321)

'''
--------------------------------
Encapsulation Interview Q&A
--------------------------------

Q1. What is encapsulation and how do you implement it in Python?
A1. Encapsulation is the bundling of data and methods operating on that data, restricting direct external access. In Python, prefix attributes with "_" (protected, convention) or "__" (private, name mangling). Provide public methods (getters/setters) to access/change state.

    Example:
        class A:
            def __init__(self):
                self.__x = 10
            def get_x(self):
                return self.__x

Q2. Is encapsulation enforced by the Python language?
A2. Python's encapsulation is by convention and name mangling. Direct access to __private attributes is hard (but possible with _ClassName__attr), so it’s not strictly enforced. Developers are expected to respect access conventions.

Q3. How do properties with @property help in encapsulation?
A3. They allow controlled attribute access: a read-only property, a setter with validation, or computed property. Example:

    class C:
        def __init__(self): self.__a = 0
        @property
        def a(self): return self.__a
        @a.setter
        def a(self, v):
            if v > 0: self.__a = v

Q4. Can a subclass access the parent class's private variables? Explain with code.
A4. No, because private variables are name-mangled. However, they can be accessed via parent’s methods or via _ParentClassName__var (not recommended).

    class P:
        def __init__(self): self.__x = 99
    class C(P):
        def show(self):
            # print(self.__x) # AttributeError
            print(self._P__x)
    C().show()   # 99

Q5. What are the practical benefits of encapsulation in large projects?
A5. Encapsulation allows developers to:
    - Hide complexity.
    - Prevent unintended changes.
    - Change private logic/attribute names without affecting public interface.
    - Implement API contracts.
  Example: The BankVault class above hides PIN and balance, exposing only safe methods.

Q6. How do you make a class attribute read-only after object creation?
A6. Only provide a getter (no setter), or raise in setter:

    class Const:
        def __init__(self, x): self.__x = x
        @property
        def x(self): return self.__x
        @x.setter
        def x(self,val): raise AttributeError("Read only")

Q7. Can you bypass encapsulation in Python? If so, is it a good idea?
A7. Yes, via "name mangling" (_ClassName__var). Example: obj._ClassName__private_var
    It’s discouraged; only for debugging or emergencies, as it breaks encapsulation and future code safety.

Q8. Design a real-world scenario where poor encapsulation could harm security.
A8. E.g., an ATM machine having the pin as a public variable:
    class UnsafeATM:
        def __init__(self): self.pin = 1234
    Anyone can do: atm.pin = 1111
    Good encapsulation would make it private and accessible only to validated methods.

Q9. What's the difference between encapsulation and abstraction, in context of Python classes?
A9.
    - Encapsulation: Controls access to internal data/methods.
    - Abstraction: Exposes only essential operations, hides complexity.
    Encapsulation implements abstraction as a tool.

Q10. Given a class with critical business logic, how would you enforce that logic using encapsulation?
A10. Make critical state variables private, provide only vetted public methods. Enforce business rules in setters/methods. E.g., The BankVault class ensures PIN validation and prevents withdrawal for insufficient funds or invalid PIN.

'''
