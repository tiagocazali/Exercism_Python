def is_isogram(word):
    
    used_letters = {}

    for each_letter in word:

        if not each_letter.isalpha():
            continue

        elif each_letter.lower() in used_letters:
            used_letters[each_letter.lower()] += 1

        else:
            used_letters[each_letter.lower()] = 1
    

    for each_letter in used_letters.values():
      if each_letter > 1:
          return False
    
    return True