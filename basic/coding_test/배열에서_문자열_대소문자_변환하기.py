# def solution(strArr):
#     # strArr[2::2] = strArr[2::2].lower()

#     return answer


strArr = ["AAA","BBB","CCC","DDD"]
list1 = []
for i in range(len(strArr)):
    if i % 2 == 0 :
        ls = strArr[i].upper()
    else :
        ls = strArr[i].lower()
    list1.append(ls)
          
print(list1)
    