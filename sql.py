import sqlite3
from car import Car
conn = sqlite3.connect("cars.db")
car1 = Car("C2150","Mec",1969)
c =conn.cursor()
sql_create_table = """
    CREATE TABLE cars (
    name text,
    brand text,
    year integer
     )
"""
sql_insert = f"""
    INSERT INTO cars VALUES ("{car1.name}", "{car1.brand}", {car1.year})
"""
sql_insert1 = f"""
    INSERT INTO cars VALUES (?, ?,?)
"""

#c.execute(sql_create_table)

sql_select = """
    SELECT * FROM cars WHERE brand = "Mec"
"""
sql_update = """
    UPDATE cars set name = "Fadin"  WHERE brand = "Vin"
"""

sql_delete = """
    DELETE FROM cars WHERE brand = "Vin"
"""
try:
    #c.execute(sql_insert)
    c.execute(sql_insert1,(car1.name,car1.brand,car1.year )) # Cach thu 2
    conn.commit()
    #c.execute(sql_update)
    #conn.commit()
    #c.execute(sql_delete)
    #conn.commit()
    c.execute(sql_select)
    print(c.fetchall())
except:
    print("Query error!!")
conn.close()