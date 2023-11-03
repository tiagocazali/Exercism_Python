import string

def is_pangram(sentence):
    
    # All lowercase Letters in the alphabet
    alfabeto = string.ascii_lowercase  

    # Create a dictinary with Key "letter" and value 1
    all_letters = {letra: 1 for letra in alfabeto}
    
    for each_letter in sentence:
        if each_letter.lower() not in alfabeto:
            continue
        all_letters[each_letter.lower()] -= 1
    
    print(all_letters)
    control = True
    for each in all_letters.values():
        if each > 0:
            control = False

    return control

print(is_pangram('Five quacking Zephyrs jolt my wax bed.'))



