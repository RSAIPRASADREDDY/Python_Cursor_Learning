'''
Name Mangling in Python
------------------------

Definition:
-----------
Name Mangling is a mechanism in Python where interpreter alters the name of a variable in a class that begins with two underscores (__) and does not end with two underscores. This is done to avoid naming conflicts between subclasses and superclasses. It is mainly used to create "private" variables within classes, i.e., to make some data/attribute less accessible to the outside world.

Methods We Can Use:
--------------------
- Single underscore (_name): Weak "internal use" indicator, not enforced by Python.
- Double underscore (__name): Triggers name mangling.
- Double underscores both sides (__init__): Reserved for special methods, NOT mangled.

Syntax:
--------
class MyClass:
    def __init__(self):
        self.__private_var = value  # Name mangling applies
        self._protected_var = value # No mangling, just a convention

After mangling, __private_var becomes _MyClass__private_var internally.

'''

# ----------------------- Beginner Level Example -----------------------

class Simple:
    def __init__(self):
        self.__data = "secret"
        self._ok = "can see"
        self.avg = "public"
        
s = Simple()
print(s.avg)        # Output: public
print(s._ok)        # Output: can see

'''
Trying to access s.__data will fail:
    print(s.__data)          # Raises AttributeError

But:
    print(s._Simple__data)   # Output: secret (name mangling in action)
'''

# print(s.__data)         # Uncommenting this will error: AttributeError
print(s._Simple__data)    # secret

# ------------------- Intermediate - Use in Inheritance -------------------

class A:
    def __init__(self):
        self.__a = 10   # Name-mangled
    def show(self):
        print(self.__a)

class B(A):
    def __init__(self):
        super().__init__()
        self.__a = 20   # Different variable (name-mangled as _B__a)

a = B()
# a.show()           # Output: 10   (calls A's show, accesses _A__a)
print(a._B__a)        # 20
# print(a.__a)       # AttributeError

'''
This ensures that __a in class A and __a in class B do not overwrite each other.
'''

# -------------- Advanced Example - Preventing Name Clash in Subclass ---------------

class Parent:
    def __init__(self):
        self.__value = 5
    
    def print_val(self):
        print(self.__value)

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.__value = 77    # mangled as _Child__value

    def show_child_val(self):
        print(self.__value)

obj = Child()
obj.print_val()            # 5 (calls Parent's method; refers to _Parent__value)
obj.show_child_val()       # 77 (refers to _Child__value)

# -------------- Snoop on Name Mangling using __dict__ ----------------

class Sample:
    def __init__(self):
        self.__hidden = 42
        self.visible = 99

s = Sample()
print(s.__dict__)    # {'_Sample__hidden': 42, 'visible': 99}

'''
You can inspect the object's dictionary to see name-mangled attributes.
'''

# --------- Attempt Name Mangling with Dunder (should not mangle) -------------

class Special:
    def __init__(self):
        self.__hidden = 9
        self.__init__ = "not hidden"  # NOT name-mangled

sp = Special()
print(hasattr(sp, "_Special__hidden"))   # True
print(hasattr(sp, "__init__"))           # True

# ------------- Mini Project: Bank Account Info Hiding Using Name Mangling -------------

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance     # Private by name mangling

    def deposit(self, amt):
        if amt > 0:
            self.__balance += amt
            print(f"Deposited {amt}")
        else:
            print("Invalid deposit.")

    def withdraw(self, amt):
        if 0 < amt <= self.__balance:
            self.__balance -= amt
            print(f"Withdrawn {amt}")
        else:
            print("Invalid or Insufficient funds.")

    def get_balance(self):
        return self.__balance
    
acct = BankAccount("John", 1000)
acct.deposit(400)              # Deposited 400
acct.withdraw(250)             # Withdrawn 250
print(acct.get_balance())      # 1150

# Direct access fails:
# print(acct.__balance)        # AttributeError!

# But it can be accessed (not recommended) using:
print(acct._BankAccount__balance)  # 1150

'''
Mini Project Summary:
- BankAccount encapsulates the balance using name mangling.
- Clients can't access __balance directly; only via class methods.

This is an example of using name mangling to implement attribute hiding in OOP.
'''


# ------------------ Interview Questions and Answers -------------------

'''
Q1. What is name mangling in Python? Why is it used?
A1. Name mangling is an internal process where Python alters the attribute names with a class-specific prefix when an identifier starts with two underscores. It is used to prevent accidental overrides and ensure that "private" attributes are only accessible within their class.

Q2. How does Python mangle the name of the variable __var in class Test?
A2. It changes __var to _Test__var internally. For example:
    class Test:
        def __init__(self):
            self.__var = 1
    t = Test()
    print(t._Test__var)   # 1

Q3. Does name mangling make attributes truly private?
A3. No. Name mangling only makes it harder (not impossible) to access, deterring accidental use. Attributes can still be accessed via obj._ClassName__attr.

Q4. What happens if a subclass defines a variable with the same name as a double-underscore variable in its superclass?
A4. Both variables coexist; each one is mangled with its respective class's name. They won't collide or interfere.
Example:
    class Base:
        def __init__(self):
            self.__x = 5
    class Sub(Base):
        def __init__(self):
            super().__init__()
            self.__x = 10
    s = Sub()
    print(s._Sub__x)     # 10
    print(s._Base__x)    # 5

Q5. Can name-mangled attributes be accessed outside the class?
A5. Yes, by using the "mangled" name: obj._ClassName__attribute.
Example:
    class Demo:
        def __init__(self): self.__val = 44
    d = Demo()
    print(d._Demo__val)  # 44

Q6. What is the difference between a single underscore and double underscore variable in a class?
A6. Single underscore (e.g., _x): Just a convention to mean "internal use", not enforced. Double underscore (e.g., __x): Triggers name mangling.

Q7. Give a real-world scenario for using name mangling in OOP design.
A7. In subclass-extension frameworks: If you write a parent class with private helpers/attributes (e.g., __helper()) and want to prevent subclasses from accidentally overriding or accessing them, you can use double-underscore names.

Q8. Does Python mangle special dunder methods or attributes (like __init__, __str__)?
A8. No. Names beginning and ending with double underscores (__init__) are reserved for system use and are NOT subject to name mangling.

Q9. Describe how you might bypass name mangling (should you ever need to).
A9. By using the actual mangled name: obj._ClassName__attr. This is discouraged and rarely needed unless debugging or for introspection.

Q10. How does name mangling work with multiple inheritance?
A10. Each class's double underscore attributes are mangled independently; the correct prefix (with the class name) is used so clashes between bases are avoided.
Example:
    class A: def __init__(self): self.__x = 1
    class B: def __init__(self): self.__x = 2
    class C(A, B): def __init__(self): A.__init__(self); B.__init__(self)
    c = C()
    print(c._A__x)  # 1
    print(c._B__x)  # 2
'''
