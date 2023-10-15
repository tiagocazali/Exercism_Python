class Luhn:
    
    def __init__(self, card_num):
        self.string_num = str(card_num).replace(" ","")

    def valid(self):
                
        if self.string_num.isdigit():
            self.num = [int(x) for x in self.string_num]
        else:
            return False
        
        double_list = []
        if len(self.num) == 1:
            return False

        for index, value in enumerate(self.num[::-1]):
            if index %2 != 0:
                temp = value*2
                if temp >= 10:
                    temp -= 9
                double_list.insert(0,temp)
            else:
                double_list.insert(0, value)

        if sum(double_list) % 10 == 0:
            return True
        return False