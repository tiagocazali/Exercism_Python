def is_paired(input_string):
    
    symbols_open = ["(", "{", "["]
    symbols_close = [")", "}", "]"]

    close_to_open = {")" : "(", "}" : "{", "]" : "["}

    #brackets_counter = {"[" : 0, "(" : 0, "{" : 0 }
    brackets_order = []

    for letter in input_string:

        if letter in symbols_open:
            #brackets_counter[letter] += 1
            brackets_order.append(letter)
        
        if letter in symbols_close:
            open_symbol = close_to_open[letter]
            #brackets_counter[open_symbol] -= 1
            if len(brackets_order) == 0 or (brackets_order.pop() != open_symbol):
                return False

            # if brackets_counter[open_symbol] < 0:
            #     print("fechou item sem abrir")
            #     return False
    
    # for quant in brackets_counter.values():
    #     if quant != 0:
    #         return False
    if len(brackets_order) != 0:
        return False
    
    return True


print(is_paired("}{"))

