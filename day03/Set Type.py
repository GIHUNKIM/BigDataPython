# 세트형 생성

lang={'Java','Java','Python','C++','Python'}

print(lang) # 세트형값 확인(중복 제거 확인) 순서가 의미가 없어서 결과값도 마음대로 나온다.
print('Java' in lang) #항목 존재 유무 확인
print('Javascript' in lang)


#-----------------------------------------------------------
#세트형 집합 연산자
a = set('abracadabra')
b = set('alacazam')


print('a = ', a)
print('b = ', b)
print('차집합,a-b = ',a-b)
print('합집합,a|b = ',a|b)
print('교집합,a&b = ',a&b)
print('여집합,a^b = ',a^b) # 합집합 - 교집합
