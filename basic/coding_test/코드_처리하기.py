def solution(code):
    answer = ""
    mode = False
    for idx in range(len(code)):
        if code[idx] == "1" :
                mode = not mode
        else :
            if mode and idx % 2 != 0:
                answer = answer + code[idx]
            
            elif not mode and idx % 2 == 0 :
                answer = answer + code[idx] 

    if answer == "" : 
         answer = "EMPTY"

    return answer



print(solution("abc1abc1abc"))


# 매우 간단한 코딩

def solution(code):
    return "".join(code.split("1"))[::2] or "EMPTY"