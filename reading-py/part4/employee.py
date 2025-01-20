with open("employee.txt", "w") as file:
  file.write("1,John,10000\n")
  file.write("2,Jane,20000\n")
  file.write("3,Doe,30000\n")
  file.write("4,Alice,40000\n")
  file.write("5,Bob,50000\n")
def add_employee(employee_id,employee_name,salary):
  with open("employee.txt","a") as file:
    file.write(f"{employee_id},{employee_name},{salary}\n")
    print(f"Employee '{employee_name}' added successfully.")
add_employee(6,"Charlie",6000)
add_employee(7,"David",7000)
def view_employee():
  print("Employee Records:")
  with open("employee.txt","r") as file:
    lines=file.readlines()
    for line in lines:
      employee_id,employee_name,salary=line.strip().split(",")
      print(f"ID:{employee_id},Name:{employee_name},Salary:{salary}")
view_employee()
def update_employee(employee_id,new_salary):
  updated_employee=[]
  employee_found=False
  with open("employee.txt","r") as file:
    lines=file.readlines()
    for line in lines:
      employee_id,employee_name,salary=line.strip().split(",")
      if int(employee_id)==employee_id:
        employee_found=True
        salary=new_salary
        print(f"Updated salary of '{employee_name}' to {new_salary}.")
        updated_employee.append(f"{employee_id},{employee_name},{salary}\n")
      else:
        updated_employee.append(line)
  with open("employee.txt","w") as file:
    file.writelines(updated_employee)
update_employee(1,10000)
view_employee()
def delete_employee(employee_id):
  updated_employee=[]
  employee_found=False
  with open("employee.txt","r") as file:
    lines=file.readlines()
    for line in lines:
      employee_id,employee_name,salary=line.strip().split(",")
      if int(employee_id)==employee_id:
        employee_found=True
        print(f"Deleted employee '{employee_name}'.")
        continue
      updated_employee.append(line)
    
    if not employee_found:
        print(f"Employee with ID {employee_id} not found.")

  with open("employee.txt","w") as file:
    file.writelines(updated_employee)
delete_employee(1)
view_employee()

