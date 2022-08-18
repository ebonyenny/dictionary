import sqlite3
# print("Imported successfully!")

#Connect to a database
conn = sqlite3.connect('Sales_db')
# print("Connected successfully!")

#Create a cursor object
curs = conn.cursor()
# print("Cursor connected successfully!")

#format output to display in a tabular form
items = curs.fetchall()
# print("item_ID"+ "\t\tname"+ "\t\t\tcost_price"+ "\t\t\tquantity_in_stock" "\n" f"{'.' * 80}") 

#looping through the items
for item in items:
    item_id, product_des, cost_price, quantity_in_stock = item
    # print(f"{item_ID}\t\t{name}\t\t\t{cost_price}\t\t\t{quantity_in_stock}")

#Calculating the amount the business owner invested in the procurement of the items.
curs.execute("SELECT SUM(cost_price) FROM inventory_data")
item = curs.fetchall()
print("The amount the business owner invested in the procurement of the items: ",item)

#Calculating the average quantity of items in stock
curs.execute("SELECT AVG(quantity_in_stock) FROM inventory_data")
item = curs.fetchall()
print("The average quantity of items in stock: ",item)

#Calculating the item with the least quantity in stock
curs.execute("SELECT name, MIN(quantity_in_stock) FROM inventory_data")
item = curs.fetchall()
print("The item with the least quantity in stock: ",item)

#Calculating the item with the most quantity in stock
curs.execute("SELECT name, MAX(quantity_in_stock) FROM inventory_data")
item = curs.fetchall()
print("The item with the most quantity in stock: ",item)

#commit the database and table
conn.commit()

#close the connection to the database
conn.close()


