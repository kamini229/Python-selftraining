"""
https://docs.python.org/3/library
"""

import math
from math import sqrt

#import Object_Demo.cars as car
from Object_Demo import cars
from Object_Demo.cars import info

class ModulesDemo():

    def builtin_modules(self):
        print(math.sqrt(100))
        print(sqrt(100))

    def car_description(self):
        make = "bmw"
        model = "550i"
        cars.info(make, model)
        info(make, model)


m = ModulesDemo()
m.builtin_modules()
m.car_description()