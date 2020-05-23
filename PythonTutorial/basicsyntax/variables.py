"""
table
object reference count
"""

a = "kyc"
b = "kyc"

print(a)

a = 123

print(a)
print(b)

b = 456
print(b)

c = 'kyc'
d = c

print(c == d)
print(d is c)