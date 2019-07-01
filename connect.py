import pyodbc

conn = pyodbc.connect(
    "Driver={SQL Server};"
    "Server=187.21.241.46;"
    "Database=_teste;"
    "uid=_teste;pwd=_teste")

def read(conn):
    print("Read")
    cursor = conn.cursor()
    cursor.execute("select * from dummy")
    for row in cursor:
        print(f'row = {row}')

def create(conn):
    print("Create")
    cursor = conn.cursor()
    cursor.execute(
        'insert into dummy(a,b) values(?,?);',
        (3232, 'Felipe')
    )
    conn.commit()
    read(conn)

def update(conn):
    print("Update")
    cursor = conn.cursor()
    cursor.execute(
        'update dummy set b = ? where a = ?;',
        ('dogzzz', 3232)
    )
    conn.commit()
    read(conn)

def delete(conn):
    print("Update")
    cursor = conn.cursor()
    cursor.execute(
        'delete from dummy where a > 5'
    )
    conn.commit()
    read(conn)


print(read(conn))

