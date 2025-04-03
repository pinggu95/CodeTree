n, m = map(int, input().split())

def gcd(n, m):
    min_num = min(n, m)
    gcd = 1
    for i in range(1, min_num + 1):
        if n % i == 0 and m % i == 0:
            gcd = i
    return gcd

def lcm(n, m):
    return abs(n * m) // gcd(n, m)

lcm()