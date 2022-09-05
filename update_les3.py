
class student:
    def __init__(self, vnaam, anaam, nummer, geboorte, mail, cijfer):
        self.vnaam = vnaam
        self.anaam = anaam
        self.mail = mail
        self.nummer = nummer
        self.geboorte = geboorte
        self.cijfer = cijfer
        self.cijfers = []

    def mailadres(self):
        mailadres = self.nummer + "@rocfriesepoort.nl"
        mailadres = mailadres.replace(' ', "")
        mailadres = mailadres.lower()
        return mailadres

    def cijfervullen(self):
        self.cijfers.append(self.cijfer)

    def gemiddelde(self):
        gemid = (sum(self.cijfers) / len(self.cijfers))
        return gemid

student1 = student("Peter", "Veelsma", "123456", "23/4/2003", "", 8)
student2 = student("Anna", "Grijpstra", "325764", "11/9/2004", "", 7)
student3 = student("Bart", "van Tongeren", "876352", "9/11/2001", "", 5)

studenten = [student1, student2, student3]

for x in studenten:
    x.mail = (x.mailadres())
    x.cijfervullen()
    print(x.vnaam, x.anaam, "-", x.nummer, "-", x.mail, "-", x.geboorte, "-", "Cijfer

    #gemiddelde is an instance method. To call it, you need an instance:

print(student1.gemiddelde())