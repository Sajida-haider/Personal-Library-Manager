import json

# Global list to store books
library = []

# Function to add a book
def add_book():
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    year = input("Enter publication year: ")
    genre = input("Enter genre: ")
    read = input("Have you read it? (yes/no): ").strip().lower() == 'yes'
    
    book = {
        'title': title,
        'author': author,
        'year': year,
        'genre': genre,
        'read': read
    }
    library.append(book)
    print("Book added successfully!\n")

# Function to remove a book by title
def remove_book():
    title = input("Enter the title of the book to remove: ")
    for book in library:
        if book['title'].lower() == title.lower():
            library.remove(book)
            print("Book removed!\n")
            return
    print("Book not found!\n")

# Function to search books
def search_book():
    keyword = input("Enter title, author, or genre to search: ").lower()
    results = [book for book in library if keyword in book['title'].lower() or
               keyword in book['author'].lower() or keyword in book['genre'].lower()]
    
    if results:
        for book in results:
            print(book)
    else:
        print("No matching books found.\n")

# Function to view all books
def view_books():
    if not library:
        print("No books in library.\n")
        return
    for book in library:
        print(book)

# Function to show statistics
def show_statistics():
    total = len(library)
    read_books = sum(book['read'] for book in library)
    unread_books = total - read_books
    genres = {}

    for book in library:
        genre = book['genre']
        genres[genre] = genres.get(genre, 0) + 1

    print(f"Total Books: {total}")
    print(f"Books Read: {read_books}")
    print(f"Books Unread: {unread_books}")
    print("Books per Genre:")
    for genre, count in genres.items():
        print(f"  {genre}: {count}")
    print()

# Save library to file
def save_library():
    with open("library.json", "w") as file:
        json.dump(library, file)
    print("Library saved successfully!\n")

# Load library from file
def load_library():
    global library
    try:
        with open("library.json", "r") as file:
            library = json.load(file)
        print("Library loaded successfully!\n")
    except FileNotFoundError:
        print("No saved library found.\n")

# Menu system
def menu():
    while True:
        print("\n--- Personal Library Manager ---")
        print("1. Add a Book")
        print("2. Remove a Book")
        print("3. Search for a Book")
        print("4. View All Books")
        print("5. View Statistics")
        print("6. Save Library")
        print("7. Load Library")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == '1':
            add_book()
        elif choice == '2':
            remove_book()
        elif choice == '3':
            search_book()
        elif choice == '4':
            view_books()
        elif choice == '5':
            show_statistics()
        elif choice == '6':
            save_library()
        elif choice == '7':
            load_library()
        elif choice == '8':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")

# Start the program
menu()
