# Constructor by Matt McCarthy
class Car:
    speed = 0
    started = False

    def start(self):
        self.started = True

    def isStarted(self):
        return self.started
# Developed by Thomas

    def accelerate(self):
        if Car.isStarted(self):
            Car.speed = Car.speed + 5
            return True
        else:
            return False
# developed by Thomas

    def show_speed(self):
        return Car.speed


newCar = Car()
newCar.start()
print(newCar.isStarted(), "\nSpeed is:", newCar.show_speed())

while newCar.speed != 30:
    newCar.accelerate()
print("Car has accelerated to :", newCar.show_speed())


