# https://projecteuler.net/problem=64 Odd Period Square Roots
# see https://en.wikipedia.org/wiki/Methods_of_computing_square_roots

from math import sqrt

odd_periods = 0

for s in range(10001):
    m = 0
    d = 1
    a_0 = int(sqrt(s))
    a = a_0
    period = 0
    if a_0 ** 2 == s:
        continue
    while a != 2*a_0:
        period += 1
        m = d*a-m
        d = (s - m ** 2)/d
        a = int((a_0 + m)/d)

    if period % 2 == 1:
        odd_periods += 1

print(odd_periods)