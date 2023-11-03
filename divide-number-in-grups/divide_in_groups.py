def divide_number(number, parts):

    list_parts = []

    integer_part, rest = divmod(number,parts)
    
    for x in range(parts):
        list_parts.append(integer_part)
    
    if rest != 0:
        for y in range(rest):
            list_parts[y] += 1
    
    return list_parts


def divide_number2(number, parts):

    integer_part, rest = divmod(number,parts)

    first_part = (parts - rest) *[integer_part]

    second_part = [integer_part + 1]*rest

    answer = first_part + second_part

    return answer

    
