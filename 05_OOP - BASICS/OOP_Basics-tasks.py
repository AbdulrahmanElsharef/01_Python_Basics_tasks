class Vehicle:
     color="white"
     def __init__(self,name,max_speed, min_speed):
          self.name=name
          self.max_speed = max_speed
          self.min_speed = min_speed
     def average_sp(self):
          avr = (self.max_speed+self.min_speed)/2
          return avr
     def seating_capacity(self, capacity=50):
          return f"The seating capacity of a {self.name} is {capacity} passengers"


class Bus(Vehicle):
     pass


class Car(Bus):
     pass



car_1 = Vehicle("Volvo",240, 75)
print(f"car name is {car_1.name},color is {car_1.color}, max is {car_1.max_speed} and min is  {car_1.min_speed}")
print(f"average is {car_1.average_sp()}")
print(car_1.seating_capacity(6))



print("_________________________________________________________")
bus_1 = Bus("Mersedce", 180, 60)
bus_1.color = "blue"
print(f"car name is {bus_1.name},color is {bus_1.color},max is {bus_1.max_speed} and min is  {bus_1.min_speed}")
print(f"average is {bus_1.average_sp()}")
print(car_1.seating_capacity())
print(type(bus_1))
print(isinstance(bus_1, Vehicle))





