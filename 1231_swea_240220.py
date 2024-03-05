import sys
sys.stdin = open('1231_hw_input.txt')

# 중위순회 재귀함수
def inorder_traverse(X):   # root 노드를 X 에 대입
    if X:  # if X != 0: (자식 여부 확인)
        inorder_traverse(left[X])
        print(nodes[X-1][1], end='')
        inorder_traverse(right[X])


for t in range(1, 11):
    N = int(input())
    nodes = [list(input().split()) for _ in range(N)]

    # 자식 노드 정리
    left = [0] * (N + 1)
    right = [0] * (N + 1)
    for n in range(N):
        if len(nodes[n]) == 4:
            left[n + 1] = int(nodes[n][2])
            right[n + 1] = int(nodes[n][3])
        elif len(nodes[n]) == 3:
            left[n + 1] = int(nodes[n][2])

    print(f'#{t}', end=' ')
    inorder_traverse(1)
    print()