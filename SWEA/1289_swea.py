import sys
sys.stdin = open('1289_extra_input.txt')

# 테스트 케이스 수 입력
T = int(input())

# 각각의 테스트 케이스에 대하여 단어 입력
for t in range(1, T + 1):
    word = input()
    # 슬라이싱을 이용하여 입력 받은 단어 reverse 하고
    # 회문인지 확인 후 결과 출력
    if word == word[::-1]:
        print(f'#{t} 1')
    else:
        print(f'#{t} 0')