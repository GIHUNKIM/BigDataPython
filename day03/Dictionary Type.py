balls = {'red':4, 'blue':3, 'green':5}

print(balls) #사전형값 확인
print(type(balls)) #데이터형 확인
print(len(balls)) #사전형 길이 확인

#-----------------------------------------------
#검은공 항목 추가
balls['black']=1
print(balls)

#-----------------------------------------------
#녹색공 항목 제거
del balls['green']
print(balls)


#-----------------------------------------------

#값 변경
balls['black'] = 3;
print(balls)

#-----------------------------------------------
#사전키 차출후 리스트형
print(list(balls.keys())) #사전키 추출후 리스트형으로 전환
print(sorted(balls.keys())) #사전키 추출후 오름차순 정렬
#print(sorted(balls.keys(),reverse=True)) #내림차순 정렬
#print(sorted(balls.keys(),reverse=False)) #오름차순 정렬

print(list(balls.values())) #사전값 추출후 리스트형으로 전환


#-----------------------------------------------
print('blue' in balls) #키 존재 유무 확인
print('white' not in balls) #키누락 유무 확인


#-----------------------------------------------
#------------dict표현방법 3가지----------------
#표현1
balls1 = {'red':0, 'blue':1,'green':2}
print('표현방법1 :',balls1)

#리스트안의 항목이 키와 값의 쌍으로 이루어진 튜플인 경우
balls2 = dict([('brown',3),('gray',7)])
print(balls2)


#키가 단순한 문자열의 경우, dict 함수의 인자값 형태로 진행
balls3 = dict(brown=4,gray=8)
print(balls3)