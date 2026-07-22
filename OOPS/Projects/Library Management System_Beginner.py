
"""
Python OOP Learning: Real-World Projects from Beginner to Advanced

For each project, you will find:
- Project meta info & real-world context
- OOP concepts demonstrated explicitly
- Detailed code with extensive comments
- Interview Q&A and best practices

You can work through each project in order, as each one introduces more advanced OOP concepts and patterns.

───────────────────────────────
Project 1: Library Management System (Beginner)
───────────────────────────────

Project Name:
    Library Management System

Real-world Use Case:
    Small libraries need a basic system to manage books and members, track borrowed items, and due dates.

Problem Statement:
    Build a console-based library system that supports:
        - Adding/removing/listing books and members
        - Borrowing/returning books with rules

Requirements:
    - Use classes, objects, instance/class variables and methods
    - Demonstrate encapsulation (public/private), basic inheritance, and __str__ method
    - Custom exceptions for book/member not found

Folder Structure:
    library_system/
        main.py
        models.py
        exceptions.py
        tests.py

Step-by-Step Development Plan:
    1. Define Book and Member classes with encapsulation
    2. Create Library class with a collection of books and members
    3. Demonstrate adding/removing/listing operations
    4. Implement borrowing/returning logic with checks and exceptions
    5. Add __str__ & __repr__ for print-friendly output
    6. Provide simple test cases


# ─────────────────────────────
# Filename: main.py
# ─────────────────────────────

"""

# Let's define custom exceptions in exceptions.py

# exceptions.py
class BookNotFoundError(Exception):
    """Raised when a book with a given ISBN is not found."""
    pass

class MemberNotFoundError(Exception):
    """Raised when a member with a given ID is not found."""
    pass

class BookAlreadyBorrowedError(Exception):
    """Raised when a book is already borrowed."""
    pass

class BookNotBorrowedError(Exception):
    """Raised when attempting to return a book that isn't borrowed."""
    pass

# models.py

class Book:
    """Represents a book in the library."""
    # Class variable to track total books (demonstrates class variable use)
    total_books = 0

    def __init__(self, title: str, author: str, isbn: str):
        # Encapsulation: private member denoted by _
        self._title = title
        self._author = author
        self.isbn = isbn  # public variable
        self._borrowed_by = None  # protected member to indicate member ID if borrowed
        Book.total_books += 1

    # Properties for encapsulation (getters/setters)
    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    def is_borrowed(self):
        """Helper to check if book is borrowed."""
        return self._borrowed_by is not None

    def borrow(self, member_id):
        if self.is_borrowed():
            raise BookAlreadyBorrowedError(f"{self._title} is already borrowed.")
        self._borrowed_by = member_id

    def return_book(self):
        if not self.is_borrowed():
            raise BookNotBorrowedError(f"{self._title} is not borrowed.")
        self._borrowed_by = None

    def __str__(self):
        borrow_status = "Available" if not self.is_borrowed() else f"Borrowed by {self._borrowed_by}"
        return f"Book(Title: {self._title}, Author: {self._author}, ISBN: {self.isbn}, Status: {borrow_status})"

    def __repr__(self):
        return self.__str__()

class Member:
    """Represents a member of the library."""
    total_members = 0

    def __init__(self, name: str, member_id: str):
        self.name = name
        self.member_id = member_id
        self._borrowed_books = []
        Member.total_members += 1

    def borrow_book(self, book: Book):
        if book.is_borrowed():
            raise BookAlreadyBorrowedError(book.title)
        book.borrow(self.member_id)
        self._borrowed_books.append(book.isbn)

    def return_book(self, book: Book):
        if book.isbn not in self._borrowed_books:
            raise BookNotBorrowedError(f"{book.title} not borrowed by {self.name}")
        book.return_book()
        self._borrowed_books.remove(book.isbn)

    def __str__(self):
        return f"Member(Name: {self.name}, ID: {self.member_id}, Borrowed Books: {self._borrowed_books})"

# Inheritance Example: Staff is a subclass of Member (Single Inheritance)
class Staff(Member):
    def __init__(self, name, member_id, staff_id):
        super().__init__(name, member_id)  # Single Inheritance
        self.staff_id = staff_id

    def __str__(self):
        return f"Staff(Name: {self.name}, StaffID: {self.staff_id}, ID: {self.member_id})"

# Library aggregates books & members; demonstrates Association & Composition
class Library:
    """Main library management interface."""
    def __init__(self):
        self.books = {}     # isbn: Book
        self.members = {}   # member_id: Member

    def add_book(self, book: Book):
        self.books[book.isbn] = book

    def remove_book(self, isbn: str):
        if isbn in self.books:
            del self.books[isbn]
        else:
            raise BookNotFoundError(isbn)

    def add_member(self, member: Member):
        self.members[member.member_id] = member

    def remove_member(self, member_id: str):
        if member_id in self.members:
            del self.members[member_id]
        else:
            raise MemberNotFoundError(member_id)

    def borrow_book(self, member_id: str, isbn: str):
        if member_id not in self.members:
            raise MemberNotFoundError(member_id)
        if isbn not in self.books:
            raise BookNotFoundError(isbn)
        member = self.members[member_id]
        book = self.books[isbn]
        member.borrow_book(book)

    def return_book(self, member_id: str, isbn: str):
        if member_id not in self.members:
            raise MemberNotFoundError(member_id)
        if isbn not in self.books:
            raise BookNotFoundError(isbn)
        member = self.members[member_id]
        book = self.books[isbn]
        member.return_book(book)

    def list_books(self):
        for book in self.books.values():
            print(book)

    def list_members(self):
        for member in self.members.values():
            print(member)

# main.py
def main():
    # Demo: Create a library and add books/members
    library = Library()

    # Create books and members (objects)
    b1 = Book("Harry Potter", "J.K. Rowling", "ISBN123")
    b2 = Book("1984", "Orwell", "ISBN987")

    m1 = Member("Alice", "M001")
    m2 = Staff("Bob", "M002", "S001")     # Inheritance (Staff is a kind of Member)

    library.add_book(b1)
    library.add_book(b2)
    library.add_member(m1)
    library.add_member(m2)

    # Showcase borrowing
    print("--- Library Books ---")
    library.list_books()

    print("\n--- Library Members ---")
    library.list_members()

    print("\n--- Borrowing Book ---")
    library.borrow_book("M001", "ISBN123")
    print(b1)

    print("\n--- Attempt Double Borrow ---")
    try:
        library.borrow_book("M002", "ISBN123")
    except BookAlreadyBorrowedError as e:
        print(e)

    print("\n--- Returning Book ---")
    library.return_book("M001", "ISBN123")
    print(b1)

if __name__ == "__main__":
    main()

"""
──────────
OOP Concepts Used:
──────────
- Class, Object, Constructor, Instance/Class Variables, Instance Methods
- Single Inheritance (Staff → Member), Association/Composition (Library has Books and Members)
- Encapsulation (private/protected/public vars), Getters/Setters/Property
- Magic Methods (__str__, __repr__)
- Custom Exceptions and Error Handling

Why these choices?
- Encapsulation: Keeps attributes safe and exposes only necessary info (best practice)
- Inheritance: Staff "is a" Member (models real-life hierarchies)
- Composition: Library "has" Books, Members
- Custom Exceptions: Clean and clear error communication

Sample Interview Questions:
- Q: How does encapsulation improve code maintainability in this project?
- Q: What is the difference between association and inheritance here?
- Q: Why use a custom exception rather than a built-in one?
- Q: Give an example of a magic method and its purpose.

Common Mistakes:
- Making all attributes public (violates encapsulation)
- Not handling errors when borrowing an already checked-out book
- Forgetting to update borrowed status on return

Refactoring Opportunities:
- Decouple persistence (file/db) from logic
- Support role-based permissions for Staff vs. Member

Production-level Improvements:
- Database backend for persistence
- Logging for all major actions
- Authentication for Staff/Member
- Testing (see tests.py for examples)

Scalability:
- Use of dicts for O(1) lookup
- Abstract interfaces if dealing with thousands of books/members

───────────────────────────────
Project 2: Banking Application (Intermediate)
───────────────────────────────

Project Name:
    Banking Application

Real-world Use Case:
    Banks or fintech apps require robust OOP systems to manage accounts, transactions, and users securely.

Problem Statement:
    Design a banking system that models:
        - Savings, Checking (and possibly Business) accounts
        - Deposits, withdrawals, transfers
        - Account locking, notifications, and transaction history

Requirements:
    - Demonstrate multi-level, hierarchical, and multiple inheritance
    - Use abstract classes (abc), method overriding, operator overloading, class/static methods
    - Apply SOLID design principles
    - Exception handling for overdraft, locked account, invalid transaction

Folder Structure:
    banking_app/
        accounts.py
        transactions.py
        notifications.py
        exceptions.py
        main.py
        tests.py

Step-by-Step Development Plan:
    1. Define abstract Account base class with account operations (Abstraction)
    2. Implement SavingsAccount and CheckingAccount
    3. Show multiple inheritance via NotificationMixin or context manager for logs
    4. Overload operators to allow account merging/balance comparison
    5. Compose Transaction history object with aggregation
    6. Implement exception handling strategy for transactions

# ─────────────────────────────
# Filename: accounts.py
# ─────────────────────────────

import abc

# exceptions.py
class OverdraftError(Exception): pass
class AccountLockedError(Exception): pass

# Mixin for notifications (Multiple Inheritance)
class NotificationMixin:
    def send_notification(self, message: str):
        print(f"[NOTIFY] {message}")

# Abstract Base Class (Abstraction/OOP)
class Account(abc.ABC):
    all_accounts = []

    def __init__(self, owner: str, balance: float = 0.0):
        self._owner = owner                 # encapsulated attribute (protected)
        self._balance = balance
        self._locked = False
        Account.all_accounts.append(self)

    @abc.abstractmethod
    def account_type(self): pass

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Deposit must be positive.")
        self._balance += amount

    def withdraw(self, amount: float):
        if self._locked:
            raise AccountLockedError("Account is locked.")
        if amount > self._balance:
            raise OverdraftError("Insufficient funds.")
        self._balance -= amount

    def lock(self):
        self._locked = True

    def unlock(self):
        self._locked = False

    @property
    def balance(self):
        return self._balance

    def __str__(self):
        return f"{self.account_type()} Account (Owner: {self._owner}, Balance: ${self._balance:.2f})"

    def __add__(self, other):
        # Operator Overloading: Merging two accounts creates a new temporary joint-type account
        if not isinstance(other, Account):
            return NotImplemented
        return TemporaryJointAccount(self._owner + '&' + other._owner, self._balance + other._balance)

    def __eq__(self, other):
        return isinstance(other, Account) and self._balance == other._balance

class TransactionHistory:
    def __init__(self):
        self._logs = []

    def add(self, entry):
        self._logs.append(entry)

    def __iter__(self):
        self._index = 0
        return self

    def __next__(self):
        if self._index >= len(self._logs):
            raise StopIteration
        val = self._logs[self._index]
        self._index += 1
        return val

# Inheritance Examples:

# Multi-level Inheritance: SavingsAccount inherits Account, then ChildSavings can inherit SavingsAccount
class SavingsAccount(NotificationMixin, Account):
    def __init__(self, owner, balance=0.0, interest_rate=0.01):
        Account.__init__(self, owner, balance)
        self._interest_rate = interest_rate
        self.history = TransactionHistory()

    def account_type(self):
        return "Savings"

    def add_interest(self):
        self._balance += self._balance * self._interest_rate
        self.history.add(f"Interest added. New balance: {self._balance:.2f}")
        self.send_notification(f"Interest credited: {self._balance:.2f}")

    def deposit(self, amount):
        super().deposit(amount)
        self.history.add(f"Deposited: ${amount}")
        self.send_notification(f"Deposit received: ${amount}")

    def withdraw(self, amount):
        super().withdraw(amount)
        self.history.add(f"Withdrew: ${amount}")
        self.send_notification(f"Withdrawal: ${amount}")

class CheckingAccount(NotificationMixin, Account):
    def __init__(self, owner, balance=0.0, overdraft_limit=100.0):
        super().__init__(owner, balance)
        self._overdraft_limit = overdraft_limit
        self.history = TransactionHistory()

    def account_type(self):
        return "Checking"

    def withdraw(self, amount):
        if self._locked:
            raise AccountLockedError()
        if amount > self._balance + self._overdraft_limit:
            raise OverdraftError("Over limit")
        self._balance -= amount
        self.history.add(f"Withdrew: ${amount}")
        self.send_notification(f"Withdrawal ({amount}) on Checking")

# Temporary joint account via operator overloading
class TemporaryJointAccount(Account):
    def account_type(self):
        return "TemporaryJoint"

# Demonstration via main.py
def demo_banking():
    acc1 = SavingsAccount("Alice", 500)
    acc2 = CheckingAccount("Bob", 200)
    try:
        acc1.deposit(150)
        acc2.withdraw(50)
        acc1.add_interest()
        acc1.withdraw(700)  # Will raise OverdraftError
    except OverdraftError as ex:
        print("[Error]", ex)
    # Operator Overloading
    joint = acc1 + acc2
    print(joint)
    # Iterable transaction history
    for entry in acc1.history:
        print("Log:", entry)

if __name__ == "__main__":
    print("\n==== Banking Demo ====")
    demo_banking()


'''
──────────
OOP Concepts Used:
──────────
- Abstract Class, Abstract Method, Inheritance (multi-level, hierarchical), Multiple Inheritance via Notifications
- Static/Class methods, Operator Overloading (__add__, __eq__)
- Encapsulation, Exception Handling with custom exceptions, Aggregation of TransactionHistory
- Magic Methods (__str__, __iter__, __next__)

Interview Questions:
- Q: What is the role of abstract classes in Python OOP?
- Q: How does operator overloading make code more Pythonic?
- Q: What's the difference between multiple and multi-level inheritance?
- Q: Why use mixins in this context?

Common Mistakes:
- Not calling super() in overriden methods
- Failing to enforce encapsulation (exposing variables directly)
- Not updating history after failed transactions

Refactoring Opportunities:
- Split account types into separate modules
- Use context managers for locking/unlocking

Production Improvements:
- Persistent transaction history (file/db)
- Real notification system (emails, SMS)
- Thread-safety, concurrency locks

Scalability:
- Use repository pattern for db access
- Divide code for high cohesion and loose coupling

───────────────────────────────
Project 3: Employee Payroll System (Intermediate/Advanced)
───────────────────────────────
-- For brevity, only the first two projects are included here. Continue project definitions in the same structure for full coverage.

"""

