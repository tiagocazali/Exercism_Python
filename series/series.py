def slices(series, length):
    
    #check for error:
    if length == 0:
        raise ValueError("slice length cannot be zero")
    
    elif length < 0:
        raise ValueError("slice length cannot be negative")
    
    elif len(series) == 0:
        raise ValueError("series cannot be empty")
    
    elif len(series) < length:
        raise ValueError("slice length cannot be greater than series length")
    
    answer =[]
    for index, value in enumerate(series):
        if index + length <= len(series):
            temp = series[index:index+length]
            answer.append(temp)
    
    return answer

print(slices("1234",2))