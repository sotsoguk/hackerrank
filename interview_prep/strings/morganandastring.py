def morgan(a,b):
    output = []
    a += 'z'
    b += 'z'
    
    for _ in range(len(a) + len(b) - 2):
        if a < b:
            output.append(a[0])
            a = a[1:]
        else:
            output.append(b[0])
            b = b[1:]
    # print(output)
    return "".join(output)

def main():
    t = "JACK"
    for c in range(4):
        print(t[0])
        t = t[1:]
    print(morgan("ABACABA","ABACABA"))
    return 0

if __name__ == "__main__":
    main()