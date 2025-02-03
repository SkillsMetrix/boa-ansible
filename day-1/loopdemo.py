
#[] -> array
userNames=['admin','manager','qa']

for uname in userNames:
    print(uname)

users=['user1','user2','user3']

for i ,data in enumerate(users):
    print(i , data)

#------------------------------

projectTypes=['HRMS','IT','Banking','Finance']

dummy=[]

for project in projectTypes:
    if project =='Banking':
        continue
    else:
        print(f"Developing Project {project}")
dummy.append('Banking')
print(f" Developed {dummy}")