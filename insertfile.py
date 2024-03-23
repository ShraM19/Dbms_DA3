import cx_Oracle
cx_Oracle.init_oracle_client(lib_dir = r"C:\oracle\instantclient_21_13")

connection = cx_Oracle.connect(user="system", password="Shraddha", dsn="localhost/xe")
cursor = connection.cursor()

sql_insert_data = """
insert into department(dcode, name, location) 
VALUES ('DS', 'SEDS', 'AB1 BUILDING')
"""

cursor.execute(sql_insert_data)

connection.commit()
cursor.close()
connection.close()

print("Table inserted successfully")