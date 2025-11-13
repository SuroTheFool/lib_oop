class Book:
    def __init__(self,id,title,author,total_copies,available_copies):
        self.id = id
        self.title = title
        self.author = author
        self.total_copies = total_copies
        self.available_copies = available_copies

class Member:
    def __init__(self,id,name,email):
        self.id = id
        self.name = name
        self.email = email
        self.borrowed_books = []

