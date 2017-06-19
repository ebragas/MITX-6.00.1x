
# Polysum

# Write a function that accepts 2 arguments, n (number of sides on a polygon)
# and s (length of each side) and returns the sum of the polygon's area ad
# perimeter squared.

# A regular polygon is one that is equiangular and equilateral

# https://courses.edx.org/courses/course-v1:MITx+6.00.1x+2T2017/courseware/0de4fecc5a9a4749923133fcf4de181f/344d02eadf134621a1f17f473ef14514/

from math import *

# Main used to drive program
def main():
    x, y = 3, 5
    print("Perimeter: {}".format(perimeter(x, y)))
    print("Perimeter squared: {}".format(perimeter(x, y)**2))
    print("Area: {}".format(area(x, y)))
    print("Polysum: {}".format(polysum(x, y)))

def area(n, s):
    """
    Input: int n, number of sides of a regular polygon; int s, length of each side
    Returns the area of the polygon.
    """
    area = (0.25 * n * s**2) / tan(pi / n)
    return area

def perimeter(n, s):
    """
    Input: int n, number of sides of a regular polygon; int s, length of each side
    Returns the perimeter of the polygon
    """
    perim = n * s
    return perim

def polysum(n, s):
    """
    Input: int n, number of sides of a regular polygon; int s, length of each sides
    Returns the sum of the area and perimeter squared of a regular polygon,
    rounded to four decimals.
    """
    return round(area(n, s) + perimeter(n, s)**2, 4)

if __name__ == '__main__':
    main()
