
def fibonacci_last_digit(n):
    # 피사노 주기의 길이는 60이다 (mod 10)
    pisano_period = 60
    
    # n이 매우 크다면, n % 60을 사용하여 계산을 최적화한다
    n = n % pisano_period
    
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, (previous + current) % 10

    return current

if __name__ == '__main__':
    n = int(input())
    print(fibonacci_last_digit(n))


