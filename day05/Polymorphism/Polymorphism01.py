#다형성
#developer 부모 클래스 선언
class Developer:
    def __init__(self, name):
        self.name = name

    def coding(self):
        print(self.name + 'is developer!!')


#PythonDeveloper 자식 클래스 선언
class PythonDeveloper(Developer):
    def coding(self):
        print(self.name + 'is Python developer!!')

#JavaDeveloper 자식 클래스 선언
class JavaDeveloper(Developer):
    def coding(self):
        print(self.name + 'is Java Developer!!')

#CPPDeveloper 자식 클래스 선언
class CPPDeveloper(Developer):
    def coding(self):
        print(self.name + 'is C++ Developer!!')

pd = PythonDeveloper('찬영이')
jd = JavaDeveloper('준영이')
cd = CPPDeveloper('채영이')

pd.coding()
jd.coding()
cd.coding()
