import sys
sys.stdin = open('hw_input.txt')

# 회문 찾아서 회문 개수 반환하는 함수 정의
def palindrome(words, length):
    # 회문 개수 변수 설정
    count = 0
    # 모든 row 를 순회하며
    for i in range(8):
        # 회문의 첫 문자를 기준으로 찾고자 하는 회문의 길이를 고려하여
        # column 순회 범위 설정
        for j in range(9 - length):
            # 가능한 모든 경우 슬라이싱
            test_word = words[i][j : j + length]
            # 슬라이싱한 문자열이 회문이라면 회문 개수 변수에 카운팅
            if test_word == test_word[::-1]:
                count += 1
    # 최종 회문 개수 반환
    return count

# 각각의 테스트 케이스에 대하여
# 찾고자 하는 회문의 길이와 글자판 정보 입력
for t in range(1, 11):
    length = int(input())
    words = [list(input()) for _ in range(8)]

    # 글자판 전치행렬 준비
    reverse_words = [[0] * 8 for _ in range(8)]
    for i in range(8):
        for j in range(8):
            reverse_words[i][j] = words[j][i]

    # 글자판과 글자판의 전치행렬에 대해 회문을 찾아서 그 합을
    # 조건에 맞게 출력
    print(f'#{t} {palindrome(words, length) + palindrome(reverse_words, length)}')