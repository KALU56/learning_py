with open("movex_tickets.txt","w") as file:
  file.write("1,adventher,2:00,100\n")
  file.write("2,batman,3:00,100\n")
  file.write("3,superman,4:00,100\n")
  file.write("4,spiderman,5:00,100\n")
  file.write("5,ironman,6:00,100\n")
def add_move_ticket(movie_id,movie_name,show_time,available_tickets):
  with open("movex_tickets.txt","a") as file:
    file.write(f"{movie_id},{movie_name},{show_time},{available_tickets}\n")
    print(f"Movie '{movie_name}' added successfully.")
def view_move_ticket():
  print("Movie Records:")
  with open("movex_tickets.txt","r") as file:
    lines=file.readlines()
    for line in lines:
      movie_id,movie_name,show_time,available_tickets=line.strip().split(",")
      print(f"ID:{movie_id},Name:{movie_name},Show Time:{show_time},Available Tickets:{available_tickets}")
view_move_ticket()
def update_move_ticket(movie_id,new_available_tickets):
  updated_move_ticket=[]
  movie_found=False
  with open("movex_tickets.txt","r") as file:
    lines=file.readlines()
    for line in lines:
      movie_id,movie_name,show_time,available_tickets=line.strip().split(",")
      if int(movie_id)==movie_id:
        with open("movex_tickets.txt","w") as file:
          file.write(f"{movie_id},{movie_name},{show_time},{new_available_tickets}\n")
          print(f"Updated available tickets for '{movie_name}' to {new_available_tickets}.")
          movie_found=True
      else:
        updated_move_ticket.append(line)
  if not movie_found:
    print(f"Movie with ID {movie_id} not found.")
  with open("movex_tickets.txt","w") as file:
    file.writelines(updated_move_ticket)
update_move_ticket(1,100)
view_move_ticket()
def delete_move_ticket(movie_id):
  updated_move_ticket=[]
  movie_found=False
  with open("movex_tickets.txt","r") as file:
    lines=file.readlines()
    for line in lines:
      movie_id,movie_name,show_time,available_tickets=line.strip().split(",")
      if int(movie_id)==movie_id:
        movie_found=True
        print(f"Deleted movie '{movie_name}'.")
      else:
        updated_move_ticket.append(line)
  if not movie_found:
    print(f"Movie with ID {movie_id} not found.")
  with open("movex_tickets.txt","w") as file:
    file.writelines(updated_move_ticket)
delete_move_ticket(1)
view_move_ticket()
    

