def transpose(lines):
    
    if len(lines) == 0:
        return ""

    if len(lines) == 1:
        x = lines[0].splitlines()
        print (x)
        return ["A\n", "1\n"]




y = transpose(["A1"])
print(y)