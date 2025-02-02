import pyodbc

# Define SQL Server connection details
server = 'localhost'  # Replace with your server name if needed
database = 'master'   # Connect to the 'master' DB to create a new one
driver = '{ODBC Driver 17 for SQL Server}'  # Ensure this driver is installed

# Connect using Windows Authentication
conn_str = f'DRIVER={driver};SERVER={server};DATABASE={database};Trusted_Connection=yes;'

try:
    # Connect to SQL Server
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    print("Connected to SQL Server successfully!")

    # Step 1: Create the StudentDB database
    cursor.execute("""
    IF NOT EXISTS (SELECT name FROM sys.databases WHERE name = 'StudentDB')
    CREATE DATABASE StudentDB
    """)
    conn.commit()
    print("Database 'StudentDB' created successfully!")

    # Step 2: Switch to StudentDB to create tables
    cursor.execute("USE StudentDB")

    # Step 3: Create Students table
    create_table_query = """
    IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='Students' AND xtype='U')
    CREATE TABLE Students (
        StudentID INT PRIMARY KEY IDENTITY(1,1),
        FirstName NVARCHAR(50),
        LastName NVARCHAR(50),
        Age INT,
        Major NVARCHAR(100),
        EnrollmentDate DATE
    )
    """
    cursor.execute(create_table_query)
    conn.commit()
    print("Table 'Students' created successfully!")

    # Step 4: Insert sample student records
    insert_query = """
    INSERT INTO Students (FirstName, LastName, Age, Major, EnrollmentDate)
    VALUES 
        ('Alice', 'Johnson', 20, 'Computer Science', '2023-09-01'),
        ('Bob', 'Smith', 22, 'Electrical Engineering', '2022-09-01'),
        ('Charlie', 'Brown', 21, 'Mechanical Engineering', '2021-09-01')
    """
    cursor.execute(insert_query)
    conn.commit()
    print("Sample student records inserted successfully!")

    # Step 5: Display inserted records
    cursor.execute("SELECT * FROM Students")
    rows = cursor.fetchall()
    print("\nStudent Records:")
    for row in rows:
        print(f"ID: {row.StudentID}, Name: {row.FirstName} {row.LastName}, Age: {row.Age}, Major: {row.Major}, Enrolled: {row.EnrollmentDate}")

    conn.close()

except Exception as e:
    print(f"Error: {e}")
