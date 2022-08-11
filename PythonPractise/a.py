def MissingDigit(exp):
    exp = list(exp.split())
    first_operand = exp[0]
    operator = exp[1]
    second_operand = exp[2]
    resultant = exp[-1]
    if 'x' in resultant:
        x = resultant
        first_operand = int(first_operand)
        second_operand = int(second_operand)
 
        if operator == '+':
            res = first_operand + second_operand
        elif operator == '-':
            res = first_operand - second_operand
        elif operator == '*':
            res = first_operand * second_operand
        else:
            res = first_operand // second_operand
 
    else:
        resultant = int(resultant)
        if 'x' in first_operand:
 
            x = first_operand
            second_operand = int(second_operand)
 
            if operator == '+':
                res = resultant - second_operand
            elif operator == '-':
                res = resultant + second_operand
            elif operator == '*':
                res = resultant // second_operand
            else:
                res = resultant * second_operand
 
        # If x is in the second operand
        else:
 
            x = second_operand
            first_operand = int(first_operand)
 
            if operator == '+':
                res = resultant-first_operand
            elif operator == '-':
                res = first_operand - resultant
            elif operator == '*':
                res = resultant // first_operand
            else:
                res = first_operand // resultant
 
    res = str(res)
    k = 0
    for i in x:
        if i == 'x':
            result = res[k]
            break
        else:
            k = k + 1
    return result
s="56? * 106 = 5?678"
print(MissingDigit(s))