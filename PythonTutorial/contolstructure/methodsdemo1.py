
"""
def sum_nums():
    print(3+2)

sum_nums()
"""

"""
def sum_nums(n1, n2):
    print(n1 + n2)

sum_nums(4, 6)
sum_nums(42, 6)
"""
"""
l = [1, 2, 3]
print(l.append(4))
print(l)

print(len(l))

"""

def sum_nums(n1, n2):
    return n1 + n2

sum1 = sum_nums(4, 6)
print(sum1)

print(sum_nums(42, 6))
print('*'*20)

string_add = sum_nums('one', 'two')
print(string_add)

print('*'*20)

def isMetro(city):
    l = ['abc', 'xyz', 'df']

    if city in l:
        return True
    else:
        return False

x = isMetro('abc')
print(x)