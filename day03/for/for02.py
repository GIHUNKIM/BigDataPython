# for문과 range()함수 예시

signals = 'blue','yellow','red'  #3가지 색에 대한 튜플 생성

for x in range(len(signals)):           # range()함수를 통한 for문 수행 -> x값에 0,1,2 index값이 들어간다.
    print(x, signals[x],len(signals[x])) #튜플의 색인, 값, 길이 출력



#---------------------------------------------------
#print('-' * 50) -를 50개 출력하라
#\t: 탭키만큼 띄워주기 , \n : 한줄 띄기

for x in range(1,10):   #1부터 9까지  range(1,10,2) : 1부터 9까지 2씩 건너 띄어서
    print(x)

    