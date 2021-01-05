# Super Class
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, milage):
        self.odometer_reading = milage

    def increment_odometer(self, miles):
        self.odometer_reading += miles
    
    # Overriding a method from the parent class
    def fill_gas_tank(self):
        print("This car's gas tank is now full.")

# Super Class
class Battery:
    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}--kWh battery.")

    def get_range(self):
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on a full charge.")

# Sub Class
class ElectricCar(Car):
    def __init__(self, make, model, year):
        # super() is a special method that allows you to call a method from the parent
        # in this case, we are calling the __init__ function from Car
        super().__init__(make, model, year)
        # Using a Class as an attribute
        self.battery = Battery()

    # Overriding a method from the parent class
    def fill_gas_tank(self):
        print("This is an Electric Car and does not need gas.")

tesla = ElectricCar('tesla', 'model s', 2019)
print(tesla.get_descriptive_name())
# Using a Class and an attribute
tesla.battery.describe_battery()
tesla.battery.get_range()
tesla.fill_gas_tank()