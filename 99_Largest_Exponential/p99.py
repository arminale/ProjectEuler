# https://projecteuler.net/problem=99 Largest Exponential
# Instead of comparing numbers in the form of a^b, I'll take the log of all numbers and compare b*log(a)

from math import log

with open("p099_base_exp.txt", 'r') as input_file:
    maximum = 0
    max_line = 0
    line_counter = 0
    for line in input_file:
        line_counter += 1
        [base, exp] = map(int,line.split(','))
        temp = exp*log(base)
        if temp > maximum:
            maximum = temp
            max_line = line_counter

print(max_line)
