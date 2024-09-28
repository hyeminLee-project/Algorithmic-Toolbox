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
    # F(n+2) - 1이 전체 합이므로, n+2번째 피보나치를 구한다.
    pisano_period = get_pisano_period(10)
    n = (n + 2) % pisano_period
    fib_n_plus_2 = fibonacci_mod(n, 10)
    
    if fib_n_plus_2 == 0:
        return 9
    else:
        return (fib_n_plus_2 - 1) % 10

def fibonacci_partial_sum(from_, to):
    if from_ == 0:
        return fibonacci_sum(to)
    
    # 전체 합에서 from_ 이전 부분을 빼면 구간 합이 된다.
    sum_to = fibonacci_sum(to)
    sum_from_minus_1 = fibonacci_sum(from_ - 1)

    return (sum_to - sum_from_minus_1) % 10


if __name__ == '__main__':
    from_, to = map(int, input().split())
    print(fibonacci_partial_sum(from_, to))
