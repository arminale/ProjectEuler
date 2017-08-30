from math import sqrt
primes = []
squares = [0]
upperBound = 1000000
numbers = [True] * (upperBound + 1)
for i in range(2, int(sqrt(upperBound) + 1)):
    if numbers[i]:
        for j in range(i * 2, upperBound + 1):
            if j % i == 0:
                numbers[j] = False
for i in range(2, upperBound + 1):
    if numbers[i]:
        primes.append(i)
for i in range(1, 5001):
    squares.append(i ** 2)
for i in range(9, 4000000, 2):
    print(i)
    if i not in primes:
        flag = False
        for j in primes:
            if j < i:
                for k in squares:
                    if j + 2 * k == i:
                        flag = True
                    elif j + 2 * k > i:
                        break
            else:
                break
        if not flag:
            print(i)
            break