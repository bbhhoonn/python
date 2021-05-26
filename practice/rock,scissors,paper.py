from random  import choice

가위바위보=['가위','바위','보']
User_choice=None
while User_choice not in 가위바위보:
    User_choice=input('가위 바위 보 중 입력하세요! ')

Computer_choice=choice(가위바위보)
if User_choice==Computer_choice:
    print('User : {}, Computer : {}'.format(User_choice,Computer_choice))
    print(User_choice,'로 비겼습니다.')
else:
    if User_choice=='가위':
        if Computer_choice=='바위':
            print('User : {}, Computer : {}'.format(User_choice,Computer_choice))
            print('졌습니다..')
        else:
            print('User : {}, Computer : {}'.format(User_choice,Computer_choice))
            print('이겼습니다!')
    elif User_choice=='바위':
        if Computer_choice=='보':
            print('User : {}, Computer : {}'.format(User_choice,Computer_choice))
            print('졌습니다..')
        else:
            print('User : {}, Computer : {}'.format(User_choice,Computer_choice))
            print('이겼습니다!')
    else:
        if Computer_choice=='가위':
            print('User : {}, Computer : {}'.format(User_choice,Computer_choice))
            print('졌습니다..')
        else:
            print('User : {}, Computer : {}'.format(User_choice,Computer_choice))
            print('이겼습니다!')

