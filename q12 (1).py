#Remove duplicates from a list (without set). 

l = [1,2,2,3,4,4]
new = []

for i in l:
    if i not in new:
        new.append(i)

print(new)