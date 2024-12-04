class Vehicle : 
    def __init__(self,name,max_speed,mileage):
        self.name = name 
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass 

school_busses = Bus("Mercedez Benz",190,18)

print("Name of Vehicle", school_busses.name)
print("Speed of Vehicle", school_busses.name)
print("Mileage of Vehicle", school_busses.name)



  