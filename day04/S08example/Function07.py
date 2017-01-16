#함수의 매개변수 표기할때 기본값 설정
def daily_sleeping_hours(hours=7):   # 함수 사용시 인자값이 안들어오면 기본값으로 7을 사용하겠다.
    return hours


print(daily_sleeping_hours())