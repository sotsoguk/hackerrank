def sd(arr):
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return arr[0]
    if len(arr) == 2:
        return (arr[0] + arr[1])%9
    
    # split into half
    m = len(arr) // 2
    a1 = arr[:m]
    a2 = arr[m:]
    return sd([sd(a1),sd(a2)])
def sd_mult(arr,k):
    s = sd(arr)
    ss = []
    for i in range(k):
        ss.append(s)
    return sd(ss)
def main():
    print(sd([1,4,8]))
    print(sd_mult([1,4,8],3))
    
    t = "1234531243"
    print(list(map(int,t)))
    return 0

if __name__ == "__main__":
    main()