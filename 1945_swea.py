import sys
sys.stdin = open('1945_extra_input.txt')

# 테스트 케이스 입력
T = int(input())

# 각각의 테스트 케이스에 대하여 숫자 입력
for t in range(1, T + 1):
    N = int(input())

    # 소인수분해 할 소수를 담은 리스트와
    # 소수별 개수를 담을 리스트 준비
    decimal = [2, 3, 5, 7, 11]
    abcde = [0] * 5

    # 주어진 수가 1이 될때까지
    while N > 1:
        # 소수를 순회하며 주어진 숫자를 나누어 떨어지게 하는 소수의 개수를 카운팅
        for i in range(5):
            while N % decimal[i] == 0:
                abcde[i] += 1
                N /= decimal[i]

    # 결과 출력
    print(f'#{t}', *abcde)