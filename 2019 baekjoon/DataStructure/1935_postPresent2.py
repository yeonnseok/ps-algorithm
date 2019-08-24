def postCalculate(equation):
    while len(equation) > 1:
        i = 0
        while i < len(equation):
            if equation[i] == "*":
                equation[i - 2:i + 1] = [equation[i-2] * equation[i-1]]
            elif equation[i] == "+":
                equation[i - 2:i + 1] = [equation[i - 2] + equation[i - 1]]
            elif equation[i] == "-":
                equation[i - 2:i + 1] = [equation[i - 2] - equation[i - 1]]
            elif equation[i] == "/":
                equation[i - 2:i + 1] = [equation[i - 2] / equation[i - 1]]
            i += 1
    return equation[0]


def replaceInput():
    numOfVar = int(input())
    equation = list(input())
    variables = {}
    i = 0
    while i < len(equation) and numOfVar > 0:
        if equation[i] != "*" and equation[i] != "+" and equation[i] != "-" and equation[i] != "/":
            variables[equation[i]] = int(input())
            numOfVar -= 1
        i += 1
    for i in range(len(equation)):
        if equation[i] != "*" and equation[i] != "+" and equation[i] != "-" and equation[i] != "/":
            equation[i] = variables[equation[i]]
    return equation


def main():
    equation_list = replaceInput() #list형태
    print("%.2f" %postCalculate(equation_list))


main()



