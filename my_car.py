from car import Car

imp = Car('honda', 'civic', 2017)
print(imp.get_descriptive_name())
imp.odometer_reading = 31978
imp.read_odometer()