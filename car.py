# Constructor by Matt McCarthy
class Car:
    speed = 0
    started = False

    def start(self):
        self.started = True

    def isStarted(self):
        return self.started

    def accelerate(self):
        if isStarted():
            Car.speed = Car.speed + 5
            return True
        else:
            return False