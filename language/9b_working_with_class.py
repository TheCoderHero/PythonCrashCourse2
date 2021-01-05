class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        # When we create a new car, it has 0 miles on it
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    # Method to update attribute
    def update_odometer(self, milage):
        self.odometer_reading = milage

    # Method to increment an attribute
    def increment_odometer(self, miles):
        self.odometer_reading += miles
    
new_car = Car('honda', 'civic', 2017)
print(new_car.get_descriptive_name())
new_car.read_odometer()

# Modify an attribute directly
new_car.odometer_reading = 33987
new_car.read_odometer()

# Modify an attribute using a method
new_car.update_odometer(23098)
new_car.read_odometer()

new_car.increment_odometer(100)
new_car.read_odometer()