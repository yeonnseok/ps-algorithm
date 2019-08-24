def analysis(string):
    ans = [0] * 4
    for i in range(len(string)):
        #숫자
        if string[i].isdigit():
            ans[2] += 1
        else:
            #소문자
            if string[i].isupper():
                ans[1] += 1
            #대문자
            elif string[i].islower():
                ans[0] += 1
            #공백
            elif string[i].isspace():
                ans[3] += 1
    return ans


def main():
    string = list(input())
    print(analysis(string))


main()