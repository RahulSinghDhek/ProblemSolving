def areBracketsBalanced(input_brackets):
    temp=[]
    flag= True
    for bracket in input_brackets:
        if bracket == "[":
            temp.append("]")
        elif bracket== "{":
            temp.append("}")
        elif bracket == "(":
            temp.append(")")
        else:
            if temp ==[] or temp[-1] != bracket:
                flag = False
                break
            temp.pop()
    if not flag:
        return "No"
    elif temp ==[]:
        return "Yes"
    else:
        return "No"
