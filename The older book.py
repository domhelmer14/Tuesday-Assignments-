class Book:
    def __init__(self, name, author, genre, year):
        self.name = name
        self.author = author
        self.genre = genre
        self.year = year

def older_book(book1, book2):
    if book1.year < book2.year:
        print(f"{book1.name} by {book1.author} ({book1.year}) is older than {book2.name} by {book2.author} ({book2.year}).")
    elif book2.year < book1.year:
        print(f"{book2.name} by {book2.author} ({book2.year}) is older than {book1.name} by {book1.author} ({book1.year}).")
    else:
        print(f"Both books, {book1.name} by {book1.author} and {book2.name} by {book2.author}, were written in {book1.year}.")

# Example usage
python = Book("Fluent Python", "Luciano Ramalho", "programming", 2015)
everest = Book("High Adventure", "Edmund Hillary", "autobiography", 1956)
norma = Book("Norma", "Sofi Oksanen", "crime", 2015)

older_book(python, everest)
older_book(python, norma)
