import cx_Oracle
from datetime import datetime, timedelta

# Initialize Oracle client
cx_Oracle.init_oracle_client(lib_dir=r"c:\oracle\instantclient_21_13")

# Establish connection
connection = cx_Oracle.connect(user="system", password="Shraddha", dsn="localhost/xe")
cursor = connection.cursor()

# Get the start and end date for next week
today = datetime.today()
start_of_next_week = today + timedelta(days=(7 - today.weekday()))
end_of_next_week = start_of_next_week + timedelta(days=7)

# Define the SQL query to retrieve exams scheduled for next week
sql_query = """
    SELECT eid, edate, etime
    FROM exam
    WHERE edate >= TO_DATE(:start_date, 'YYYY-MM-DD')
    AND edate < TO_DATE(:end_date, 'YYYY-MM-DD')
"""

# Execute the SQL query with parameter substitution
cursor.execute(sql_query, start_date=start_of_next_week.strftime('%Y-%m-%d'), end_date=end_of_next_week.strftime('%Y-%m-%d'))

# Fetch all the rows
exams = cursor.fetchall()

# Print the exams scheduled for next week
print("Exams scheduled for next week:")
for exam in exams:
    print("Exam ID:", exam[0])
    print("Date:", exam[1].strftime('%Y-%m-%d'))
    print("Time:", exam[2].strftime('%H:%M:%S'))

# Close the cursor and connection
cursor.close()
connection.close()