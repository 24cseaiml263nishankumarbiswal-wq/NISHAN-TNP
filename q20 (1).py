#Find all pairs with a given sum. 

l = [1,2,3,4,5]
s = 5

for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i] + l[j] == s:
            print(l[i], l[j])