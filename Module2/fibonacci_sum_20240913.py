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

def fibonacci_sum(n):
    # 피보나치 수열의 합은 F(n+2) - 1
    pisano_period = get_pisano_period(10)
    n = (n + 2) % pisano_period

    # F(n+2)를 계산하고 1을 뺀 후 10으로 모듈 연산
    fib_n_plus_2 = fibonacci_mod(n, 10)
    
    if fib_n_plus_2 == 0:
        return 9
    else:
        return (fib_n_plus_2 - 1) % 10

if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum(n))
