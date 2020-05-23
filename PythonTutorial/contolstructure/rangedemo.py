"""
Built-in function
Creates a sequence of numbers but not save them in memory
Very useful in generating numbers
"""

print(list(range(0, 10)))

# a = range(20 )
# a = range(12, 100)

a = range(0, 40, 2)
print(a)
print(type(a))

print(list(a))
print('*'*20)

l = [1, 2, 3]
for num in l:
    print(num)

print('*'*20)

for num in range(3):
    print(num)

print('*'*20)

for num in range(1, 4):
    print(num)