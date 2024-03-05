import sys
sys.stdin = open('4865_im_input.txt')

# 테스트 케이스 수 입력
T = int(input())

# 각각의 테스트 케이스에 대하여 문자열 2개 입력
# 이때, 각각의 문자를 원소로 한 리스트로 입력한다.
for t in range(1, T + 1):
    str1 = list(input())
    str2 = list(input())

    # str1의 각각의 문자에 대하여 str2에 있는 수를 담을 빈 리스트 설정
    # str1의 원소들을 순회하며 str2에서 수를 확인하여 counts 리스트에 저장
    counts = []
    for s in str1:
        if s in str2:
            counts.append(str2.count(s))

    # count 최댓값 조회해서 조건에 맞춰 결괏값 출력
    print(f'#{t} {max(counts)}')