# 클래스내부변형변수는메소드를통해접근
class BookReader:
    __country = 'Korea'

    def update_country(self, country):
        self.__country = country

    def get_country(self):
        return self.__country

country = str()

br = BookReader()
country = br.get_country()
print('초기값:', country)

br.update_country('America')
country = br.get_country()
print('변경값:', country)