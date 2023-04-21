# Create a class called Car that has attributes
# make, model, and year. Add methods start and stop
# that simulate starting and stopping the car, respectively.


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start(self):
        return f"{self.make} {self.model} from {self.year} has started."

    def stop(self):
        return f"{self.make} {self.model}'s engine has stopped"


car1 = Car("Toyota", "Verso", 2010)
print(car1.start())
print(car1.stop())
