def solution(ineq, eq, n, m):
    dab = None
    if ineq == "<" :
        if eq == "=" :
            dab = n <= m 
        else :
            dab = n < m
    else :
        if eq == "=" :
            dab = n >= m 
        else :
            dab = n > m
    answer = 1 if dab else 0 
    return answer

print(solution("<","=",20,50))


# 쉬운 예제
# eval 문자열의 식 값을 반환함.
def solution(ineq, eq, n, m):
    return int(eval(str(n)+ineq+eq.replace('!', '')+str(m)))