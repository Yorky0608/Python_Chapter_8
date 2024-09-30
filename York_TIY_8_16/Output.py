import Function

print(Function.car_specs('Honda', 'Civic', Milage = 33, Doors = 4))

import Function as f

print(f.car_specs('Honda', 'Civic', Milage = 33, Doors = 4))

from Function import car_specs

print(car_specs('Honda', 'Civic', Milage = 33, Doors = 4))

from Function import car_specs as cs

print(cs('Honda', 'Civic', Milage = 33, Doors = 4))

from Function import *

print(car_specs('Honda', 'Civic', Milage = 33, Doors = 4))