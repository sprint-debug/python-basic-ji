sum:str = 'aBcD'
l1 = list(sum)

l2 = []
for su in l1:
    if su.islower() :
        c_su = su.upper()
        l2.append(c_su)
    else:
        c_su2 = su.lower()
        l2.append(c_su2)

# 리스트 공백없이 합치기
sum2 = ''.join(l2)
print(sum2)

# -----------------------------------------
# 뭐한거지... 그냥 이거 쓰면 됨...ㅋㅋㅋㅋㅋ
# swapcase() 소문자는 대문자로, 대문자는 소문자로 상호전환....
print(sum.swapcase())