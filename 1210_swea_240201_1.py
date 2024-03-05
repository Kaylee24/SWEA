import sys
sys.stdin = open('1210_input.txt')

# 각각의 테스트 케이스에 대하여
# 사다리 배열은 indexError 를 대비해서 좌우로 0 원소를 추가
for t in range(10):
    case_number = int(input())
    ladder = []
    for n in range(100):
        ladder.append([0] + list(map(int, input().split())) + [0])

    # 시작 지점만 따로 starts 리스트에 담기
    starts = []
    for j in range(102):
        if ladder[0][j] == 1:
            starts.append(j)

    # 시작 지점들을 순회하며
    # 아래 row 로 내려갈 때마다 좌우 값이 1인지 확인
    # 좌우 중 값이 1인 칸이 있다면 column 좌표를 수정하고 다시 아래 row 로 이동
    # 이때 column 좌표는 사다리의 기둥 기준(시작 지점들의 집합 starts)과 동일
    for s in range(len(starts)):
        start = starts[s]
        x = s
        for i in range(100):
            # print(f'현재 위치 : {i}, {starts[x]}')
            if ladder[i][starts[x]-1] == 1:
                x -= 1
            elif ladder[i][starts[x]+1] == 1:
                x += 1
        if ladder[99][starts[x]] == 2:
            print(f'#{case_number} {start - 1}')
            break