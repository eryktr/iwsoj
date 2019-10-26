def fibn(n):
    if n < 2:
        return n
    cur, prev = 1, 0
    while n - 1:
        cur, prev, n = cur + prev, cur, n - 1
    return cur


if __name__ == "__main__":
    print(f"The 10th Fib number is {fibn(10)}")
