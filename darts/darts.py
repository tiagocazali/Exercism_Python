from math import sqrt


def score(x, y):
    
    #Calculating the distance beteween the center (0,0) and the giving point (x,y)
    #Since the center is ZERO, ZERO it is easier to calculate:

    distance = sqrt(x**2 + y**2)
    
    if distance <= 1:
        return 10
    if distance <=5:
        return 5
    if distance <=10:
        return 1
    else:
        return 0
