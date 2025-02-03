

# in python we dont have return types mentioned during method declarations

def demoFun():
    print("demo function")

demoFun()

#---------

def sumDemo(x,y):
    return(x+y)


sum= sumDemo(12,13)
print(f"Addition is  {sum}")

#------------

def arrayFun(*data):
    for args in data:
        print( args)

arrayFun(12,13,14,15)