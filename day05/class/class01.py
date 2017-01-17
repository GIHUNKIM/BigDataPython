#클래스 정의
class BookReader:   #클래스 BookReader 선언
    name = str()    #문자열형 변수 name 선언

    def read_book(self):
        print(self.name + ' is reading Book!!')


#클래스 호출
reader = BookReader()   #인스턴스 생성
reader.name = 'Daniel'  #속성값 변경
reader.read_book()  #메소드 호출

reader2 = BookReader() 
reader2.name = 'Alice'
reader2.read_book()