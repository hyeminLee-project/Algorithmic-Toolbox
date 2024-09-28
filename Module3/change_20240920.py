def change(money):
    # write your code here
    coins = [10, 5, 1]
    count = 0 # count of coins  
    for coin in coins: 
        count += money // coin # 해당 동전으로 교환할 수 있는 개수를 더함
        money %= coin  # 남은 금액을 계산

    return count


if __name__ == '__main__':
    m = int(input())
    print(change(m))
