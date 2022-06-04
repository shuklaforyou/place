import re
from importlib_metadata import pass_none


class Employee:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        # self.email=f"{fname}.{lname}@codewithabhi.com" 

    def explain(self):
        return f"This is employee is {self.fname} {self.lname}"

    @property
    def email(self):
        if self.fname==None or self.lname==None:
            return f"this is not  set. Please set it using setters"
        return f"{self.fname}.{self.lname}@codewithabhi.com" 
 
    @email.setter
    def email(self,string):
        print("stting.now")
        names=string.split("@")[0] 
        self.fname=names.split(".")[0]
        self.lname=names.split(".")[1]
    
    @email.deleter
    def email(self):
        self.fname=None
        self.lname=None

skillf=Employee("skill","F")

print(skillf.email)
o="this is string"

print(dir(skillf))


import inspect
print(inspect.getmembers(skillf))