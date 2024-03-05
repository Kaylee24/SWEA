import sys
sys.stdin = open('5102_im_input.txt')

def bfs(start, finish, N):    # 시작정점 start, 도착정점 finish, 노드 개수 N
    q = []                    # 큐
    visited = [0] * (N + 1)   # visited
    q.append(start)           # 시작점 인큐
    visited[start] = 1        # 시작점 방문 표시
    while q:                  # 큐가 비워질 때까지 (남은 정점이 있으면)
        t = q.pop(0)
        # t 에서 할일...
        for i in adjl[t]:     # t 에 인접인 정점 i
            if visited[i] == 0:   # 방문하지 않은 정점이면
                q.append(i)   # 인큐
                visited[i] = 1 + visited[t]   # 방문표시
            if i == finish:
                return visited[i] - 1
    return 0

T = int(input())
for t in range(1, T + 1):
    V, E = map(int, input().split())
    node = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())
    # 인접리스트
    adjl = [[] for _ in range(V + 1)]
    for i in range(E):
        adjl[node[i][0]].append(node[i][1])
        adjl[node[i][1]].append(node[i][0])   # 무향그래프

    print(f'#{t} {bfs(S, G, V)}')