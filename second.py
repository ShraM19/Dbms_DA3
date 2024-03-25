# Import cx_Oracle
import cx_Oracle

# Initialize Oracle client
cx_Oracle.init_oracle_client(lib_dir=r"c:\oracle\instantclient_21_13")

# Establish connection
connection = cx_Oracle.connect(user="system", password="Shraddha", dsn="localhost/xe")
cursor = connection.cursor()

try:
    # Define the student ID to be deleted
    student_id = '22BCE1163'

    # Delete from enrollment table
    delete_enrollment_query = """
        DELETE FROM enrollment
        WHERE student_id = :student_id
    """
    cursor.execute(delete_enrollment_query, student_id=student_id)

    # Delete from student table
    delete_student_query = """
        DELETE FROM student_proj
        WHERE student_id = :student_id
    """
    cursor.execute(delete_student_query, student_id=student_id)

    # Commit the transaction
    connection.commit()

    # Print confirmation
    print("Student record and related enrollments deleted successfully.")

except cx_Oracle.Error as error:
    print("Error occurred:", error)

finally:
    # Close the cursor and connection
    cursor.close()
    connection.close()