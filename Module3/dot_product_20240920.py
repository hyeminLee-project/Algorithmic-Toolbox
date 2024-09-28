from itertools import permutations


def max_dot_product(first_sequence, second_sequence):
    # 두 수열을 각각 내림차순으로 정렬
    first_sequence.sort(reverse=True)
    second_sequence.sort(reverse=True)
    
    #내림차순으로 정렬한 두 수열의 같은 인덱스 값끼리 곱해서 더함
    max_product = sum(first_sequence[i] * second_sequence[i] for i in range(len(first_sequence)))
    return max_product


if __name__ == '__main__':
    n = int(input()) #입력: 수열의 길이
    prices = list(map(int, input().split()))
    clicks = list(map(int, input().split()))
    
    # 점곱의 최대값을 계산하고 출력
    print(max_dot_product(prices, clicks))
    
