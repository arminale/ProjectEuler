from math import sqrt


def getPrimes(upperBound):
    """ Finds all prime numbers less than a specified upper bound using an implementation of The Sieve of Eratosthenes.
    Can take a long time for large (>1 000 000) upper bounds since it is not optimized!

    :param upperBound: The upper bound of prime numbers
    :return: A list, containing all prime numbers found
    """
    primes = []
    numbers = [True] * (upperBound + 1)
    for i in range(2, int(sqrt(upperBound) + 1)):
        if numbers[i]:
            for j in range(i ** 2, upperBound + 1):
                if j % i == 0:
                    numbers[j] = False
    for i in range(2, upperBound + 1):
        if numbers[i]:
            primes.append(i)

    return primes
