def rotate(text, key):
    # ASCII 
    # A-65 - a-97
    # Z-90 - z-122

    encripted_msg = []

    for each_letter in text:
        #For CAPITAL letters
        if ord(each_letter) >= 65 and ord(each_letter) <= 90:
            new_letter = ord(each_letter)+key
            if new_letter > 90:
                new_letter -= 26
            encripted_msg.append(chr(new_letter))
        
        #For Lowercase letters:
        elif ord(each_letter) >= 97 and ord(each_letter) <= 122:
            new_letter = ord(each_letter)+key
            if new_letter > 122:
                new_letter -= 26
            encripted_msg.append(chr(new_letter))
        
        #For others characteres, like space and ponctuation:
        else:
            encripted_msg.append(each_letter)
    
    return "".join(encripted_msg)


