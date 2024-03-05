import sys
sys.stdin = open('4821_input.txt')

# 테스트 케이스의 수 입력 받기
T = int(input())

# 각 테스트 케이스에 대해 입력값 받기
for t in range(1, T + 1):
    N = int(input())
    N_list = list(map(int, input().split()))

    # 최댓값, 최솟값 구하고 두 수간의 차 출력하기
    result = max(N_list) - min(N_list)
    print(f'#{t} {result}')