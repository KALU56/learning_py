import psycopg2

# Replace these values with your database credentials
hostname = "localhost"
database = "your_db_name"
username = "your_db_user"
password = "your_db_password"
port = "5432"  # default PostgreSQL port

# Establish the connection
connection = psycopg2.connect(
    host=hostname,
    dbname=database,
    user=username,
    password=password,
    port=port
)

# Create a cursor object to interact with the database
cursor = connection.cursor()

# Check if the connection was successful by executing a query
cursor.execute("SELECT version();")
db_version = cursor.fetchone()
print("Database version:", db_version)
