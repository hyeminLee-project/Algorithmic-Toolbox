def get_pisano_period(m):
    previous, current = 0, 1
    for i in range(m * m):
        previous, current = current, (previous + current) % m
        # 피사노 주기는 항상 0, 1로 시작한다
        if previous == 0 and current == 1:
            return i + 1

def fibonacci_huge(n, m):
    # 피사노 주기를 계산
    pisano_period = get_pisano_period(m)
    
    # 피보나치 n을 Pisano 주기 내의 값으로 변환
    n = n % pisano_period

    if n <= 1:
        return n

    previous, current = 0, 1
    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m

if __name__ == '__main__':
    n, m = map(int, input().split())
    print(fibonacci_huge(n, m))
