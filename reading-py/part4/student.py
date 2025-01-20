# Create the initial students file
with open("students.txt", "w") as file:
    file.write("1,John Doe,85\n")
    file.write("2,Jane Smith,90\n")
    file.write("3,Mark Johnson,78\n")
    file.write("4,Emily Davis,92\n")

# Function to add a new student
def add_student(student_id, student_name, score):
    with open("students.txt", "a") as file:
        file.write(f"{student_id},{student_name},{score}\n")
    print(f"Student '{student_name}' added successfully.")

# Function to view all students
def view_students():
    print("Student Records:")
    with open("students.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            student_id, student_name, score = line.strip().split(",")
            print(f"ID: {student_id}, Name: {student_name}, Score: {score}")

# Function to update a student's score
def update_score(student_id, new_score):
    updated_students = []
    student_found = False
    with open("students.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            s_id, student_name, score = line.strip().split(",")
            if int(s_id) == student_id:
                student_found = True
                score = new_score
                print(f"Updated score of '{student_name}' to {new_score}.")
            updated_students.append(f"{s_id},{student_name},{score}\n")
    
    if not student_found:
        print(f"Student with ID {student_id} not found.")

    with open("students.txt", "w") as file:
        file.writelines(updated_students)

# Function to delete a student record
def delete_student(student_id):
    updated_students = []
    student_found = False
    with open("students.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            s_id, student_name, score = line.strip().split(",")
            if int(s_id) == student_id:
                student_found = True
                print(f"Deleted record of '{student_name}'.")
                continue
            updated_students.append(line)
    
    if not student_found:
        print(f"Student with ID {student_id} not found.")

    with open("students.txt", "w") as file:
        file.writelines(updated_students)

# Example Workflow
view_students()
add_student(5, "Chris Brown", 88)
view_students()
update_score(3, 80)
view_students()
delete_student(4)
view_students()
