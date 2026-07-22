'''
Data Hiding in Python
------------------------

Definition:
-----------
Data Hiding refers to the practice of restricting access to internal object details and implementation, 
exposing only what is necessary and relevant. In Python, this is achieved through conventions and language features that help encapsulate data, 
reducing direct access to attributes and methods from outside the class.

Why is Data Hiding important?
----------------------------
- Prevents accidental modification of critical data.
- Encourages abstraction and encapsulation (core OOP principles).
- Helps maintain and evolve code safely without breaking external code/API users.
- Enforces boundaries between different parts of a program.

Methods We Can Use:
--------------------
- Single underscore _var: Suggests "protected" (internal use only, not enforced).
- Double underscore __var: Name Mangling makes it harder to access (strictest in Python).
- Property decorators (@property, @setter): Offer controlled access/mutation.
'''

# ------------------------------- SYNTAX -------------------------------
'''
Syntax of Data Hiding in Python:
-------------------------------
class MyClass:
    def __init__(self):
        self._internal = "not hidden, but internal-use"
        self.__private = "hidden with name mangling"

Access:
    obj._internal            # Allowed but discouraged
    obj.__private            # AttributeError!
    obj._MyClass__private    # Possible (name mangling), should be avoided outside the class
'''

# ------------------ BEGINNER LEVEL EXAMPLE ----------------------------
class Student:
    def __init__(self, name, age):
        self._name = name         # "Protected" (by convention)
        self.__age = age          # "Private" (name mangling)
    
    def display(self):
        print("Name:", self._name)
        print("Age:", self.__age)

s = Student("Sai", 20)
s.display()
print(s._name)          # Accessible, but discouraged
# print(s.__age)        # Uncommenting will cause AttributeError!
print(s._Student__age)  # Name-mangled: correct (for debugging or expert use)

'''
Explanation:
------------
- _name is for internal/protected use (not enforced).
- __age is for private use (name mangled).
'''

# ----------------- INTERMEDIATE EXAMPLE: Setter and Getter -----------------
class Employee:
    def __init__(self, salary):
        self.__salary = salary

    def get_salary(self):
        return self.__salary
    
    def set_salary(self, value):
        if value < 0:
            print("Invalid Salary!")
        else:
            self.__salary = value

e = Employee(30000)
print(e.get_salary())         # 30000
e.set_salary(40000)
print(e.get_salary())         # 40000
e.set_salary(-500)            # Invalid Salary!

'''
Explanation:
------------
Using getter/setter methods provides controlled access, validating values and hiding internals.
'''

# ------------------- USING PROPERTY DECORATOR (PYTHONIC) -------------------
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self, value):
        if value < 0:
            print("Balance can't be negative!")
        else:
            self.__balance = value

acc = BankAccount(5000)
print(acc.balance)         # 5000
acc.balance = 9000
print(acc.balance)         # 9000
acc.balance = -100         # Balance can't be negative!

'''
With @property, you can use attribute-like access with behind-the-scenes control.
'''

# ------------------- ADVANCED EXAMPLE: Inheritance and Data Hiding -------------------
class Parent:
    def __init__(self):
        self.__secret = "Parent secret"

    def reveal(self):
        print("Parent Secret:", self.__secret)

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.__secret = "Child secret"   # Different attribute due to name mangling

    def reveal(self):
        # Trying to access parent's __secret will not work:
        # print(self.__secret)             # This is Child's __secret, not parent's!
        # print(super().__secret)          # Error!
        print("Child Secret:", self.__secret)

c = Child()
c.reveal()                   # Child Secret: Child secret
print(c._Child__secret)      # Child secret
print(c._Parent__secret)     # Parent secret

'''
Explanation:
------------
- Both Parent and Child can have __secret: no clash due to name mangling (_Parent__secret, _Child__secret).
- Data hiding works properly even in inheritance hierarchies.
'''

# ---------------------------- MINIPROJECT ----------------------------
'''
Mini Project: Simple Password Vault using Data Hiding

Requirements:
-------------
- Each user has a vault with hidden password data.
- Passwords can only be viewed/changed via public methods (access control!).
- Direct access to passwords is hidden.

'''

class PasswordVault:
    def __init__(self, username):
        self.username = username
        self.__passwords = {}   # Hidden from outside!

    def add_account(self, site, pwd):
        if site in self.__passwords:
            print(f"Account for {site} already exists.")
        else:
            self.__passwords[site] = pwd
            print(f"Added account '{site}'.")

    def get_password(self, site):
        return self.__passwords.get(site, "No such account.")

    def update_password(self, site, old_pwd, new_pwd):
        if self.__passwords.get(site) == old_pwd:
            self.__passwords[site] = new_pwd
            print(f"Password updated for {site}.")
        else:
            print("Old password incorrect or account does not exist!")

    def list_sites(self):
        return list(self.__passwords.keys())

vault = PasswordVault("Sai")
vault.add_account("gmail", "pass123")
vault.add_account("github", "mygitpass")
print(vault.get_password("gmail"))       # pass123
vault.update_password("gmail", "pass123", "newpass123")  # Password updated
print(vault.get_password("gmail"))       # newpass123
print(vault.list_sites())                # ['gmail', 'github']

# Direct access fails:
# print(vault.__passwords)     # AttributeError!
print(vault._PasswordVault__passwords)   # Possible, but STRONGLY discouraged

'''
This project demonstrates:
- Hidden sensitive data (__passwords)
- Controlled access/update
- OOP encapsulation and data hiding principles
'''

# ------------------- INTERVIEW Q&A (with examples) -------------------
'''
Q1. How does Python implement data hiding? Is it truly private like C++/Java?
A1. No, Python does not strictly enforce privacy. Data hiding in Python works via name mangling (double underscore) and conventions. Attributes with __name are rewritten as _ClassName__name, making access from outside more difficult, but not impossible. 
Example:
    class Demo:
        def __init__(self): self.__x = 1
    d = Demo()
    print(d._Demo__x)   # 1

Q2. When would you choose a single underscore versus double underscore attribute?
A2. Use a single underscore (_var) for internal-use indicators (protected, don't use externally but subclass can). Use double underscore (__var) when you want to avoid accidental name clashes, especially in base classes, or want to make the attribute less accessible from subclasses.
Example:
    class Parent:
        def __init__(self): self.__secret = 42
    class Child(Parent):
        def foo(self): print(self._Parent__secret)  # Access parent hidden var

Q3. Can you give a real-world scenario where data hiding protects you from bugs?
A3. Yes. Suppose you write a library and use __counter as an internal state. If someone extends your class and also defines __counter, there’s no accidental overwrite because their __counter will be mangled differently. Maintains library and subclass safety.

Q4. How would you expose hidden data for special use or debugging?
A4. You can provide a getter method/property, or if really necessary, access the mangled name (_ClassName__attr).
Example:
    class X: 
        def __init__(self): self.__y = 99
    x = X()
    print(x._X__y)  # 99

Q5. Is it possible to set up read-only properties for hidden data?
A5. Yes, using @property without a setter:
    class Person:
        def __init__(self, ssn): self.__ssn = ssn
        @property
        def ssn(self): return self.__ssn
    p = Person(12345)
    print(p.ssn)   # 12345
    # p.ssn = 234   # AttributeError!

Q6. Can you demonstrate how a subclass cannot accidentally override parent’s hidden fields?
A6. Yes:
    class Base:
        def __init__(self): self.__val = 1
    class Sub(Base):
        def __init__(self): super().__init__(); self.__val = 2
    obj = Sub()
    print(obj._Base__val)  # 1
    print(obj._Sub__val)   # 2

Q7. Why is it not recommended to use mangled names to access private attributes?
A7. Doing so breaks encapsulation and the class's abstraction, making future code fragile. That attribute may change or be removed, and your code will silently break or misbehave.

Q8. How does data hiding support encapsulation in OOP?
A8. Data hiding means only exposing what is needed and hiding the rest. This protects an object’s invariant and internal logic, making the program more robust, modular, and maintainable.

Q9. Can you override property access to implement data validation? Give an example.
A9. Yes, using @property and @property.setter you can perform checks before allowing access or mutation:
    class Test:
        def __init__(self): self.__val = 5
        @property
        def val(self): return self.__val
        @val.setter
        def val(self, v): 
            if v < 0: raise ValueError("Negative!")
            self.__val = v
    t = Test()
    t.val = 10
    # t.val = -5     # Raises ValueError

Q10. When is it OK to make attributes public (no hide at all)?
A10. When the attribute is part of the API, is not critical, or for simple data structures (like records) where privacy is irrelevant. Use hiding only for sensitive or implementation-specific data.

'''
