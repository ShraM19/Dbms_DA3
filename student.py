# Import cx_Oracle
import cx_Oracle

# Initialize Oracle client
cx_Oracle.init_oracle_client(lib_dir=r"c:\oracle\instantclient_21_13")

# Establish connection
connection = cx_Oracle.connect(user="system", password="Shraddha", dsn="localhost/xe")
cursor = connection.cursor()

# Define the SQL query
sql_query = """
    SELECT c.course_code, c.title, COUNT(e.student_id) as enrolled_students
    FROM course_proj c
    LEFT JOIN enrollment e ON c.course_code = e.course_code
    GROUP BY c.course_code, c.title
"""

# Execute the SQL query
cursor.execute(sql_query)

# Fetch all the rows
course_enrollments = cursor.fetchall()

# Print the number of students enrolled in each course
print("Number of students enrolled in each course:")
for course in course_enrollments:
    print(f"Course: {course[0]} - {course[1]}, Enrolled Students: {course[2]}")

# Close the cursor and connection
cursor.close()
connection.close()