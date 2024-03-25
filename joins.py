import cx_Oracle

# Initialize Oracle client
cx_Oracle.init_oracle_client(lib_dir=r"c:\oracle\instantclient_21_13")

# Establish connection
connection = cx_Oracle.connect(user="system", password="Shraddha", dsn="localhost/xe")
cursor = connection.cursor()

# Define the course code for which you want to retrieve student names
course_code = 'BCS101L'

# Define the SQL query
sql_query = """
    SELECT s.name
    FROM student_proj s
    JOIN enrollment e ON s.student_id = e.student_id
    WHERE e.course_code = :course_code
"""

# Execute the SQL query with parameter substitution
cursor.execute(sql_query, course_code=course_code)

# Fetch all the rows
student_names = cursor.fetchall()

# Print the names of students enrolled in the specified course
print("Students enrolled in course", course_code, ":")
for name in student_names:
    print(name[0])

# Close the cursor and connection
cursor.close()
connection.close()