# def solution(num_list):
#     num = 0
#     for su in num_list:
#         if su >= 0 :
#             num += 1
#         else :
#             return num 
        
#     num = -1 if len(num_list)-1 < num else num

#     return num

# 또는 아래와 같이..
def solution(num_list):
    for i in range(len(num_list)):
        if num_list[i]<0:return i
    return -1

print(solution([12, 4, 15, 46, 38, -2, 15]))
print(solution([13, 22, 53, 24, 15, 6]))




