#single inhertance


from re import L


class  employee:
    no_of_leaves=8
    var=8
    def __init__(self,name,salary,role) -> None:
        self.name=name
        self.salary=salary
        self.role=role


    def printdetails(self):
        return f"The name is {self.name}.salary is {self.salary} and role is {self.role}"
  
    @classmethod
    def change_leaves(cls,newleaves):
        cls.no_of_leaves=newleaves
    
    @classmethod
    def form_dash(cls,string):
        # parms=string.split("-")
        # return cls(parms[0],parms[1],parms[2])
        return cls(*string.split("-"))

        
#   A static method is also a method that is bound to the class and not the object of the class.
# A static method can’t access or modify the class state.
# It is present in a class because it makes sense for the method to be present in class.
    @staticmethod
    def printgood(string):
        print("this is good " + string)
 

class Player:
    var=9
    no_of_games=4
    def __init__(self,name,game):
        self.name=name
        self.game=game

    def printdetails(self):
        return f"The name is {self.name}.game is {self.game}"

class coolprgrammer(employee,Player):

    language="c++"
    def printlanguages(self):
        print(self.language)

harry = employee("shubhum",555,"Programmer")
rohan = employee("karan",777,"Programmer")

shubhum =Player("shubhum",["cricket"])

karan =coolprgrammer("karan",89998,"coolprogrammer")
det=karan.printdetails()
karan.printlanguages()
print(karan.var)
#print(det)