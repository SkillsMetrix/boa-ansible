userAge = input("Please enter your Age: ")

age=int(userAge)
if age<=0:
    print('Enter Valid Age')
elif age <=18:
    print("You are not allowed to vote")
elif age>18 and age<70:
    print("You are allowed")
else:
    print("You are Senior citizon") 
    