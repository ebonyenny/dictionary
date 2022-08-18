import sqlite3
# print("Imported successfully!")

#Connect to a database
conn = sqlite3.connect('WAEC_Scores_db')
# print("Connected successfully!")

#Create a cursor object
curs = conn.cursor()
# print("Cursor connected successfully!")

table = (""" CREATE TABLE Data_SCORES(
            ID INTEGER,
            Name TEXT,
            Maths INTEGER,
            English INTEGER,
            Chemistry INTEGER,
            Physics INTEGER,
            Geography INTEGER,
            Biology INTEGER,
            History INTEGER,
            Accounting INTEGER,
            FurtherMaths INTEGER
)
""")
print("Successful")

curs.execute(table)

#open the csv file 
with open('waec_marks.csv', "r") as opened_file:
    read_file = csv.reader(opened_file)
    next(read_file)
#insert the values of the read file into the sql table
    curs.executemany("""
                    INSERT INTO waec_marks VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """, read_file)
# print("executed successfully!")

#querying the database
curs.execute("SELECT * FROM waec_marks")
print("Query executed successfully!")

# format output to display in a tabular form
items = curs.fetchall()

print("ID" + "\tNAME" + "\tMATHS" + "\tENGLISH" + "\tCHEMISTRY" + "\tPHYSICS" + "\tGEOGRAPHY" + "\tBIOLOGY" + "\tHISTORY" + "\tACCOUNTING" + "\tFURTHER_MATHS" "\n" f"{'.' * 120}")
print(items)

#looping through the items
for item in items:
    ID, Name, Maths, English, Chemistry, Physics, Geography, Biology, History, Accounting, Further_Maths = item

#The student with highest score in Maths
def highest_maths():
    curs.execute("""
    SELECT Name, MAX(Maths) FROM Data_SCORES
    """) 
    item = curs.fetchall()
    print(f"Student with the highest score in Math, {item}")
highest_maths()

#The student with lowest score in English
def lowest_in_english():
    curs.execute("""
    SELECT Name, MIN(English) FROM Data_SCORES
    """) 
    item = curs.fetchall()
    print(f"Student lowest score in English, {item}")
lowest_in_english()

#The average score of students in Maths
def average_maths():
    curs.execute("""
    SELECT AVG(MATHS) FROM Data_SCORES
    """) 
    item = curs.fetchall()
    print(f"Average score of students in Maths, {item}")
average_maths()

#The average score of students in English
def average_english():
    curs.execute("""
    SELECT AVG(English) FROM WAEC_Scores_data
    """) 
    item = curs.fetchall()
    print(f"Average score of students in English, {item}")
average_english()

#The best performing student across all nine subjects in terms of overall scores
def best_student_overall_scores():
    curs.execute("""SELECT Name, MAX(best_student)
                FROM(
                SELECT Name, SUM(Maths + English + Chemistry + Physics + Geography + Biology + History + Accounting + Further_Maths) AS "best_student"
                FROM Data_SCORES
                GROUP BY Name)
                """) 
    item = curs.fetchall()
    print(f"Best performing student across all nine subjects in terms of overall scores, {item}")
best_student_overall_scores()

#The best performing student across all nine subjects in term of average scores
def best_student_average_scores():
    curs.execute("""SELECT Name, MAX(best_student)
                FROM(
                SELECT Name, AVG(Maths + English + Chemistry + Physics + Geography + Biology + History + Accounting + Further_Maths) AS "best_student"
                FROM Data_SCORES
                GROUP BY Name)
                """) 
    item = curs.fetchall()
    print(f"Best performing student across all nine subjects in term of average scores, {item}")
best_student_average_scores()


#commit the database and table
conn.commit()

#close the connection to the database
conn.close()