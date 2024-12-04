class LibraryBookTracker:
    def __init__(self):
        self.collection = set()  
        self.borrowed_books = []  

    # 1. Add new books to the library collection
    def add_book(self, book):
        if book in self.collection:
            print(f'The book "{book}" is already in the collection.')
        else:
            self.collection.add(book)
            print(f'The book "{book}" has been added to the collection.')
            
# 2. Search for books by a keyword
    def search_books(self, keyword):
        results = [book for book in self.collection if keyword.lower() in book.lower()]
        if results:
            print("Search Results:")
            for book in sorted(results):
                print(f"- {book}")
        else:
            print("No books found matching the keyword.")
            
# 3. Remove a book by its exact title
    def remove_book(self, title):
        book_to_remove = next((book for book in self.collection if book.startswith(title)), None)
        if book_to_remove:
            self.collection.remove(book_to_remove)
            print(f'The book "{book_to_remove}" has been removed from the collection.')
        else:
            print("The book was not found in the collection.")

    # 4. Display the list of all unique authors
    def display_unique_authors(self):
        authors = {book.split(" by ")[-1] for book in self.collection}
        if authors:
            print("Unique Authors:")
            for author in sorted(authors):
                print(f"- {author}")
        else:
            print("No authors found in the collection.")

    # 5. Display all books sorted alphabetically by title
    def display_all_books(self):
        if self.collection:
            print("Books in the Collection (Sorted by Title):")
            for book in sorted(self.collection):
                print(f"- {book}")
        else:
            print("The library collection is empty.")

    # 6. Add and show borrowed books
    def add_borrowed_book(self, borrower, book_title):
        if book_title in self.collection:
            self.borrowed_books.append((borrower, book_title))
            print(f'"{book_title}" has been borrowed by {borrower}.')
        else:
            print(f'The book "{book_title}" is not available in the collection.')

    def display_borrowed_books(self):
        if self.borrowed_books:
            print("Borrowed Books:")
            for borrower, book in self.borrowed_books:
                print(f"- {borrower} borrowed '{book}'")
        else:
            print("No books are currently borrowed.")

# Example Usage
def main():
    library = LibraryBookTracker()

    # Adding books
    print("\nAdding books:")
    library.add_book("1984 by George Orwell")
    library.add_book("To Kill a Mockingbird by Harper Lee")
    library.add_book("Pride and Prejudice by Jane Austen")
    library.add_book("The Great Gatsby by F. Scott Fitzgerald")
    library.add_book("1984 by George Orwell")  # Duplicate

    # Searching for books
    print("\nSearching for books:")
    library.search_books("Pride")
    library.search_books("Mockingbird")
    library.search_books("Unknown")

    # Removing a book
    print("\nRemoving a book:")
    library.remove_book("1984")
    library.remove_book("Nonexistent Book")

    # Displaying unique authors
    print("\nUnique authors:")
    library.display_unique_authors()

    # Displaying all books
    print("\nAll books:")
    library.display_all_books()

    # Managing borrowed books
    print("\nManaging borrowed books:")
    library.add_borrowed_book("Alice", "To Kill a Mockingbird by Harper Lee")
    library.add_borrowed_book("Bob", "Pride and Prejudice by Jane Austen")
    library.add_borrowed_book("Charlie", "Nonexistent Book")  # Book not in collection

    # Displaying borrowed books
    print("\nBorrowed books:")
    library.display_borrowed_books()

if __name__ == "__main__":
    main()
