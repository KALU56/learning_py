# Create the initial library file
with open("library.txt", "w") as file:
    file.write("1,To Kill a Mockingbird,10\n")
    file.write("2,1984,8\n")
    file.write("3,The Great Gatsby,5\n")
    file.write("4,The Catcher in the Rye,7\n")

# Function to add a new book
def add_book(book_id, book_name, copies):
    with open("library.txt", "a") as file:
        file.write(f"{book_id},{book_name},{copies}\n")
    print(f"Book '{book_name}' added successfully.")

# Function to view all books
def view_books():
    print("Available books:")
    with open("library.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            book_id, book_name, copies = line.strip().split(",")
            print(f"ID: {book_id}, Title: {book_name}, Copies: {copies}")

# Function to borrow a book
def borrow_book(book_id, copies_to_borrow):
    updated_books = []
    book_found = False
    with open("library.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            b_id, book_name, copies = line.strip().split(",")
            if int(b_id) == book_id:
                book_found = True
                if int(copies) >= copies_to_borrow:
                    copies = int(copies) - copies_to_borrow
                    print(f"Borrowed {copies_to_borrow} copies of '{book_name}'.")
                else:
                    print(f"Insufficient copies of '{book_name}'.")
            updated_books.append(f"{b_id},{book_name},{copies}\n")
    
    if not book_found:
        print(f"Book with ID {book_id} not found.")
    
    with open("library.txt", "w") as file:
        file.writelines(updated_books)

# Function to return a book
def return_book(book_id, copies_to_return):
    updated_books = []
    book_found = False
    with open("library.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            b_id, book_name, copies = line.strip().split(",")
            if int(b_id) == book_id:
                book_found = True
                copies = int(copies) + copies_to_return
                print(f"Returned {copies_to_return} copies of '{book_name}'.")
            updated_books.append(f"{b_id},{book_name},{copies}\n")
    
    if not book_found:
        print(f"Book with ID {book_id} not found.")
    
    with open("library.txt", "w") as file:
        file.writelines(updated_books)

# Example Workflow
view_books()
borrow_book(3, 2)
view_books()
return_book(3, 2)
view_books()
add_book(5, "Pride and Prejudice", 6)
view_books()
