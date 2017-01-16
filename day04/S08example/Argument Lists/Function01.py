#가변 인자 리스트 활용하기
def introduce_your_family(name, *family_names, **family_info):
    print('제 이름은',name,'입니다.')
    print('제 가족들의 이름은 아래와 같아요.')
    for name in family_names:
        print(name)
        print("="*40)
    for key in family_info.keys():
        print(key, ":", family_info[key])


introduce_your_family('진수','희영','찬영','준영','채영',집='코아루',가훈='행복하게 살자!')