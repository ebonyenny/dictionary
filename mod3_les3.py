#create a class students
from typing_extensions import Self


class Students:
    def __init__(self, first, last, email, rollNo):
        self.first=first
        self.last=last
        self.email=first+"."+last+"@stutern.com"

#create class group_leader that inherits from class students
class Group_leader(Students):
    pass

#Define a method that adds students to the list of student under the group leader.
    def add(self):
        self.append()
        print('updated list:', self)

 #Define a method that removes students from the list of students under the group leader.   
    def remove(self):
        self.pop()
        print('updated list:', self)

#Define a method that prints out the full names of students in the list of students under group leader.

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
       

#Create 3 more instances of the parent class we defined in the practical session
Stud1 = Students('Eniola', 'Osadare')
Stud2 = Students('Faith', 'Amure')
Stud3 = Students('Eke', 'Ihuoma')

#Create 2 instances of the sub class you created
Leader1 = Group_leader() 
Leader1 = []
Leader2 = Group_leader()
Leader2 = []

#Add 2 students each to the list of students under the instances of your subclass
Leader1.add(Stud1, Stud2)
Leader2.add(Stud3, Stud2)

#Remove 1 student each from the list of students under the instances of your subclass
Leader1.remove(Stud2)
Leader2.remove(Stud2)

#Print the fullname of the students in the list of students under the instances of your subclass.
for Leader1 in range(Leader1-1, -1, -1):
    print(Leader1.fullname)

for Leader2 in range(Leader2-1, -1, -1):
    print(Leader2.fullname)

#Print the email of the instances of your subclass.


