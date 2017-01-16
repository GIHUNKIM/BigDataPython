#변수의 유효 범위, Scope

def my_func(param):
    param = "Modified by my_func"
    print('함수 : ',param)
    print('함수 : ',id(param))

param = 'Create from outside'

my_func(param)

print('메인 :',param)
print('메인 :',id(param))