class Book:
    def __init__(self, id, title, author, total_copies, available_copies):
        self.id = id
        self.title = title
        self.author = author
        self.total_copies = total_copies
        self.available_copies = available_copies


class Member:
    def __init__(self, id, name, email):
        self.m_id = id          
        self.name = name
        self.email = email
        self.borrowed_books = []


class Library():
    def __init__(self):
        self.books = []
        self.members = []
        self.transactions = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added successfully!")

    def add_member(self, member):
        self.members.append(member)
        print(f"Member '{member.name}' added successfully!")

    def find_book(self, book_id):
        for book in self.books:
            if book.id == book_id:
                return book
        return None

    def find_member(self, member_id):
        """Find a member by ID"""
        for member in self.members:
            if member.m_id == member_id:
                return member
        return None

    def display_members_books(self, member_id):
        member = self.find_member(member_id)
        if not member:
            print("Error: Member not found!")
            return

        print(f"=== Books borrowed by {member.name} ===")
        if not member.borrowed_books:    
            print("No books currently borrowed")
        else:
            for book_id in member.borrowed_books:
                book = self.find_book(book_id)
                if book:
                    print(f"- {book.title} by {book.author}")

    def return_book(self, member_id, book_id):
        member = self.find_member(member_id)
        book = self.find_book(book_id)

        if not member or not book:
            print("Error: Member or book not found!")
            return False

        if book_id not in member.borrowed_books:
            print("Error: This member hasn't borrowed this book!")
            return False

        book.available_copies += 1
        member.borrowed_books.remove(book_id)

        for i, transaction in enumerate(self.transactions):  
            if transaction['member_id'] == member_id and transaction['book_id'] == book_id:
                self.transactions.pop(i)                     
                break

        print(f"{member.name} returned '{book.title}'")      
        return True

    def display_available_books(self):
        print("=== Available Books ===")
        for book in self.books:
            if book.available_copies > 0:
                print(f"{book.title} by {book.author} - {book.available_copies} copies available")

    def borrow_book(self, member_id, book_id):
        """Process a book borrowing transaction"""
        member = self.find_member(member_id)
        book = self.find_book(book_id)

        if not member:
            print("Error: Member not found!")
            return False

        if not book:
            print("Error: Book not found!")
            return False

        if book.available_copies <= 0:
            print("Error: No copies available!")
            return False

        if len(member.borrowed_books) >= 3:
            print("Error: Member has reached borrowing limit!")
            return False

        book.available_copies -= 1
        member.borrowed_books.append(book.id)

        transaction = {
            'member_id': member.m_id,   
            'book_id': book.id,
            'member_name': member.name,
            'book_title': book.title
        }
        self.transactions.append(transaction)

        print(f"{member.name} borrowed '{book.title}'")
        return True


# Main program
def test_library_system():
    """Comprehensive test of all library functions"""

    print("=" * 60)
    print("LIBRARY MANAGEMENT SYSTEM - COMPREHENSIVE TEST")
    print("=" * 60)

    library = Library()

    # Test 1: Add Books
    print("\n--- TEST 1: Adding Books ---")
    b1 = Book(1, "Python Crash Course", "Eric Matthes", 3, 3)
    b2 = Book(2, "Clean Code", "Robert Martin", 2, 2)
    b3 = Book(3, "The Pragmatic Programmer", "Hunt & Thomas", 1, 1)
    b4 = Book(4, "Design Patterns", "Gang of Four", 2, 2)

    library.add_book(b1)
    library.add_book(b2)
    library.add_book(b3)
    library.add_book(b4)

    # Test 2: Add Members
    print("\n--- TEST 2: Registering Members ---")
    m1 = Member(101, "Alice Smith", "alice@email.com")
    m2 = Member(102, "Bob Jones", "bob@email.com")
    m3 = Member(103, "Carol White", "carol@email.com")

    library.add_member(m1)
    library.add_member(m2)
    library.add_member(m3)

    # Test 3: Display Available Books
    print("\n--- TEST 3: Display Available Books ---")
    library.display_available_books()

    # Test 4: Successful Book Borrowing
    print("\n--- TEST 4: Successful Borrowing ---")
    library.borrow_book(101, 1)  
    library.borrow_book(101, 2)
    library.borrow_book(102, 1)  

    # Test 5: Display Member's Borrowed Books
    print("\n--- TEST 5: Display Member's Books ---")
    library.display_members_books(101)
    library.display_members_books(102) 
    library.display_members_books(103)

    # Test 6: Display Available Books After Borrowing
    print("\n--- TEST 6: Available Books After Borrowing ---")
    library.display_available_books()

    # Test 7: Borrow Last Available Copy
    print("\n--- TEST 7: Borrowing Last Copy ---")
    library.borrow_book(103, 3) 
    library.display_available_books()

    # Test 8: Try to Borrow Unavailable Book
    print("\n--- TEST 8: Attempting to Borrow Unavailable Book ---")
    library.borrow_book(102, 3) 

    # Test 9: Borrowing Limit Test
    print("\n--- TEST 9: Testing Borrowing Limit (3 books max) ---")
    library.borrow_book(101, 4)  
    library.display_members_books(101)
    library.borrow_book(101, 3) 

    # Test 10: Return Books
    print("\n--- TEST 10: Returning Books ---")
    library.return_book(101, 1)
    library.return_book(102, 1)
    library.display_members_books(101)
    library.display_available_books()

    # Test 11: Try to Return Book Not Borrowed
    print("\n--- TEST 11: Attempting Invalid Return ---")
    library.return_book(102, 2)

    # Test 12: Return and Borrow Again
    print("\n--- TEST 12: Return and Re-borrow ---")
    library.return_book(103, 3)
    library.borrow_book(102, 3)
    library.display_members_books(102)

    # Test 13: Error Cases - Non-existent Member/Book
    print("\n--- TEST 13: Error Handling ---")
    library.borrow_book(999, 1)
    library.borrow_book(101, 999)
    library.return_book(999, 1) 
    library.display_members_books(999)  

    # Test 14: Final Status
    print("\n--- TEST 14: Final Library Status ---")

    print("\nAll Borrowed Books:")
    if library.transactions:
        for transaction in library.transactions:
            print(f"  {transaction['member_name']} has '{transaction['book_title']}'")
    else:
        print("  No borrowed books")

    print("\nAll Members and Their Books:")
    for member in library.members:
        print(f"\n{member.name} ({member.m_id}):")
        if member.borrowed_books:
            for book_id in member.borrowed_books:
                book = library.find_book(book_id)
                if book:
                    print(f"  - {book.title} by {book.author}")
        else:
            print("  (No books borrowed)")
