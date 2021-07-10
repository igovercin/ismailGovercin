# Fill in this file with the code from parsing JSON exercise

import json

f=open('myfile.json',)
data=json.load(f)
f.close()


print(data["kimlik"]['Ad'])
print(data["kimlik"]['Soyad'])