#Find the largest element in a list.

print("Min:", min(l))
print("Max:", max(l))

l = [2, 5, 1, 9, 3]
largest = l[0]

for i in l:
    if i > largest:
        largest = i

print("Largest:", largest)