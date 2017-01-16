#반환값을 표기하지 않는 함수의 반환 값, None
def no_return():
    print('안녕하세요')
    return      #반환값 없음, 생략 가능


print(no_return())  #함수 반환값 출력
print(type(None))   #<class 'NoneType'> : 아무것도 없다는 파이썬의 객체