print("안녕하세요!\n반갑습니다.")


print("""
빅데이터과정에서
만나서 반값습니다.
끝까지 화이팅 하세요!!!
""")


test = '파이썬 프로그래밍 재미있다!' # 문자열을 변수에 저장

result = test.startswith('파이썬') #문자열이 파이썬으로 시작하는지 확인
print(result)
#startswith는 시작하는 문자열이 같으면 전부다 True이다 파이, 파로 해도 결과는 같다
result = test.endswith('!') #문자열이 '!'로 끝나는지 확인
print(result)
result = test.endswith('어려워요!') # 문자열이 '어려워요!'로 끝나는지 호가인
print(result)
result = test.replace('파이썬', 'Python') #문자열중 '파이썬'을 'Python'으로 변경
print(result)


test = 'Python Programming is Interesting!'

result = test.upper()  # 문자열을 모두 대문자로 변경
print(result)
result = test.lower() # 문자열을 모두 소문자로 변경
print(result)
result = '/'.join(test) # 문자열의 각 문자 사이에 '/'문자 집어 넣기
print(result)




