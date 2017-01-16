#여러 개의 인자 값 및 키워드 인자 활용하기
def introduce_my_car(manufacturer, seats =4, type = 'sedan'):
    print('내 차는',manufacturer,'의',seats,'인승',type,'이다')


#위치 인자 값 1개
introduce_my_car('현대')

#키워드 인자 값 1개
introduce_my_car(manufacturer='GM대우')

#키워드 인자 값 2개
introduce_my_car(manufacturer='GM대우',type='SUV')

#순서 바뀐 키워드 인자 값2개, 순서가 바뀐 경우는 반드시 키워드 인자값 사용!
introduce_my_car(type='SUV',manufacturer='GM대우')

#순서를 지킨 위치 인자 ㄱ밧 3개, 순서가 같다면 모두 위치 인자 값 사용 가능
introduce_my_car('아우디',2,'스포츠카')

#위치 인자 값1개, 키워드 인자 값 1개, 혼용으로 사용 가능
introduce_my_car('아우디',seats=2)