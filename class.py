class car:
    wheels=4

    #Constructer(used to create Objects)
    def __init__(self,brand,model):
        self.brand=brand #instance attribute
        self.model=model #instance attribute
    
    #Method(action)
    def display_info(self):
        print(f"{self.brand} {self.model} has {self.wheels} wheels")

#creating an object for a class
my_car=car("Toyota","Corolla")

#calling a Method
my_car.display_info()