def postPresent(equation):
    equation = list(equation)
    stack = []
    i = 0
    while i < len(equation):
        if equation[i] == "*" or equation[i] == "+" or equation[i] == "-" or equation[i] == "/":
            stack.append(equation.pop(i))

        if equation[i] == "(":
            del equation[i]
        elif equation[i] == ")":
            equation.insert(i+1, stack.pop())
            del equation[i]
        i += 1

    for i in range(len(stack)):
        equation.append(stack.pop())
    return "".join(equation)


def main():
    equation = input()
    print(postPresent((equation)))


main()



