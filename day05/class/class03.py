#클래스 변수와 인스턴스 변수
#변수의 선언위치 따라 달라지는 유효 범위
class BookReader:
    country = 'South Korea' #클래수 변수 country선언

    def __init__(self,name):
        self.name = name #인스턴스 변수 name선언


    def read_book(self):
        print(self.name + 'is reading Book!!')

#객체 인스턴스화
reader1 = BookReader('Cheyoung')
reader2 = BookReader('Heeyoung')
reader3 = BookReader('Chanyoung')


reader1.country = 'America'
reader2.country = 'China'

#클래스 변수 country 확인
print('reader1.country : ',reader1.country)
print('reader2.country : ',reader2.country)
print('reader3.country : ',reader3.country,'\n')

#클래스함수 호출(인스턴수 변수 name 출력)
reader1.read_book()
reader2.read_book()
reader3.read_book()

