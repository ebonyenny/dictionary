import sqlite3

#check
print("successfully imported module")

conn = sqlite3.connect("SGA_1_3_learners.db")

#check 
print("Database created successfully!") ; print(type(conn))

cursor=conn.cursor()

#check
print("cursor created successfully \n", type(cursor))

cursor.execute("""
               CREATE TABLE students (
                    first_name text,
                    last_name text,
                    email  text
                   
                   )
    """)

mygroup_list = [("Deborah", "Olorunnishola", "deboraholuwatobi247@gmail.com"),
  	("Eniola", "Osadare", "dorcasosadare@gmail.com"), ("Gideon", "Uko", "ukogideon13@gmail.com"),
 	("Joyce", "Ezeonwu", "joyceokore@gmail.com"), ("Kehinde", "Orolade", "kehindeorolade@gmail.com"),
    ("Idowu", "Adesanya", "idsworld22@yahoo.com")]

cursor.executemany('INSERT INTO students VALUES(?, ?, ?)', mygroup_list)

#check
print("We have inserted your group data into data science class", cursor.rowcount )

cursor.execute("SELECT * FROM student")

#commit
conn.commit()

#close
conn.close()
