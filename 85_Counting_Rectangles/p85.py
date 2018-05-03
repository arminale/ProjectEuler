#https://projecteuler.net/problem=85 Counting Rectangles
# The number of rectangles in a m by n grid is simply (m+1 choose 2) * (n+1 choose 2) since to create a rectangle,
# one must choose two vertical and two horizontal lines out of lines that make the grid.
# We can simplify the above expression to (m^2 + m)*(n^2 + n)/4 (1)
# We want to make (1) as close to 2 000 000 as possible. Since 2 000 000 is a small bound, we can brute force it.

from math import sqrt

min_difference = 2000000
closest_val = 0

for m in range(int(sqrt(2000000))):
    for n in range(m, int(sqrt(2000000))):
        rects = (m * m + m) * (n*n + n) / 4
        if rects > 2000000:
            break
        else:
            if min_difference > abs(rects - 2000000):
                closest_val = [m,n]
                min_difference = abs(rects-2000000)
print(min_difference)
print(closest_val)