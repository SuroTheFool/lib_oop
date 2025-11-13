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
