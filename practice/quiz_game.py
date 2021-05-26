def new_game():
    guesses=[]
    correct=0
    option_num=0
    for key in questions:
        print(key)
        print(options[option_num])
        guess=input('A,B,C,D 중 하나를 입력하세요. ').upper()
        guesses.append(guess)
        correct+=check_answer(questions.get(key),guess)
        option_num+=1
    display_score(correct,guesses)

def check_answer(answer,guess):
    if answer==guess:
        print('정답!')
        return 1
    else:
        print('오답..')
        return 0

def display_score(correct_num,guesses_list):
    print('결과')
    print('---------------')
    print('입력 : ',end="")
    for i in guesses_list:
        print(i,end='')
    print('')
    print('정답 : ',end="")
    for i in questions:
        print(questions.get(i),end='')
    print('')
    print(int(correct_num/len(guesses_list)*100),'점 입니다!')

def play_again():
    
    response=input('다시 하겠습니까? (네,아니오)')
    if response=='네':
        return True
    else:
        return False
    

questions={'대한민국의 수도는?':'A','일본의 수도는?':'C', '미국의 수도는?':'B','중국의 수도는?':'D'}
options=[['A : 서울, B : 대전, C : 대구, D : 부산'],['A : 오사카, B : 삿포로, C : 도쿄, D : 오키나와'],
['A : 뉴욕, B : 워싱턴 DC, C : 하와이, D : 뉴저지'],['A : 후안, B : 동경, C : 만주, D : 베이징']]

new_game()

while play_again():
    new_game()

print('게임 종료')