"""
with / As keyword
"""
"""

print("Normal write Start")
my_write = open("textfile.txt", "w")
my_write.write("Trying to write to the file")
my_write.close()

print("Normal Read Start")
my_read = open("textfile.txt", "r")
print(str(my_read.read()))

"""

print("with As Write Start")
with open("withas.txt", "w") as with_as_write:
    with_as_write.write("This is an example of with as write/read")

print()
print("With As Read Start")
with open("withas.txt", "r") as with_as_readd:
    print(str(with_as_readd.read()))