def view_book():
  try:
    with open("library.txt", "r") as file:
      lines=file.readlines()
      if not lines:
        print("No books available")
      else:
        for line in lines:
          print(line.strip())
  except FileNotFoundError:
    print("No books available . the file does not exist")
  except Exception as e:
    print("An error occurred: ", {e})
def add_book(book_id,book_name,no_of_books):
  try:
    book_id=int(book_id)
    no_of_books=int(no_of_books)
    if book_id<=0 or no_of_books <0:
      raise ValueError("invalid move id or no")
    with open("library.txt","a")as file:
      file.write(f"{book_id},{book_name},{no_of_books}\n")
    print(f"book'{book_id},add successfully")
  except ValueError as e:
    print(f"error:{e}")
  except Exception as e:
    print(f"an error occurred: {e}")
def update_book(book_id,no_of_book):
  try:
    book_id=int(book_id)
    new_no_of_books=int(new_no_of_books)
    if book_id<=0 or new_no_of_books <0:
      raise ValueError("invalid move id or no")
    

    update_book=[]
    book_found=False
    try:
      with open("library.txt","r")as file:
        lines=file.readlines()
    except FileNotFoundError:
      print("the file not exist")
      return
    for line in lines:
      current_id,book_name,no_of_book=line.strip().split(",")
      if int(current_id)==book_id:
        update_book.append(f"{book_id},{book_name},{no_of_book}\n")
        print(f"updated no_of_book for{book_name}to {new_no_of_books}")
        book_found=True
      else:
        update_book.append(line)
    if not book_found:
      print(f"book with id {book_id}is not found")
    else:
      with open("library.txt","w")as file:
        file.writelines(update_book)
   
  except ValueError as e:
    print(f"error:{e}")
  except Exception as e:
    print(f"an error occurred: {e}")


def delete_book(book_id):
    try:
        book_id = int(book_id)
        if book_id <= 0:
            raise ValueError("Invalid book id")
        
        updated_book = []
        movie_found = False
        
        try:
            with open("library.txt", "r") as file:
                lines = file.readlines()
        except FileNotFoundError:
            print("No book found. The file does not exist.")
            return

        for line in lines:
            current_id, book_name, no_of_book = line.strip().split(",")
            if int(current_id) == book_id:
                print(f"Deleted book '{book_name}' with ID {book_id}.")
                movie_found = True
            else:
                updated_book.append(line)
        
        if not movie_found:
            print(f"book with ID {book_id} not found.")
        else:
            with open("library.txt", "w") as file:
                file.writelines(updated_book)
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    while True:
        print("\nbook management  System")
        print("1. Add book")
        print("2. View book")
        print("3. Update book")
        print("4. Delete book")
        print("5. Exit")
        
        try:
            choice = int(input("Enter your choice (1-5): "))
            
            if choice == 1:
                book_id = input("Enter book ID: ")
                book_name = input("Enter book name: ")
               
                no_of_book = input("no_of_book: ")
                add_book(book_id, book_name, no_of_book)
            
            elif choice == 2:
                view_book()
            
            elif choice == 3:
                book_id = input("Enter book ID to update: ")
                no_of_book = input("Enter new no_of_book: ")
                update_book( book_id,  no_of_book)
            
            elif choice == 4:
                movie_id = input("Enter book ID to delete: ")
                delete_book(movie_id)
            
            elif choice == 5:
                print("Thank you for using the book management System!")
                break
            
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")
                
        except ValueError:
            print("Please enter a valid number.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
