def is_valid(isbn):
    
    formated_isbn = validate(isbn)
    if formated_isbn == -1:
        return False
    
    
    check_digit = formated_isbn.pop()
    if check_digit == -1:
        check_digit = 10
    
    temp = 0
    aux = 10
    for each in formated_isbn:
        temp += (each*aux)
        aux -= 1

    if 11-(temp % 11) == check_digit:
        return True
    else:
        return False
      


def validate(isbn):

    temp = isbn.replace("-","").replace(" ", "")
    
    formated_isbn = []

    for x in temp:
        if (x == "x" or x == "X") and len(formated_isbn) == 9:
            formated_isbn.append(-1)

        elif x.isalpha():
            return -1

        else:
            formated_isbn.append(int(x))
    
    if len(formated_isbn) != 10:
        return -1
    return formated_isbn
    


x = is_valid("3-598-21508-A")
print(x)

