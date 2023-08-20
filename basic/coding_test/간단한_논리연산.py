def solution(x1, x2, x3, x4):
    answer = False
    s1 = True
    s2 = True
    # 1식은 True가 하나라도 포함되지 않으면 false
    # 2식은 False가 하나라도 포함되지 않으면 True

    if True not in (x1, x2):
        s1 = False
    if True not in (x3, x4):
        s2 = False
    if False not in (s1, s2):
        answer = True

    return answer

# lambda 식을 이용한 ..
solution=lambda w,x,y,z:(w or x)and(y or z)