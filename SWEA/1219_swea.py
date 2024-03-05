import sys
sys.stdin = open('1219_hw_input.txt')

# 정해지지 않은 수의 값 입력
while 1:
    try:
        T, N = map(int, input().split())
        ways = list(map(int, input().split()))

        # 길 정리
        ways1 = [0] * 100
        ways2 = [0] * 100

        for i in range(len(ways)):
            if i % 2 == 0:   # ways 짝수 index 는 출발 지점, 홀수 index 는 도착 지점
                if ways1[ways[i]] == 0:   # 길 존재하면 ways1 우선 저장
                    ways1[ways[i]] = ways[i + 1]
                else:                     # 갈림길 존재하면 ways2 저장
                    ways2[ways[i]] = ways[i + 1]

        current = 0   # 현재 위치
        tried = [0]   # 분기점으로 돌아가기 위한 stack
        visited = 0   # 도착지에 도착 못했을 때의 종료조건을 위한 지나온 길 수를 담을 변수

        while current != 99:
            # 길이 있을 때
            if ways1[current] != 0:
                current = ways1[current]
                tried.append(current)
                visited += 1
            # 길이 없을 때
            else:
                # 갈림길 찾을 때까지 돌아가기
                while ways2[current] == 0:
                    tried.pop()
                    current = tried[-1]
                current = ways2[current]
                tried.append(current)
                visited += 1
            # 결과 출력 - 도착지점에 도달하지 못한 경우
            if visited == N:
                print(f'#{T} 0')
                break

        # 결과 출력 - 도착지점에 도달한 경우
        if current == 99:
            print(f'#{T} 1')

    # 정해지지 않은 수의 값 입력 - 더 이상 입력할 값이 없을 때의 종료 조건
    except:
        break