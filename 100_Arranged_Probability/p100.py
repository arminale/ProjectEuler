# https://projecteuler.net/problem=100 Arranged Probability
# Let b be the number of blue disks and t be the total number of disks. The probablity of taking out two blue disks is:
# (b/t) * ((b-1)/(t-1)
# By setting the above equal to 1/2 and simplifying, we get: 2b^2 - 2b - t^2 + t = 0
# We need to treat above as a Diophantine equation. Using https://www.alpertron.com.ar/QUAD.HTM we get the following
# solution for the equation:
# b_0 = 1, t_0 = 1
# b_n+1 = 3b_n + 2t_n - 2
# t_n+1 = 4b_n + 3t_n - 3

blue = 1
total = 1

while total <= 1000000000000:
    blue, total = 3*blue + 2*total - 2, 4*blue + 3*total - 3

print(blue)
