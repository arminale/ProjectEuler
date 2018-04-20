# https://projecteuler.net/problem=50 Consecutive prime sum

from util.useful_math import getPrimes

# generate a list of primes under 1 000 000
upperBound = 1000000
primes = getPrimes(upperBound)
print("Primes Generated")

sequenceSum = 0 # running sum of the sequence of primes. may or may not be a prime itself
tempLength = 0 # running length of the sequence. may or may not sum to a prime
sequenceLength = 0 # length of the portion of the current sequence of primes that DO sum to a prime
maxSequenceLength = 0 # running length of the longest sequence of primes that sum to a prime
bigPrime = 0 # the prime up to which the longest sequence sums
numberOfPrimes = len(primes)

# starting from the first prime, construct sequences consecutive of primes that may or may not sum to a prime
for i in range(numberOfPrimes):
    for j in range(i, numberOfPrimes):
        sequenceSum += primes[j]
        if sequenceSum >= upperBound:
            break

        tempLength += 1

        if tempLength > maxSequenceLength:
            # very important optimization! only checks a sequence when it can improve on the global best
            if sequenceSum in primes:
                sequenceLength = tempLength
                if sequenceLength > maxSequenceLength:
                    maxSequenceLength = sequenceLength
                    bigPrime = sequenceSum
    sequenceLength = 0
    sequenceSum = 0
    tempLength = 0

print(bigPrime)
print(maxSequenceLength)