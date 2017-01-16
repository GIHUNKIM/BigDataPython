#전역변수 사용 global

def my_func():
    global param
    param = "Modified by my_func"
    print('함수 : ',param)
    print('함수 : ',id(param))

#del param
param = 'Create from outside' #id가 생성되면 삭제되고 다른곳에 global이 만들어짐

my_func()

print('메인 :',param)
print('메인 :',id(param))