def is_armstrong_number(number):
    num_as_string = str(number)
    
    power = len(num_as_string)
    total = 0

    for each_algarism in num_as_string:
        total += int(each_algarism)**power


    if total == int(num_as_string):
        return True
    return False