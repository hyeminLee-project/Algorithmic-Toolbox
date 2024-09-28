def fibonacci_number(n):
    if n <= 1:
        return n

    # 배열을 사용해 동적 프로그래밍 방식으로 피보나치 수를 저장
    fib = [0] * (n + 1)
    fib[1] = 1

    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]

    return fib[n]

if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))
