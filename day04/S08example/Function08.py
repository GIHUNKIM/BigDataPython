#기본값은 없으나 타입에러 나지 않게 메시지 출력
def daily_workinging_hours(hours=None):
    if hours == None:
        print('인자값 세팅을 잊으셨군요~^^')
    return hours

daily_workinging_hours()


