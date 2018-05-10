# https://projecteuler.net/problem=66
# see https://en.wikipedia.org/wiki/Pell%27s_equation
# and https://en.wikipedia.org/wiki/Continued_fraction#Infinite_continued_fractions_and_convergents
from math import sqrt

maxX = 0
for D in range(2, 1001):

    m = 0
    d = 1
    a_0 = int(sqrt(D))
    a = a_0
    if a_0 ** 2 == D:
        continue

    num1 = 1
    num = a_0

    den1 = 0
    den = 1

    while num ** 2 - D*den*den != 1:

        m = d*a - m
        d = (D - m ** 2)/d
        a = int((a_0 + m)/d)

        num2 = num1
        num1 = num
        den2 = den1
        den1 = den

        num = a*num1 + num2
        den = a*den1 + den2

    if num > maxX:
        maxX = num
        maxD = D
print(maxD)
