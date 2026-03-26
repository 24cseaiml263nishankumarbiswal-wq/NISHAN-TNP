#Find the sum of digits of a number. 

n = 1234
s = 0

while n > 0:
    s += n % 10
    n //= 10

print(s)