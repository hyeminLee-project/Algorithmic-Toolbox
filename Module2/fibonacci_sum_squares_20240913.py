def get_pisano_period(m):
    previous, current = 0, 1
    for i in range(m * m):
        previous, current = current, (previous + current) % m
        if previous == 0 and current == 1:
            return i + 1

def fibonacci_mod(n, m):
    if n <= 1:
        return n
    
    previous, current = 0, 1
    for _ in range(n - 1):
        previous, current = current, (previous + current) % m

    return current

def fibonacci_sum_squares(n):
    # 피사노 주기 계산 (mod 10)
    pisano_period = get_pisano_period(10)
    
    # n을 피사노 주기 안으로 변환
    n = n % pisano_period
    
    # F(n)와 F(n+1) 계산
    fib_n = fibonacci_mod(n, 10)
    fib_n_plus_1 = fibonacci_mod(n + 1, 10)
    
    # F(n) * F(n+1)의 결과를 10으로 나눈 나머지
    return (fib_n * fib_n_plus_1) % 10

if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum_squares(n))
