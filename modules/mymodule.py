

person1= {
           "name":"FELIX",
           "age": "22",
           "country": "KE"
          }

import mymodule as fx

a = fx.person1["age"]

import platform

b= platform.system()

b = dir(platform)


from mymodule import person1

print("Hello ," +   person1["name"] +   "of" +   "Kenya")