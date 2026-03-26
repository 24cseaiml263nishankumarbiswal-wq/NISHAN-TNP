#Rotate a list by k positions. 

l = [1,2,3,4,5]
k = 2

l = l[k:] + l[:k]

print(l)