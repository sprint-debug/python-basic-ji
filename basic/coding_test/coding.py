def solution(arr, q):
    answer = []
    li = []
    # for i in range(len(q)) : 
    #     li = arr[q[i][0]: q[i][1]+1]
    #     for j in range(len(li)) :
    #         if li[j] % q[i][2] == 0 : 
    #             li[j] = li[j] + 1
    for a, b, c in q:
        li = arr[a:b+1]
        for i in range(len(li)):
            if li[i] % c == 0 :
                li[i] += 1
            answer
            print('li:', li)
        
        # answer[q[i][0]: q[i][1]+1] = li      
        
    return answer

print(solution([0, 1, 2, 4, 3],	[[0, 4, 1],[0, 3, 2],[0, 3, 3]]))
