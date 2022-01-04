def commaCode(spam):
    string=''
    for i in range(len(spam)):
        if i == 0:
            string = spam[i]
        elif i < len(spam)-1:
            string = string + ', ' + spam[i]
        else:
            string = string + ' and ' + spam[-1]
    return string

spam = list(map(str, input().split()))
print(commaCode(spam))
