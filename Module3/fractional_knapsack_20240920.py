from sys import stdin


def optimal_value(capacity, weights, values):
    value = 0.
    # write your code here
    # 가치/무게 비율과 함께 아이템 정보를 (비율, 무게, 가치)로 저장
    items = [(values[i] / weights[i], weights[i], values[i]) for i in range(len(weights))]
    
    #가치/무게 비율이 높은 순으로 정렬
    items.sort(reverse=True, key=lambda x: x[0])
    
    #각 아이템을 가능한 한 많이 배낭에 담는다
    for value_per_weight, weight, value_of_item in items:
        if capacity == 0:
            break # 배낭이 가득 차면 종료 
        
        #현재 아이템을 배낭에 담을 수 잇는 최대 양
        amount = min(weight, capacity)
        value += amount * value_per_weight # 현재 아이템을 가능한 만큼 담고, 그 가치를 더함
        capacity -= amount #배낭 남은 용량 갱신 

    return value


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = optimal_value(capacity, weights, values)
    print("{:.3f}".format(opt_value))
