#import Car from car.py
from car import Car

# Developed by Matt McCarthy
newCar = Car()
newCar.start()
# developed by Thomas
print(newCar.isStarted(), "\nSpeed is:", newCar.show_speed())
while newCar.speed != 30:
    newCar.accelerate()
print("Car has accelerated to :", newCar.show_speed())

# developed by dave
newCar.brake()
newCar.brake()
newCar.brake()
newCar.brake()

print("speed: ", newCar.show_speed())
