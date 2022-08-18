
import sqlite3

#check
#print("successfully imported module")

conn = sqlite3.connect("celebs.db")

#check 
print("Database created successfully!") 

c=conn.cursor()

#check
print("Cursor connected successfully")

# c.execute("""
#                  CREATE TABLE celebrity_1 (
#                       name text,
#                       genre text,
#                       num_albums INTEGER,
#                       age INTEGER,
#                       awards INTEGER,
#                       years_in_industry INTEGER
                   
#                      )
#      """)

# print("successful")

#inserting values to a table
data_set = [('Beyonce', 'Hip-hop', '20', '40', '5', '20'),
 ('Burna', 'Hip-hop', '10', '39', '10', '20'),
 ('Banky-W', 'RNB', '5', '42', '15', '25'),
 ('Ariana Grande', 'RnB', '10', '50', '3', '40'),
 ('Jason Durelo', 'RnB', '7', '33', '4', '10'),
 ('Rick Ross', 'Rap', '4', '40', '7', '25'),
 ('Ed Sheeran', 'Rock', '20', '35', '8', '15'),
 ('Adesuwa', 'RnB', '20', '27', '1', '6'),
 ('Rihana', 'RnB', '20', '30', '0', '3'),
 ('Adele', 'Hip-hop', '20', '32', '15', '30'),
 ('David Guetta', 'Hip-hop', '5', '3', 'TRUE', '20'),
 ('Fireboy', 'Hip-hop', '3', '39', '4', '20'),
 ('Camilla Cabelo', 'RNB', '7', '35', '6', '25'),
 ('Maroon 5', 'RnB', '8', '43', '2', '10'),
 ('Liam Payne', 'Blues', '7', '38', '0', '2'),
 ('Katty Perry', 'Hip-hop', '4', '29', '5', '20'),
 ('Pink', 'Country', '6', '48', '3', '15'),
 ('Rita Ora', 'Blues', '3', '26', '3', '10'),
 ('Jess Glyne', 'Jazz', '8', '41', '4', '15'),
 ('Asa', 'Country', '3', '35', '0', '14')]

#print("Successful")

#c.executemany("INSERT INTO celebrity_1 VALUES(?,?,?,?,?,?)", data_set)

#check
#print("Done")

#querying database
#the mopst decorated celebrity
c.execute ("""
SELECT NAME , MAX(awards)
FROM celebrity_1
""")
item = c.fetchall()
print(item)


#the oldest celebrity
c.execute ("""
SELECT NAME,MAX(age)
FROM celebrity_1
""")

item = c.fetchall()

print(item)


#the oldest celebrity in the industry
c.execute ("""
SELECT NAME , MAX(years_in_industry)
FROM celebrity_1
""")

item = c.fetchall()
print(item)


#the least no of albums
c.execute ("""
SELECT NAME , Min(albums)
FROM celebrity_1
""")

item = c.fetchall()
print(item)


#the popular genere
c.execute ("""
SELECT NAME , MAX(genre)
FROM celebrity_1
""")

item = c.fetchall()
print(item)


#commit
conn.commit()

#close
conn.close()
