def seq(n):
    # if (n-2) % 4 == 0:
    #     return 0
    
    j = n // 4
    result = 0
    for i in range(4*j,n+1):
        result ^= i
    return result

def xors(n):
    
    result = 0
    if n % 2 == 0:
        return seq(n//2)*2
    else:
        result = seq((n-1) //2) * 2
        if ((n-1) // 2 +1 ) % 2 == 1:
            return result + 1
        else:
            return result
    
def x(l,r):
    return xors(r)^xors(l-1)
def main():
    
    for i in range(20):
        print(i,xors(i))

   # print(seq(8))
    
    # for j in range(20):
    #     t = 0
    #     for i in range(j+1):
    #         t ^= i
    #     print(j,seq(j),t)
    print(x(15,20))
    return 0
if __name__ == "__main__":
    main()