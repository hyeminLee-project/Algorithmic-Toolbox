#def binary_search(keys, query):
#    # write your code here
#    pass
#
#
#if __name__ == '__main__':
#    num_keys = int(input())
#    input_keys = list(map(int, input().split()))
#    assert len(input_keys) == num_keys
#
#    num_queries = int(input())
#    input_queries = list(map(int, input().split()))
#    assert len(input_queries) == num_queries
#
#    for q in input_queries:
#        print(binary_search(input_keys, q), end=' ')

def binary_search(keys, query):
    left, right = 0, len(keys) - 1
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if keys[mid] == query:
            result = mid          # 현재 발견된 위치를 저장하고
            right = mid - 1       # 더 왼쪽에 같은 값이 있는지 확인
        elif keys[mid] < query:
            left = mid + 1        # 검색 범위를 오른쪽으로 이동
        else:
            right = mid - 1       # 검색 범위를 왼쪽으로 이동
    return result

if __name__ == '__main__':
    num_keys = int(input())  # 배열의 크기 입력
    input_keys = list(map(int, input().split()))  # 정렬된 배열 입력
    assert len(input_keys) == num_keys  # 배열의 길이가 올바른지 확인

    num_queries = int(input())  # 쿼리의 개수 입력
    input_queries = list(map(int, input().split()))  # 쿼리 배열 입력
    assert len(input_queries) == num_queries  # 쿼리의 길이가 올바른지 확인

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')
