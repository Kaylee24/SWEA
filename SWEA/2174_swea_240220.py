import sys
sys.stdin = open('2174_im_input.txt')

T = int(input())
for t in range(1, T + 1):
    E, N = map(int, input().split())          # 간선의 개수 E, N
    nodes = list(map(int, input().split()))   # 간선 정보 nodes

    kids1 = [0] * (E + 2)   # 간선 정보 담을 리스트 - 왼쪽 자식
    kids2 = [0] * (E + 2)   # 간선 정보 담을 리스트 - 오른쪽 자식
    # 왼쪽 자식, 오른쪽 자식 나눠서 간선 정보 담기
    for e in range(E):
        if kids1[nodes[2 * e]] == 0:
            kids1[nodes[2 * e]] = nodes[2 * e + 1]
        else:
            kids2[nodes[2 * e]] = nodes[2 * e + 1]

    q = [N]   # 큐
    cnt = 1   # 서브 트리에 속한 노드의 수
    while q:
        n = q.pop(0)
        if kids1[n] != 0:           # 왼쪽 자식 정보부터 확인
            q.append(kids1[n])
            cnt += 1
            if kids2[n] != 0:       # 오른쪽 자식 정보 확인
                q.append(kids2[n])
                cnt += 1

    # 결과 출력
    print(f'#{t} {cnt}')