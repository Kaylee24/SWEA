import sys
sys.stdin = open('1208_input.txt')

# 테스트 케이스 10개에 대해서
for testcase in range(1, 11):

    # 각각 입력값을 입력 받는다.
    N = int(input())
    heights = list(map(int, input().split()))

    # 상자들의 높이를 정렬한다.
    heights.sort()

    # 정렬한 상자들의 높이 중
    # 가장 낮은 상자의 높이 (list.[0]) 에는 1을 더하고,
    # 가장 높은 상자의 높이 (list.[-1]) 에는 1을 빼서
    # 평탄화를 진행한다.
    # 다시 한번 상자들의 높이를 정렬하고, 덤프 횟수를 1회 차감한다.
    while N != 0:
        heights[-1] -= 1
        heights[0] += 1
        heights.sort()
        N -= 1

    # 평탄화가 완료되면
    # 가장 높은 높이와 낮은 높이의 차를 출력한다.
    result = heights[-1] - heights[0]
    print(f'#{testcase} {result}')