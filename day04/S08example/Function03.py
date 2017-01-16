#인자값, 반환값 모두 있는 함수
def sum(a,b):   #a,b 는 sum안에서만 존재하는 변수!
    return(a+b)

param1 = 4
param2 = 5
result = sum(param1,param2)

print('sum(%d, %d) = %d' %(param1,param2,result))