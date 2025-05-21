class Building:
    year = None
    city = None

    def __init__(self , year = None , city = None):
        self.year = year
        self.city = city

    def get_data (self):
        print("Year: " , self.year , ". City: " , self.city)    

class House(Building):
    people = 0

    def __init__(self, year=None, city=None , people = 0):
        super(House , self).__init__(year, city)
        self.people = people

    def get_data(self):
        super().get_data()
        print("Peoplt: " , self.people)    

class School(Building):
    pupils = 0
    
    def __init__(self, year=None, city=None , pupits = 0):
        super(School , self).__init__(year , city)
        self.pupils=pupits

    def get_data(self):
        super().get_data()
        print("Pipils: ", self.pupils)

class Shop(Building):
    pass

house = House(2025 , "moscow" , 125)
house.get_data()
school = School(2025 , "moscow" , 1000)
school.get_data()
shop = Shop(2025 , "moscow")