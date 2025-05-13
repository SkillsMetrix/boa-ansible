

import json

data=open('user.json')

userdata=json.load(data)

for udata in userdata['emp_details']:
    print (udata)
data.close