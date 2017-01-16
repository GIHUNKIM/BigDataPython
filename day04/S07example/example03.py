books = list()  #책 목록 선언  데이터를 읽어와서 담아놓기 위해서

#책 목록 만들기
books.append({'제목':'파이썬프로그램','출판연도':'2016','출판사':'A','쪽수':200,'추천유무':False})
books.append({'제목':'플렛폼 비즈니스','출판연도':'2013','출판사':'B','쪽수':584,'추천유무':True})
books.append({'제목':'빅데이터 마케팅','출판연도':'2013','출판사':'A','쪽수':296,'추천유무':True})
books.append({'제목':'외식경영 전문가','출판연도':'2010','출판사':'B','쪽수':526,'추천유무':False})
books.append({'제목':'십억만 벌어보자','출판연도':'2013','출판사':'A','쪽수':248,'추천유무':True})

many_page = list()
    #다른표기방법
    #many_page = [ book['제목'] for book in books if book['쪽수'] > 250 ] 250이상인것만 제목을 many_page에 담는다.
recommends = list()
    #다른표기방법
    #recommends = [ book['제목'] for book in books if book['추천유무'] ]
all_page = int()
pub_companies = set()   #출판사 집합 선언
    #다른 표기방법
    #pub_companies = { book['출판사'] for book in books }

for book in books:
    if book['쪽수']>=250:
        many_page.append(book['제목'])

    if book['추천유무']:
        recommends.append(book['제목'])
    all_page += book['쪽수']
    pub_companies.add(book['출판사'])

print('쪽수가 250쪽 넘는 책 리스트 : ', many_page)
print('내가 추천하는 책 리스트 : ', recommends)
print('내가 읽은 책 전체 쪽수 : ', all_page)
print('내가 읽은 책의 출판사 목록 : ', pub_companies)


