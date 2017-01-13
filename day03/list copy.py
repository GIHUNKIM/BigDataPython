pockets = [4, 6, 1, 9]

#--------------call by reference---------------
#리스트형 복사하기
pockets_copy = pockets  #신규 변수 생성 및 기존리스트 대입
#call by reference 방식으로 리스트의 주소값을 복사해준다
pockets_copy.append(1) #신규변수에 1추가
print(pockets_copy)
print(pockets)
print(id(pockets_copy))
print(id(pockets))   # 동일한 id값을 가진다



#--------------call by value----------------
pockets_real_copy = pockets[:]  #신규변수생성 및 pockets 복사
#처음부터 끝까지 모든 데이터 값을 복사 : call by value
pockets_real_copy.append(9) #신규변수에 9추가

print(pockets)
print(pockets_real_copy)
print(id(pockets))
print(id(pockets_real_copy))