class Dog:
    name = None 
    age = None
    hangry = None

    def set_data(self , name , age , hangry):
        self.name= name
        self.age = age
        self.hangry = hangry
    def get_data(self):
        print(self.name , self.age , self.hangry) 

class Cat:
    name = None
    age = None
    isHealth = None

    def __init__(self , name= None , age = None , isHealth = None):
        self.set_data(name,age,isHealth)
        self.get_data()
    def set_data(self, name = None, age = None ,isHealth = None):
        self.name=name
        self.age=age
        self.isHealth=isHealth
    def get_data(self):
        print (self.name , self.age , self.isHealth)         

dog1 = Dog()
dog1.set_data("Roman" , 22 , False)

dog2 = Dog()
dog2.set_data("Ralf" , 18 , True) 

cat1=Cat("Barsik" , 7 , True)

dog1.get_data()
dog2.get_data()
