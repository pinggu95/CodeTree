n, m = map(int, input().split())

max_num = max(n,m)
gcd =1
def gcd_num():
    for i in range (1,max_num):
        if n % i ==0 and m%i ==0:
            gcd = i

    print(gcd)  
gcd_num()

      
# Please write your code here.