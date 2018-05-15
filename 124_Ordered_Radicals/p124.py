# https://projecteuler.net/problem=124 Ordered Radicals
# Idea:
# 1. Generate radicals of numbers upto 100000
# 2. Store them in an array in the form [rad(n), n]
# 3. Sort the array on rad(n) and return the 10000 element
# Note: [1,0] is included in the array. Thus E(10000) is indeed array[10000] and not array[10001]
upper_bound = 100000

radicals = [[1,n] for n in range(upper_bound + 1)]

for i in range(2,upper_bound+1):
    if radicals[i][0] == 1:
        for j in range(i, upper_bound+1,i):
            radicals[j][0] *= i

radicals.sort(key= lambda x: x[0])
print(radicals[10000])