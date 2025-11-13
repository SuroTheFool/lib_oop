# Library Management System (OOP)

## Project Overview
This project is a beginner-friendly Object-Oriented Library Management System.  
It lets you add books and members, borrow and return books, and display available books or books borrowed by a member.

---

## Project Structure

```text
.
├── library.py      # Book, Member, Library classes and main logic
└── test_oop.py     # Test suite for the library system
```

---

## Design Overview

### `Book`
- Attributes: `id`, `title`, `author`, `total_copies`, `available_copies`
- Role: represents a single book and its current availability.

### `Member`
- Attributes: `m_id`, `name`, `email`, `borrowed_books`
- Role: represents a library member and which books they have borrowed.

### `Library`
- Attributes: `books`, `members`, `transactions`
- Key methods:  
  `add_book`, `add_member`, `find_book`, `find_member`,  
  `display_available_books`, `display_members_books`,  
  `borrow_book`, `return_book`.

---

## Testing

All tests are in:

```python
test_oop.py
```

The test suite covers:

- Basic operations  
  - Adding books and members  
  - Borrowing and returning books  
  - Displaying available books and member books  

- Edge cases  
  - Borrowing unavailable books  
  - Exceeding the borrowing limit (3 books)  
  - Returning books not borrowed  
  - Non-existent books or members  

---

## How to Run Your Test Code

From the project directory, run:

```bash
python test_oop.py
```
