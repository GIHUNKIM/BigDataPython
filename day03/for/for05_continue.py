#continue 문 에시

signals = 'blue','yellow', 'red'  #3가지 색에 대한 튜플 생성

for x in range(len(signals)): #range()함수를 통한 for문 수행
    print(x,signals[x],'루프 시작!') #튜플의 색인, 값, 루프 시작 메시지 출력
    if signals[x] == 'yellow':
        continue  #루프 수행 종료
    print(x, signals[x],'루프 종료!!') #튜플의 색인, 값 , 루프 종료 메시지 출력

print('프로그램 종료!!') #프로그램 종료 메시지 출력