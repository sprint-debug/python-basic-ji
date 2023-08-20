def solution(arr, queries):
    
    for s,e,k in queries:
        print(s,e,k)
        for i in range(s, e+1):
            if i % k == 0:
                arr[i]+=1
  
    return arr

print(solution([0, 1, 2, 4, 3],	[[0, 4, 1],[0, 3, 2],[0, 3, 3]]))
