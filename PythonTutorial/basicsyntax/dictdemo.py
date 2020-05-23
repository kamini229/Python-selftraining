"""
Data type to store more than one value in one variable name, in terms of key value pair
Dictionary items are in brackets {} in key:value pairs, separated with "," {'k1':'v1' , 'k2':'v2'}
No sequenced , no indexing  -> mapping
"""

car = {'make':'BMW', 'model':'550i','year':2016}
print(car)

print(car['make'])

model = car['model']
print(model)
print('*#'*20)
d = {}

d['one'] = 1
d['two'] = 2

print(d)
print('*#'*20)

sum_1 = d['two'] + 8
print(sum_1)
print(d)

print('*#'*20)
d['two'] = d['two'] + 8
print(d)