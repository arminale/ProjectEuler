# https://projecteuler.net/problem=102 Triangle Containment
# For any 3 non collinear points ABC:
# The sum of the areas of the three triangles OAB, OAC, and OBC is  equal to the area of a triangle ABC if and only if
# O is contained in ABC
# The area of a triangle can be calculated from the coordinates of its vertices using the formula here:
# https://www.mathopenref.com/coordtrianglearea.html

with open("p102_triangles.txt", 'r') as file:
    contains = 0

    for line in file:
        coordinates = line.split(',')
        coordinates[5] = coordinates[5][:-1]  # removes the newline character
        coordinates = list(map(int, coordinates))
        
        ax = coordinates[0]
        ay = coordinates[1]
        bx = coordinates[2]
        by = coordinates[3]
        cx = coordinates[4]
        cy = coordinates[5]

        s_abc = abs(ax*(by-cy) + bx*(cy-ay) + cx* (ay-by))/2
        s_obc = abs(bx*cy - cx*by)/2
        s_oab = abs(ax*by - bx*ay)/2
        s_oac = abs(ax*cy - cx*ay)/2

        if s_abc == s_oab + s_oac + s_obc:
            contains += 1

print(contains)