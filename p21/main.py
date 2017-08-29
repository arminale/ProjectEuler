def sumDivisors(n):
    result = 0
    for i in range(1,int(n/2) + 1):
        if n % i == 0:
            result += i
    return result
numbers = [0] * 10000
result = 0
for i in range(2,10000):
    numbers[i] = sumDivisors(i)
for i in range(2,10000):
    if numbers[i] < 10000:
        if numbers[i] == numbers[numbers[i]]:
            result += i
print(result)