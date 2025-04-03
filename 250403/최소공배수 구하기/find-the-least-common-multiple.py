n, m = map(int, input().split())

min_num = min(n,m)
gcd =1
for i in range (1,max_num):
    if n % i ==0 and m%i ==0:
        gcd = i

def lcm(n, m):
    return abs(n * m) // gcd

lcm()


# Please write your code here.