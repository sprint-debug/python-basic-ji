def solution(a, b, c, d):
    # 리스트 오름차순으로 정렬
    li =  sorted([str(a),str(b),str(c),str(d)])
    li2 = [str(li[0])]
    count = 0

    for i in range(1, len(li)):
        if li[i] in li2[count] : #li2에 포함되면,
            li2[count] += li[i]
        else :
            li2.append(li[i])
            count += 1
        
    li2 = sorted(li2, key=lambda x:len(x), reverse=True)

    for i in range(len(li2)):
        if len(li2[i]) == 3 :
            li2[i] = int(li2[i][0])
            
            li2[2:5] = [li2[i],li2[i],li2[i]]
        else: 
            li2[i] = int(li2[i][0])

    if len(li2) == 1 :
        return 1111 * li2[0]
    elif len(li2) == 2 : 
        return (li2[0] + li2[1]) * abs(li2[0] - li2[1])
    elif len(li2) == 3 :
        return li2[1] * li2[2]
    elif len(li2) == 4 :
        return min(li2)
    else :
        return (10 * li2[0] + li2[1]) ** 2


print(solution(	4, 1, 4, 4))



# 다른 풀이
# count 가 핵심인 것 같음

def solution(a, b, c, d):
    l = [a,b,c,d]
    c = [l.count(x) for x in l]
    if max(c) == 4:
        return 1111*a
    elif max(c) == 3:
        return (10*l[c.index(3)]+l[c.index(1)])**2
    elif max(c) == 2:
        if min(c) == 1:
            return eval('*'.join([str(l[i]) for i, x in enumerate(c) if x == 1]))
        else:
            return (max(l) + min(l)) * abs(max(l) - min(l))
    else:
        return min(l)