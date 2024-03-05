import sys
sys.stdin = open('1232_hw_input.txt')

operator = ['+', '-', '*', '/']
result = 0

def operate(node):
    global result
    if tree[node][1] == '+':
        result = tree[tree[node][2] - 1][1] + tree[tree[node][3] - 1][1]
    elif tree[node][1] == '-':
        result = tree[tree[node][2] - 1][1] - tree[tree[node][3] - 1][1]
    elif tree[node][1] == '*':
        result = tree[tree[node][2] - 1][1] * tree[tree[node][3] - 1][1]
    elif tree[node][1] == '/':
        result = tree[tree[node][2] - 1][1] / tree[tree[node][3] - 1][1]
    tree[node][1] = result

def f(node):
    while tree[node][1] in operator:
        f(tree[node][2] - 1)
        f(tree[node][3] - 1)
        operate(node)

for t in range(1, 11):
    N = int(input())   # 정점의 개수
    tree = [list(input().split()) for _ in range(N)]

    for i in range(N):   # node 정보 자료형 정리
        for j in range(len(tree[i])):
            try:
                tree[i][j] = int(tree[i][j])
            except:
                pass

    f(0)
    print(f'#{t} {int(tree[0][1])}')