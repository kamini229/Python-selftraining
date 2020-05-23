"""
Variable Scop
"""
"""
a = 10

def test_method(a):
    print("value of local 'a' is:" + str(a))
    a =2
    print("New value of local 'a' is:" + str(a))

print('value of global a is:' + str(a))

test_method(a)
print('Did the value of global a change?' + str(a))

"""
# when we use global keyword inside the function we can change the value of global variable

a = 10

def test_method():
    global a
    print("value of 'a' inside the method is:" + str(a))
    a =2
    print("New value of 'a' inside the method is changed to:" + str(a))

print('value of global a is:' + str(a))
test_method()
print('Did the value of global a change?' + str(a))