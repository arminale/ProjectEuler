from math import sqrt
primes = []
longestChain = 0
ab = 0
upperBound = 100000
numbers = [True] * (upperBound + 1)
for i in range(2, int(sqrt(upperBound) + 1)):
    if numbers[i]:
        for j in range(i ** 2, upperBound + 1):
            if j % i == 0:
                numbers[j] = False
for i in range(2, upperBound + 1):
    if numbers[i]:
        primes.append(i)
print("primes generated")
for a in range(-999, 1000, 2):
    for b in range(1, 1000, 2):
        chain = 0
        for n in range(1000):
            if n**2 + a * n + b in primes:
                chain += 1
            else:
                break
        if chain > longestChain:
            longestChain = chain
            ab = a * b
print(ab)