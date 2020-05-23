"""
Example to show string formatting in python
"""

city = 'Pune'
event = 'show'

print("Welcome to "+ city + " and enjoy the " + event)

# Other way to print above messege

print("Welcome to %s and enjoy the %s" %(city, event))
print("welcome to %s" %(city))
print("Enjoy the %s" %(event))