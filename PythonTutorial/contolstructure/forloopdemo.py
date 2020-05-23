"""
Execute statement repeatedly
Conditions are used to stop the execution of loop
Iterable items are Strings, list, Tuple, Directory
"""
my_string = 'abcabc'

for x in my_string:
    if x == 'a':
        print('A', end=' ')
    else:
        print(x, end=' ')
print('*'* 20)
print()

# list
cars = ['BMW', 'Honda', 'Audy']

for car in cars:
    print(car)

print('*'* 20)
nums = [1, 2, 3]
for n in nums:
    print(n)
    print(n * 10)

# Dictionary

print('*'* 20)
d = {'one': 1, 'two': 2, 'three': 3}
for k in d:
    print(k + " " + str(d[k]))
print('*'* 20)

for k,v in d.items():
    print(k)
    print(v)