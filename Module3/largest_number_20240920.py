from functools import cmp_to_key

def compare(x, y):
    # x+y와 y+x를 비교하여 큰 순서로 정렬
    if x + y > y + x:
        return -1  # x should come before y
    elif x + y < y + x:
        return 1   # y should come before x
    else:
        return 0   # x and y are equal in terms of concatenation

def largest_number(numbers):
    # 모든 숫자를 문자열로 변환
    numbers = list(map(str, numbers))
    # compare 함수 기준으로 정렬
    numbers.sort(key=cmp_to_key(compare))
    # 정렬된 숫자들을 연결하여 최종 결과 생성
    largest_num = ''.join(numbers)
    # 앞에 0이 여러 개 붙는 경우를 방지 (000 -> 0)
    return largest_num if largest_num[0] != '0' else '0'

if __name__ == '__main__':
    _ = int(input())  # 입력 수 개수는 사용되지 않으므로 _
    input_numbers = list(map(int, input().split()))  # 입력된 숫자들을 리스트로 받음
    print(largest_number(input_numbers))
