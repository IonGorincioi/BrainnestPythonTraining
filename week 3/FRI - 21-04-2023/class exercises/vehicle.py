#  Create a Vehicle class with the following attributes:
#  make, model, and year. The class should also have the
#  following methods: start(), stop(), and info().

# Create a Car class that inherits from the Vehicle class.
# The Car class should have an additional attribute: num_doors.
# The class should also have the following method: lock_doors().

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start(self):
        pass

    def stop(self):
        pass

    def info(self):
        pass


class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        Vehicle.__init__(make, model, year)
        self.num_doors = num_doors

    def lock_doors(self):
        pass
