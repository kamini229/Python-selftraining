"""
Data type to store more than one value in one variable name
List items are in bracket, seprated with ","   [1, 2, 3]
"""
cars =["BMW", "HondaCity", "Audi"]
length = len(cars)
print(length)

cars.append("Benz")
print(cars)

cars.insert(1 , "Jeep")
print(cars)

x = cars.index("Benz")
print(x)

# pop - bydefault works for removing the end

y = cars.pop()
print(y)
print(cars)

cars.remove("Jeep")
print(cars)
print("*#"*20)

slicing = cars[0:2]
print(slicing)
a = cars[1:]
print(a)

print("*#"*20)

print(cars)
cars.sort()
print(cars)