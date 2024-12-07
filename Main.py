class vehicle:
    def __init__(self,name,maxspeed,mileage):
        self.name = name
        self.maxspeed = maxspeed
        self.mileage = mileage

class bus(vehicle):
    pass

v1 = bus("Tesla","I don't know",55)
print("Taseen's fav car is",v1.name)
v2 = bus("BMW","I don't know",55)
print("Vedanshi's fav car is",v2.name)














