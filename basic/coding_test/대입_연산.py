def solution(n, control):
    n = 0
    for i in range(len(control)):
        if control[i] == 'w' :
            n += 1
        elif control[i] == 's' :
            n -= 1
        elif control[i] == 'd' :
            n += 10
        elif control[i] == 'a' :
            n -= 10
        print(n)
    return n
    
print(solution(0, 'wsdawsdassw'))


# if 연산자를 간단하게

def solution(n, control):
    key = dict(zip(['w','s','d','a'], [1,-1,10,-10]))
    return n + sum([key[c] for c in control])