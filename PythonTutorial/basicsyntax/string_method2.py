# Example to show available string methods in python

# Replace method

a = "1abc2abc3abc4abc"
print(a.replace('abc', 'ABC'))

# Substring
# Starting index is inclusive
# Ending index is Exclusive

sub = a[0:6]
step = a[1:6:2]
print("**************")
print(sub)
print("**************")
print(step)
print("**************")
step2 = a[-1]
print(step2)
print("**************")
step3 = a[:-1]
print(step3)
print("**************")
step4 = a[::2]
print(step4)
print("**************")


# reverse string
b = "This is the string"
step5 = b[::-1]
print(step5)

print(a[0])
print(b[0])