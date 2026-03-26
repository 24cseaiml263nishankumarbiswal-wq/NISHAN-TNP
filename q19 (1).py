#Flatten a nested list.

l = [[1,2],[3,4],[5]]

flat = []

for i in l:
    for j in i:
        flat.append(j)

print(flat)