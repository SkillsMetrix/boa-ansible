
class Student:
    def __init__(self, rollno,name,subject,totalMarks):
        self.name = name
        self.rollno = rollno
        self.subject = subject
        self.totalMarks = totalMarks
    
    def displayData(self):
        print(f"the name is {self.name} and subject is {self.subject}")
    
    def __str__(self):
        return f"{self.name} and {self.rollno} ad totalMArks is {self.totalMarks}"

sanya= Student("199","sanya","Physics","89")

suresh= Student("198","suresh","Maths","90")

print(sanya)
print(suresh.displayData())