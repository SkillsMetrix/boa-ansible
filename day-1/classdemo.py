
# class declaration
class Employee:
    name='SAM'
# creating an object
emp=  Employee()
# acccess the object
print(f"Employee name {emp.name}")

#--------creating constructor-------

class Employee:
 
   
    #constructor initialization

    def __init__(self, name, age):
        self.name = name
        self.age = age
    #convert object into human readbale string
    def __str__(self):
        return f" user name {self.name} and age is {self.age}"

emp= Employee("Buddy",30)

print(f"{emp}")