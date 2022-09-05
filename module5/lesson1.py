import sqlite3

#check
print("successfully imported module")

conn = sqlite3.connect("Sales.db")

#check 
print("Database created successfully!") ; print(type(conn))

cursor=conn.cursor()

#check
print("cursor created successfully \n", type(cursor))

# cursor.execute("""
#                 CREATE TABLE inventory_list (
#                  item_id INTEGER,
#                    product_des text,
#                     cost_price REAL,
#                    quantity_in_stock INTEGER                   
#                     )
#    """)

inventory_data = [( '1','40 Leaves','340','3'), ('2','Ruler','50','10'), ('3','Biro','30','30'), ('4','Pencil','20','4'),
('5','Text-book','1500','10'), ('6','Staplers','500','1'), ('7','Mouse-pads','7000','2'), ('8','Battries','1000','30'),
('9','60 Leaves','600','30'), ('10','Pen','80','4')]

#cursor.executemany("INSERT INTO inventory_list VALUES(?,?,?,?)", inventory_data)

cursor.execute("""SELECT * FROM inventory_list
            WHERE quantity_in_stock < 20
            ORDER BY cost_price DESC;
            """
            )
item = cursor.fetchall()
print("Please see the list of Items to restock", item)
#commit"
conn.commit()

#close
conn.close()
