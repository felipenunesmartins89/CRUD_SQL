import pyodbc

def read(conn):
    print("Read")
    cursor = conn.cursor()
    cursor.execute("select * from dummy")
    for row in cursor:
        print(f'row = {row}')

conn = pyodbc.connect(
    "Driver={SQL Server Native Cliente 11.0;"
    "Server=187.21.241.46;"
    "Database=_teste;"
    "Trusted_connection=yes;"
)

read(conn)
create(conn)
update(conn)
delete(conn)

