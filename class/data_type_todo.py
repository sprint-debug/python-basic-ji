#1. 주민번호 "901211-1027213"의 앞 6자리만 조회해서 출력하시오.
num = "901211-1027213"
print(num[:6])

#2. "안녕하세요" 를 10번 출력하시오.
hi = "안녕하세요"
print(hi * 10)


#3. 다음 문자열의 글자수를 출력하시오.
str_value = "akdlclkdkdlelql39du7마구0ㅌ" 
print(len(str_value))

#4.
name="TV"
price=300000
maker = "LG"
# 위 변수의 값을 다음과 같은 형태로 출력하시오.
#"제품명 : TV, 가격 : 300000, 제조사 : LG"

# 방법1
# template = "제품명:{}, 가격:{}, 제조사{}"
# info = template.format(name, price, maker)

# 방법2
info = "제품명:%s, 가격: %d ,제조사:%s" %(name, price, maker)
print(info)



#5.
fruits = "사과 복숭아 귤 배"
# 위 fruits에 "수박"이 있는지 확인하는 코드를 작성하시오.
print("수박" in fruits)

#6.
str_value = "aldkjaldjfalfjlksajfladlkaalalkdjfa"
# str_value 문자열안에 a가 몇개 있는지 출력하시오.
print(str_value.count('a'))


#7. 두개의 정수를 입력받아서 곱한 결과를 출력하는 코드를 작성하세요.
a = input('a 정수:')
b = input('b 정수:')
print(int(a) * int(b))