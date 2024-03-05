import sys
sys.stdin = open('1210_input.txt')

# 각각의 테스트 케이스에 대하여
# 사다리 배열은 indexError 를 대비해서 좌우로 0 원소를 추가
for t in range(10):
    case_number = int(input())
    ladder = []
    for n in range(100):
        ladder.append([0] + list(map(int, input().split())) + [0])

    # column index 만 따로 starts 리스트에 담기
    column = []
    for j in range(102):
        if ladder[0][j] == 1:
            column.append(j)

    # 주어진 finish 조건 확인
    finish = ladder[99].index(2)

    # finish 에서 출발하여 start 지점 확인 및 출력
    x = column.index(finish)
    for i in range(99, -1, -1):
        if ladder[i][column[x] - 1] == 1:
            x -= 1
        elif ladder[i][column[x] + 1] == 1:
            x += 1
    print(f'#{case_number} {column[x] - 1}')






