import random


def game():
    print('가위 바위 보 !!!')
    rule = {0: '가위', 1: '바위', 2: '보'}
    ai = random.choice([0, 1, 2])
    ai_choice = rule[ai]
    admin = input('가위, 바위, 보 중 하나를 선택하세요: ')

    if admin not in rule.values():
        print('가위, 바위, 보 중에서 선택해야 합니다!')
        return None

    admin = list(rule.keys())[list(rule.values()).index(admin)]
    admin_choice = rule[admin]
    print('나:', admin_choice)
    print('AI:', ai_choice)

    if admin == ai:
        print('비겼다!!')
        return 'tie'
    elif (admin + 1) % 3 == ai:
        print('졌어..!')
        return 'lose'
    else:
        print('이겼어!!!')
        return 'win'


def main():
    score = {'win': 0, 'lose': 0, 'tie': 0}
    while True:
        result = game()
        if result is not None:
            score[result] += 1

        print('현재 스코어 - 승리 횟수:', score['win'], '| 패배 횟수:',
              score['lose'], '| 비긴 횟수:', score['tie'])
        restart = input('게임을 다시 시작하겠습니까? (Y, N): ')
        if restart.lower() != 'y':
            print('게임을 종료합니다!')
            break


if __name__ == '__main__':
    main()
