def solution(num_list):
    answer = 0
    gob = 1 
    hab = 0
    
    for num in num_list:
        # gob = gob * num
        # hab = hab + num 
        num*=gob
        num+=hab
        
        if gob < hab**2 :
            answer = 1
        else :
            answer = 0
    return answer

print(solution([5, 7, 8, 3]))