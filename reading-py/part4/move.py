def view_move_ticket():
    try:
        with open("movex_tickets.txt", "r") as file:
            lines = file.readlines()
            if not lines:
                print("No movie tickets found.")
            else:
                for line in lines:
                    print(line.strip())
    except FileNotFoundError:
        print("No movie tickets found. The file does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

def add_move_ticket(movie_id, movie_name, show_time, available_tickets):
    try:
        movie_id = int(movie_id)
        available_tickets = int(available_tickets)
        if movie_id <= 0 or available_tickets < 0:
            raise ValueError("Invalid movie ID or ticket count")
        
        with open("movex_tickets.txt", "a") as file:
            file.write(f"{movie_id},{movie_name},{show_time},{available_tickets}\n")
        print(f"Movie '{movie_name}' added successfully.")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

def update_move_ticket(movie_id, new_available_tickets):
    try:
        movie_id = int(movie_id)
        new_available_tickets = int(new_available_tickets)
        if movie_id <= 0 or new_available_tickets < 0:
            raise ValueError("Invalid movie ID or ticket count")
        
        updated_tickets = []
        movie_found = False
        
        try:
            with open("movex_tickets.txt", "r") as file:
                lines = file.readlines()
        except FileNotFoundError:
            print("No movie tickets found. The file does not exist.")
            return

        for line in lines:
            current_id, movie_name, show_time, available_tickets = line.strip().split(",")
            if int(current_id) == movie_id:
                updated_tickets.append(f"{movie_id},{movie_name},{show_time},{new_available_tickets}\n")
                print(f"Updated available tickets for '{movie_name}' to {new_available_tickets}.")
                movie_found = True
            else:
                updated_tickets.append(line)
        
        if not movie_found:
            print(f"Movie with ID {movie_id} not found.")
        else:
            with open("movex_tickets.txt", "w") as file:
                file.writelines(updated_tickets)
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

def delete_move_ticket(movie_id):
    try:
        movie_id = int(movie_id)
        if movie_id <= 0:
            raise ValueError("Invalid movie ID")
        
        updated_tickets = []
        movie_found = False
        
        try:
            with open("movex_tickets.txt", "r") as file:
                lines = file.readlines()
        except FileNotFoundError:
            print("No movie tickets found. The file does not exist.")
            return

        for line in lines:
            current_id, movie_name, show_time, available_tickets = line.strip().split(",")
            if int(current_id) == movie_id:
                print(f"Deleted movie '{movie_name}' with ID {movie_id}.")
                movie_found = True
            else:
                updated_tickets.append(line)
        
        if not movie_found:
            print(f"Movie with ID {movie_id} not found.")
        else:
            with open("movex_tickets.txt", "w") as file:
                file.writelines(updated_tickets)
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    while True:
        print("\nMovie Ticket Management System")
        print("1. Add Movie Ticket")
        print("2. View Movie Tickets")
        print("3. Update Movie Ticket")
        print("4. Delete Movie Ticket")
        print("5. Exit")
        
        try:
            choice = int(input("Enter your choice (1-5): "))
            
            if choice == 1:
                movie_id = input("Enter movie ID: ")
                movie_name = input("Enter movie name: ")
                show_time = input("Enter show time: ")
                available_tickets = input("Enter available tickets: ")
                add_move_ticket(movie_id, movie_name, show_time, available_tickets)
            
            elif choice == 2:
                view_move_ticket()
            
            elif choice == 3:
                movie_id = input("Enter movie ID to update: ")
                new_tickets = input("Enter new available tickets: ")
                update_move_ticket(movie_id, new_tickets)
            
            elif choice == 4:
                movie_id = input("Enter movie ID to delete: ")
                delete_move_ticket(movie_id)
            
            elif choice == 5:
                print("Thank you for using the Movie Ticket Management System!")
                break
            
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")
                
        except ValueError:
            print("Please enter a valid number.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
