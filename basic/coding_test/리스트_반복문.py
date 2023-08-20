def solution(arr, queries):
    for li in queries:
        i = li[0]
        j = li[1]
        
        arr[i], arr[j] = arr[j], arr[i]    
    return arr
   
print(solution([0, 1, 2, 3, 4], [[0, 3],[1, 2],[1, 4]]	))

# 더 쉽게
def solution(arr, queries):
    for a,b in queries:
        arr[a],arr[b]=arr[b],arr[a]
    return arr