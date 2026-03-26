#Count frequency of elements in a list. 

l = [1,2,2,3,1]

d = {}

for i in l:
    d[i] = l.count(i)

print(d)