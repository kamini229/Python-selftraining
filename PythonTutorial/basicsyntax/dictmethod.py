"""
Dictionary method
"""

car = {'make':'BMW', 'model':'550i','year':2016}
cars = {'BMW':{'model':'550i','year':2016},'Benz':{'model': 'E350', 'year': 2015}}

print(car.keys())
print(cars.keys())
print(car.values())
print(cars.values())
print(car.items())

print("*****************")
car_copy =car.copy()
print(car_copy)
print("*****************")
"""   
car.clear()
print(car)
"""
print(car.pop('model'))
print(car)

