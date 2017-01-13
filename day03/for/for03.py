#중첩 for문

#3X2 2차원 배열을 중첩리스트로 선언
next  = [[1,2,3],[4,5,6],[7,8,9]]

for x in range(3):  #행을 위한 바깥쪽 for문
    for y in range(3): #열을 위한 안쪽for문
        print('next[',x,'][',y,']:',next[x][y]) #항목 출력
        #print('next[%d][%d] : %d' %(x,y,next[x][y]))  같은 출력이다.


#Refactor : 변수에 마우스 오른쪽 클릭 -> Refactor -> Rename 을 통해 모든 변수의 이름을 한번에 바꿀수 있다.(단축키 : shift + F6)

