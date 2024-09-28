#from itertools import combinations
#
#
#def inversions_naive(a):
#    number_of_inversions = 0
#    for i, j in combinations(range(len(a)), 2):
#        if a[i] > a[j]:
#            number_of_inversions += 1
#    return number_of_inversions
#
#
#if __name__ == '__main__':
#    input_n = int(input())
#    elements = list(map(int, input().split()))
#    assert len(elements) == input_n
#    print(inversions_naive(elements))

def merge_and_count(arr, temp_arr, left, mid, right):
    i = left    # 왼쪽 부분 배열의 시작 인덱스
    j = mid + 1 # 오른쪽 부분 배열의 시작 인덱스
    k = left    # 병합된 배열의 시작 인덱스
    inv_count = 0

    # 왼쪽과 오른쪽 배열을 비교하며 병합
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            i += 1
        else:
            temp_arr[k] = arr[j]
            inv_count += (mid - i + 1)  # 왼쪽 배열에서 남은 요소들 만큼 역순쌍 증가
            j += 1
        k += 1

    # 왼쪽 배열의 남은 요소들 복사
    while i <= mid:
        temp_arr[k] = arr[i]
        i += 1
        k += 1

    # 오른쪽 배열의 남은 요소들 복사
    while j <= right:
        temp_arr[k] = arr[j]
        j += 1
        k += 1

    # 임시 배열의 내용을 원래 배열에 복사
    for i in range(left, right + 1):
        arr[i] = temp_arr[i]
        
    return inv_count

def merge_sort_and_count(arr, temp_arr, left, right):
    inv_count = 0
    if left < right:
        mid = (left + right) // 2

        inv_count += merge_sort_and_count(arr, temp_arr, left, mid)
        inv_count += merge_sort_and_count(arr, temp_arr, mid + 1, right)

        inv_count += merge_and_count(arr, temp_arr, left, mid, right)

    return inv_count

if __name__ == '__main__':
    input_n = int(input())  # 배열의 크기 입력
    elements = list(map(int, input().split()))  # 배열의 요소 입력
    assert len(elements) == input_n  # 배열의 길이 확인

    temp_arr = [0] * input_n  # 병합 정렬을 위한 임시 배열
    result = merge_sort_and_count(elements, temp_arr, 0, input_n - 1)
    print(result)
