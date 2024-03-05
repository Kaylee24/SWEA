import sys
sys.stdin = open('4835_input.txt')

# 테스트 케이스 수 입력 받기
T = int(input())

# 테스트 케이스 별로 추가 입력값 받기
for t in range(1, T + 1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))

    # 구간합의 최대, 최소 비교값, 구간합을 담을 리스트 설정하기
    # maximum = 0
    # minimum = 10000 * M
    sums = []

    # 구간합 구하기
    for n in range(N - M + 1):
        part_numbers = numbers[n : n + M]
        part_sum = sum(part_numbers)
        sums.append(part_sum)

    # 구간합의 최댓값, 최솟값 구하고 두 값의 차 출력하기
    print(f'#{t} {max(sums) - min(sums)}')