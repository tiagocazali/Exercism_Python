def response(hey_bob):
    hey_bob = str(hey_bob).rstrip()

    if not hey_bob:
        return "Fine. Be that way!"
    
    if hey_bob.endswith("?") and hey_bob.isupper():
        return "Calm down, I know what I'm doing!"
    
    if hey_bob.endswith("?"):
        return "Sure."
    
    if hey_bob.isupper() and not hey_bob.endswith("?"):
        return "Whoa, chill out!"
    
    return "Whatever."

    


    
