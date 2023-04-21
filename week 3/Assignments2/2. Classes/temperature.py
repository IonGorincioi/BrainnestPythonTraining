# Create a class called Temperature that has attribute celsius
# (a temperature in degrees Celsius). Add methods to_fahrenheit
# and to_kelvin that convert the temperature to degrees Fahrenheit
# and Kelvin, respectively.
class Temperature:

    def __init__(self, celsius):
        self.celsius = celsius

    def to_fahrenheit(self):
        return 9 * self.celsius / 5 + 32

    def to_kelvin(self):
        return self.celsius + 273.15


temp_in_fahrenheit = Temperature(35)
print(f"{temp_in_fahrenheit.to_fahrenheit()}°F")
print(f"{temp_in_fahrenheit.to_kelvin()}°K")
