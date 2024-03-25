# Import cx_Oracle
import cx_Oracle

# Initialize Oracle client
cx_Oracle.init_oracle_client(lib_dir=r"c:\oracle\instantclient_21_13")

# Establish connection
connection = cx_Oracle.connect(user="system", password="Shraddha", dsn="localhost/xe")
cursor = connection.cursor()

# Define the department code for which you want to retrieve courses
department_code = 'EEE'

# Define the SQL query to retrieve courses offered by a specific department
sql_query = """
    SELECT c.course_code, c.title
    FROM course_proj c
    JOIN teaches t ON c.course_code = t.course_code
    JOIN professor p ON t.pid = p.pid
    JOIN department d ON p.dcode = d.dcode
    WHERE d.dcode = :department_code
"""

# Execute the SQL query with parameter substitution
cursor.execute(sql_query, department_code=department_code)

# Fetch all the rows
courses = cursor.fetchall()

# Print the courses offered by the specified department
print("Courses offered by department", department_code, ":")
for course in courses:
    print(course)

# Close the cursor and connection
cursor.close()
connection.close()
