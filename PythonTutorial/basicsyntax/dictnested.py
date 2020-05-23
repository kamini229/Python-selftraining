"""
Nested Dictionary:
d = {'k1':{'nestk1':'nestvalue1' ,'nestk2':'nestvalue2' }}
d['k1']
"""

cars = {'BMW':{'model':'550i','year':2016},'Benz':{'model': 'E350', 'year': 2015}}

BMW_year = cars['BMW']['year']
print(BMW_year)

print(cars['Benz']['model'])