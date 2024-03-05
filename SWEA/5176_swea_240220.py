import sys
sys.stdin = open('5176_im_input.txt')

# 중위 순회
def inorder(now):
    if 0 < now <= N:
        inorder(tree[now][1])
        write(now)
        inorder(tree[now][2])

# 값 저장
def write(now):
    global num
    tree[now][0] = num
    num += 1

for t in range(1, int(input()) + 1):
    N = int(input())
    num = 1

    tree = [[0, 2 * i, 2 * i + 1] for i in range(N + 1)]
    inorder(1)

    print(f'#{t} {tree[1][0]} {tree[N//2][0]}')




'''
도전 → 실패

def inorder_traverse(x):
    if x:
        inorder_traverse(tree[x][0])
        number.append(x)
        inorder_traverse(tree[x][1])

T = int(input())
for t in range(1, T + 1):
    N = int(input())

    tree = [[1]]
    cnt = N - 1
    while cnt > 0:
        tree.append([tree[-1][-1] + 1, tree[-1][-1] + 2])
        cnt -= 2
        if cnt == 1:
            tree.append([tree[-1][-1] + 1, 0])
            cnt -= 1
    tree += [[0, 0] for _ in range(N - len(tree))]

    print(tree)

    number = [0]
    inorder_traverse(1)
'''