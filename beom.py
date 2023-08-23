import random


def game():
    num = random.randint(1, 100)
    count = 0
    num_a = 100
    print('숫자를 맞춰보세요!')
    while True:
        try:
            admin = input("숫자를 입력하세요 (끝내고 싶으면 '종료'를 입력해주세요!): ")
            if admin.lower() == '종료':
                return None
            admin = int(admin)
            if admin < 1 or admin > 100:
                print('----1에서 100 사이의 숫자를 입력하세요!----')
                continue
            count += 1
            if admin == num:
                print('----------{}정답입니다!----------'.format(admin))
                print('시도 횟수: ' + str(count))
                return count
            elif num_a < admin:
                print('---1에서 100 사이의 숫자만 입력해주세요!---')
            elif num < admin:
                print('----------{}보다 작습니다!----------'.format(admin))
                print('시도 횟수: ' + str(count))
            else:
                print('----------{}보다 큽니다!----------'.format(admin))
                print('시도 횟수: ' + str(count))
        except ValueError:
            print('-----숫자만 입력해주세요!-----')


def main():
    users = {}
    while True:
        nickname = input('닉네임을 입력해주세요!: ')
        if nickname in users:
            print('이전 게임 최고 시도 횟수:', users[nickname])
        print("게임을 시작하려면 '시작'를 입력하세요!")
        now = input("입력: ")
        if now.lower() == '시작':
            game_result = game()
            if game_result is not None:
                if nickname in users:
                    if game_result < users[nickname]:
                        users[nickname] = game_result
                else:
                    users[nickname] = game_result
        restart = input('게임을 다시 시작하겠습니까? (Y, N): ')
        if restart.lower() != 'y':
            print('게임을 종료합니다!')

            if nickname in users:
                users[nickname] = min(
                    users[nickname], users.get(nickname, float('inf')))
            sorted_users = sorted(users.items(), key=lambda x: x[1])
            rank = 1
            prev_score = float('inf')
            for user, score in sorted_users:
                if score != prev_score:
                    print('{}위 {} 최고 시도 횟수는 {}번 입니다!'.format(rank, user, score))
                else:
                    print('{}위 {} 최고 시도 횟수는 {}번 입니다!'.format(
                        rank - 1, user, score))
                rank += 1
                prev_score = score
            break


if __name__ == '__main__':
    main()
