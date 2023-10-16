from itertools import count


def steps(number):
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    
    count_loops = 0
    
    while number != 1:
        if number%2 == 0:
            number = number /2
        else:
            number = (number*3) + 1
        
        count_loops +=1
    
    return count_loops


