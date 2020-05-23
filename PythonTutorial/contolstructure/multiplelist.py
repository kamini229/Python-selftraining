"""
Itereting multiple list at the same time usind=g ZIP function
"""
l1 = [1, 2, 3]
l2 = [6, 7, 8, 10, 20, 34]

for a,b in zip(l1, l2):
    print(a)
    print(b)

print('*'*20)

for a,b in zip(l1, l2):
    if a > b:
        print(a)
    else:
        print(b)