def egg_count(display_value):
    
    if display_value == 0:
        return 0
    
    x = display_value
    num_binary = []

    while(x >= 2):

        integer_part, rest = divmod(x,2)
        num_binary.append(rest)
        x = integer_part
        
    num_binary.append(1)
    
    return sum(num_binary)