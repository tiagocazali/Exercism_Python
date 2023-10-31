
#- has 3 as a factor, add 'Pling' 
#- has 5 as a factor, add 'Plang' 
#- has 7 as a factor, add 'Plong'

def convert(number):
    
    answer =""
    
    if number % 3 == 0:
        answer += "Pling"
    
    if number % 5 == 0:
        answer += "Plang"
    
    if number % 7 == 0:
        answer += "Plong"
    
    if answer == "":
        answer += str(number)
    
    return answer