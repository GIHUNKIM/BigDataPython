#강사님 답안
dan = input('구구단 몇단을 출력 할까요? 숫자를 입력하세요->')
print(dan,'단 출력')
print('='*30)
for num in range(9):
    num +=1
    gop = int(dan) * num
    print(dan,'x', num,'=', gop)