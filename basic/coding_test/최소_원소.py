def solution(arr, queries):
    answer = []
    li = []
    for a, b, c in queries:
        for i in arr[a:b+1]:
            if i > c:
                li.append(i)
        
        if li :
            li.sort()
            answer.append(li[0])
            li.clear()
        else :
            answer.append(-1)
            li.clear()       

    return answer 
   
print(solution([0, 1, 2, 4, 3],[[0, 4, 2],[0, 3, 2],[0, 2, 2]]))

# min
def solution(arr, queries):
    answer = []
    for s, e, k in queries:
        l = [i for i in arr[s:e+1] if i > k]
        answer.append(-1 if len(l) == 0 else min(l))
    return answer