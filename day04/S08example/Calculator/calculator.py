# def calculator(ope, num1, num2):
#     print(ope,'연산을 선택하였습니다.')
#     if ope == '+':
#         print(num1,ope,num2 ,'=',(num1+num2))
#     elif ope == '-':
#         print(num1, ope, num2, '=', (num1 - num2))
#     elif ope == '*':
#         print(num1, ope, num2, '=', (num1 * num2))
#     elif ope == '/':
#         print(num1, ope, num2, '=', (num1 / num2))
#     else:
#         print('ope가 올바르지 않습니다.')
#     print('\n')

#-----------------------------------------------------
#return 값을 이용하여 함수 선언
def calculator(ope, num1, num2):
    print(ope,'연산을 선택하였습니다.')
    if ope == '+':
        return num1 + num2
    elif ope == '-':
        return num1 - num2
    elif ope == '*':
        return num1 * num2
    elif ope == '/':
        return num1 / num2
    else:
        print('ope가 올바르지 않습니다.')
    print('\n')

print(calculator('+',1,2))
print(calculator('-',1,2))
print(calculator('*',1,2))
print(calculator('/',1,2))