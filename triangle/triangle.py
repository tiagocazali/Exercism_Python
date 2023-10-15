def equilateral(sides):
    a,b,c = sides
    #check if it is a Triangle
    if (a+b>=c) and (b+c>=a) and (a+c>=b) and (a != 0):
        if a == b and b == c:
            return True
    return False


def isosceles(sides):
    a,b,c = sides
    #check if it is a Triangle
    if (a+b>=c) and (b+c>=a) and (a+c>=b):
        if (a == b) or (a ==c ) or (b ==c):
            return True
    return False


def scalene(sides):
    a,b,c = sides
    #check if it is a Triangle
    if (a+b>=c) and (b+c>=a) and (a+c>=b):
        if (a != b) and (a !=c ) and (b != c):
            return True
    return False
