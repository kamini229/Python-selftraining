"""
File I/O
'w' -> Write-Only Mode
'r' -> Read_Only Mode
'r+' -> Read And Write Mode
'a' -> Append Mode
"""

# write function always takes a string argument

my_list = [1, 2, 3]

my_file = open("firstfile.txt", "w")

for item in my_list:
   # my_file.write(str(item))
    my_file.write(str(item) + "\n")

my_file.close()