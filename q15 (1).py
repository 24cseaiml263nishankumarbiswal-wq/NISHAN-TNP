#Find the intersection of two lists.

a = [1,2,3]
b = [2,3,4]

c = []

for i in a:
    if i in b:
        c.append(i)

print(c)