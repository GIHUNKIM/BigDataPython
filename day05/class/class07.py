#클래스 내부변수
class BookReader:
    __country = 'Korea'

#print(dir(BookReader))
#print('\n*'.join(dir(BookReader)))  #처음에 해당되는 변수값은 join이 되지 않는다

br_list = dir(BookReader)
for num in range(len(br_list)):
    print(num+1, ':', br_list[num])

 #클래스내부변수는정의시사용했던변수명으로는접근이불가능
#BookReader.__country


