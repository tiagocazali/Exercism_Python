def translate(text):
    
    words = text.split()
    
    vowels = ["a","e","i","o","u"]
    new_word = []

    for word in words:
        consonant_added = False
        temp = []

        for i, letter in enumerate(word):
            
            if letter in vowels:
                if consonant_added:
                    new_word.append(word[i:] + "".join(temp) + "ay")
                    break
                
                new_word.append(word + "ay")
                break
            
            elif word[:2] in ("xr", "yt"):
                if consonant_added:
                    new_word.append(word[2:] + "".join(temp) + "ay")

                new_word.append(word + "ay")
                break

            else:
                if (letter == "q") and (word[i+1] == "u"):
                    new_word.append(word[i+2:] + "".join(temp) + "quay")
                    break

                if (letter == "y") and consonant_added:
                    new_word.append(word[i:] + "".join(temp) + "ay")
                    break

                if (letter == "y"):
                    new_word.append(word[i+1:] + "".join(temp) + "yay")
                    break
                    
                else:
                    temp.append(letter) 
                    consonant_added = True

                    if i == len(word):
                        new_word.append(temp)
                        break
    
    return " ".join(new_word)


print(translate("quick fast rhythm my yellow"))



