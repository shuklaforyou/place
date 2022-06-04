class cars():
    def __init__(self,modelname,year,price):
        self.modelname=modelname
        self.year=year
        self.price=price

    def price(self):
        self.price=int(self.price*1.15)


    def email(self,email):
        self.email=email    

    @property
    def pt(self):
        return "we get to you"

    



honda =cars("citiy",2017,100000)
tata= cars("bolts",2016,60000)
print(honda.year)
print(honda.price)

honda.email="th.pt@gmail.com"
print(honda.email)

del honda.email
print(honda.email)
