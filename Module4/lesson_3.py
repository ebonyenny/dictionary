import sqlite3

#check
print("successfully imported module")

conn = sqlite3.connect("student.db")

#check 
print("Database created successfully!") 

curs=conn.cursor()

#check
print("Cursor connected successfully")

# curs.execute("""
#                CREATE TABLE students_d (
#                     First text,
#                     Last text,
#                     Email text
                   
#                    )
#     """)

# students_list = [("Deborah", "Olorunnishola", "deboraholuwatobi247@gmail.com"),
#   	("Eniola", "Osadare", "dorcasosadare@gmail.com"), ("Gideon", "Uko", "ukogideon13@gmail.com"),
#  	("Joyce", "Ezeonwu", "joyceokore@gmail.com"), ("Kehinde", "Orolade", "kehindeorolade@gmail.com"),
#     ("Idowu", "Adesanya", "idsworld22@yahoo.com")]

# curs.executemany("INSERT INTO students_d VALUES(?,?,?)", students_list)

#check
print("We have inserted your group data into data science class")

conn.commit()

curs.execute("SELECT * FROM students_d")
#print("query executed successfully")

#format output to display in tabular form 
item = curs.fetchall()
print('First' + '\t\tLast' + '\t\tEmail')
print('-----------' + '\t\t------------' '\t\t--------')

for item in item:
    print(item[0] + "\t\t\t" + item[1] + "\t\t\t " + item[2])

#commit
#conn.commit()

#curs.execute("ALTER TABLE students_d RENAME to new_students")

#curs.execute("ALTER TABLE new_students ADD column DOB")
print("new column added")

#updating new column DOB with details
#curs.execute("UPDATE new_students SET DOB = '3010'")
#commit
#conn.commit()

#curs.execute("SELECT * FROM new_students")
#print("query executed successfully")

#format output to display in tabular form 
item = curs.fetchall()
print('First' + '\t\tLast' + '\t\tEmail' + '\t\tDOB')
print('-----------' + '\t\t------------' '\t\t--------' '\t\t------')

for item in item:
    print(item[0] + "\t\t\t" + item[1] + "\t\t\t " + item[2]  + "\t\t\t " + item[3] )
#commit
conn.commit()

#close
conn.close()
