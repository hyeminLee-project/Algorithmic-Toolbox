def optimal_summands(n):
    summands = []
    current_number = 1
    
    # write your code here
    while n > 0:
        # 남은 n에서 current_number를 더할 수 있는지 확인
        if n - current_number > current_number:
            summands.append(current_number)
            n -= current_number
        else:
            # 더할 수 없는 경우, 남은 n을 추가하고 종료
            summands.append(n)
            break
        current_number += 1

    return summands


if __name__ == '__main__':
    n = int(input())
    summands = optimal_summands(n)
    print(len(summands))
    print(*summands)
