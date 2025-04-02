n = int(input())

def num():
    number = list(range(1,n*n+1))
    index = 0
    
    for i in range(n):
        for j in range(n):
            print(number[index],end = ' ')
            index += 1

            if index == 9:
                index = 0
        print()        
num()