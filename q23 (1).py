#Print all prime numbers in a range.

for n in range(2, 20):
    prime = True

    for i in range(2, n):
        if n % i == 0:
            prime = False

    if prime:
        print(n)