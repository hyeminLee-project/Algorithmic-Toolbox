def can_partition_three_subsets(values):
    total_sum = sum(values)
    if total_sum % 3 != 0:
        return 0
    
    target_sum = total_sum // 3
    n = len(values)
    values.sort(reverse=True)  # 내림차순 정렬

    # 메모이제이션을 위한 딕셔너리
    memo = {}

    def backtrack(index, subset_sums):
        if tuple(subset_sums) in memo:
            return memo[tuple(subset_sums)]
        
        # 모든 세 개의 부분집합이 목표 합에 도달했는지 확인
        if subset_sums[0] == target_sum and subset_sums[1] == target_sum:
            return True
        
        # 현재 값을 세 개의 부분집합 중 하나에 배치 시도
        for i in range(3):
            if subset_sums[i] + values[index] <= target_sum:
                subset_sums[i] += values[index]
                if backtrack(index + 1, subset_sums):
                    memo[tuple(subset_sums)] = True
                    return True
                subset_sums[i] -= values[index]  # 백트래킹

            # 현재 부분집합의 합이 0이면 중복 검사를 피하기 위해 중단
            if subset_sums[i] == 0:
                break
        
        memo[tuple(subset_sums)] = False
        return False

    return 1 if backtrack(0, [0, 0, 0]) else 0


if __name__ == '__main__':
    n = int(input().strip())
    input_values = list(map(int, input().strip().split()))
    
    print(can_partition_three_subsets(input_values))
