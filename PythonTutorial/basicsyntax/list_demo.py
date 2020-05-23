"""
Data type to store more than one value in one variable name
List items are in bracket, seprated with ","   [1, 2, 3]
"""
cars =["BMW", "HondaCity", "Audi"]
emptylist = []

print(emptylist)
print(cars)

print("*#"*20)
print(cars[0])
print(cars[1])

num_list = [1, 2, 3]
sum_list = num_list[0] + num_list[1]
print(sum_list)

more_cars =["BMW", "HondaCity", "Audi"]
print(more_cars)
print(more_cars[1])

more_cars[1] = "Benz"
print(more_cars[1])

print(more_cars)