def solution(log):
    answer = ''
    for i in range(1, len(log)):
        if abs(log[i] - log[i-1]) == 1 :
            if log[i] > log[i-1] :
                answer += "w"
            else:
                answer += "s"
        else :
            if log[i] > log[i-1] :
                answer += "d"
            else:
                answer += "a"
        print(answer)
            
    return answer
 
# wsdawsdassw   
print(solution([0, 1, 0, 10, 0, 1, 0, 10, 0, -1, -2, -1]))

#abs() 절대값.. 