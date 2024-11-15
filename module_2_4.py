numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
counter = 0

for i in numbers:
    for j in range(1, i+1):  # i+1 - the maximum value of the divisor for a given number
        if i % j == 0:
            counter += 1     # the counter of the number of divisions

    if counter == 2:
        primes.append(i)
    if counter >= 3:
        not_primes.append(i)

    counter = 0

print("Primes:", primes)
print("Not_primes:", not_primes)
