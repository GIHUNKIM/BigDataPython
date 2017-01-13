#튜플 생성
movie = '슈퍼맨||',1980,'배트맨',1989

print(movie)
print(movie[1])
print(movie[-2:])



#----------------------------------------
#튜플값 변경 시도(형 오류 발생) 튜플은 immuable 하기 때문에 값을 변경할 수 없다.
#movie[1] = 1982


#----------------------------------------
movie_list = list(movie) #튜플 -> 리스트형 변환 (객체를 convert시킨다)

print(type(movie_list)) #데이터형 확인
print(movie_list)      # 데이터    값 확인(대괄호 기호 확인)
print(tuple(movie_list)) #리스트 -> 튜플형 변환(소괄호 기호 확인)

