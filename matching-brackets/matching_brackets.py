def is_paired(input_string):
    
    symbols_open = ["(", "{", "["]
    symbols_close = [")", "}", "]"]
    close_to_open = {")" : "(", "}" : "{", "]" : "["}

    brackets_order = []

    for letter in input_string:

        if letter in symbols_open:
            brackets_order.append(letter)
        
        if letter in symbols_close:
            open_symbol = close_to_open[letter]

            if len(brackets_order) == 0 or (brackets_order.pop() != open_symbol):
                return False

    if len(brackets_order) != 0:
        return False
    
    return True


print(is_paired("}{"))

