class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    #   Class Constructor
    def __init__(self, firstName, lastName, idNumber, scores):
        super().__init__(firstName, lastName, idNumber)
        if scores is None:
            self.scores = []
        else:
            self.scores = scores
   
    def calculate(self):
        avg = 0
        n = len(self.scores)
        for i in self.scores:
            avg += i
        avg /=n
        if avg >=90 and avg <=100:
            return 'O'
        elif avg < 90 and avg >=80:
            return 'E'
        elif avg <80 and avg >=70:
            return 'A'
        elif avg < 70 and avg >=55:
            return 'P'
        elif avg <55 and avg >= 40:
            return 'D'
        else:
            return 'T'

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
