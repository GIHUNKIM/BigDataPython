#리스트형 선언 및 색인
pockets = [4, 6, 1, 9] # 4개의 숫자형을 가진 리스트형 선언
print(pockets)




# 변수의 타입 확인
print(type(pockets))


print(pockets[0])  #첫번째 값 확인

print(pockets[-1])  #마지막 값 확인

#[0][1][2][3]
print(pockets[0])
print(pockets[1])
print(pockets[2])
print(pockets[3])


#indexError : list index out of range
#print(pockets[4])

# 리스트형의 길이 확인
print(len(pockets))


#리스트형 데이터 변경하기
pockets[0] = 5
print(pockets)

#리스트 항목 추가하기 : append() 함수
pockets.append(7)
print(pockets)

#리스트 항목 제거하기 : remove() 함수
pockets.remove(1) #특정 값 제거
print(pockets)

#리스트 항목 삽입하기 : insert()함수
pockets.insert(1,3) # 두번째 색인(1)에 3 삽입
print(pockets)

#리스트 항목 추출하기 : pop()함수
pockets.pop(3) #4번째 색인 값 반환후 제거
print(pockets)


#리스트형 데이터 자르기
result = pockets[1:3]  # 시작인덱스 : pockets[1] end인덱스 : pockets[2] 까지 자르기
print('pocket[1:3] = ', result)

result = pockets[:3]
print(result)

result = pockets[-2:]
print(result)