#언패킹 인자 리스트 활용하기

#일반적으로 값을 2개 따로 대입
print(list(range(3,6)))


#---------------------------------
#리스트형 데이터를 언패킹 하여 대입
args= [ 3, 6]
print(list(range(*args)))   #args로 하면 리스트라 오류가 나지만 * 이라는 개념은 3,6이 들어간다고 생각하면된다.