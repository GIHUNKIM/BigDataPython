#리스트형 데이터 합치기 & 확장하기
a= [1,2,3]
b= [4,5,6]
c= a+b

#리스트 값 확인
print('a= ',a)
print('b= ',b)
print('c= ',c)

#객체식별자 확인
print('id(a) = ',id(a))
print('id(b) = ',id(b))
print('id(c) = ',id(c)) #합칠경우 새로운 메모리 공간에 할당되어 생성된다.


#데이터 확장
a.extend(b)   #a와 동일한 메모리 공간에 그대로 리스트만 확장되는 것이다.
print('a = ',a)
print('id(a) = ',id(a))