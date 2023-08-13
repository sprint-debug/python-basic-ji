def solution(n):
    answer = 0
    if n % 2 != 0 :
        for i in range(n+1) :
            if i % 2 != 0 : 
                answer = i + answer
    else :
        for i in range(n+1) :
            if i % 2 == 0 : 
                answer = i*i + answer
    return answer


print(solution(10))

# 쉽게...
def solution(n):
    if n%2:
        return sum(range(1,n+1,2))
    return sum([i*i for i in range(2,n+1,2)])
