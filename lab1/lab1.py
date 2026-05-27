import sqlite3

conn = sqlite3.connect("maga.db")
cursor = conn.cursor()

cursor.execute ("""
    CREATE TABLE IF NOT EXISTS clientes (               
                nombre TEXT NOT NULL,
                telefono TEXT
                )
""")

cursor.execute ("""
    INSERT INTO clientes (nombre, telefono)
    VALUES ('ALdo Yamil', '921-233-2587')
""")

conn.commit()
conn.close()