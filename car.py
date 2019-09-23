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

# developed by dave
    def brake(self):
        if Car.isStarted(self):
            Car.speed = Car.speed - 5
            return True
        else:
            print("car must be on")
            return False