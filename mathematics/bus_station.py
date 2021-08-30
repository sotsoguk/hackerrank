from itertools import accumulate
import math
def bus(g):
    a = list(accumulate(g))
    num_groups = len(g)
    num_people = a[-1]
    max_group = max(g)
    max_busses = math.ceil(num_people / max_group)
    # print(num_groups,num_people)
    print(a)
    busses = []
    for i in range(1,max_busses+1):
        if num_people % i != 0:
            pass
        else:
            bus_size = num_people // i
            print(bus_size,i)
            # sizes = [bus_size*b for b in range(1,i+1)]
            # # print(i,sizes)
            # if all([x in a for x in sizes]):
            #     busses.append(bus_size)
            j  = 1
            fits = True
            while j<i+1 and fits == True:
                print("x",j*bus_size)
                if j*bus_size not in a:
                    fits = False
                j += 1
            if fits == True:
                busses.append(bus_size)

    return busses[::-1]
def main():
    # t1 = [1,2,1,1,1,2,1,3]
    t1 = [2,2,1,1,1,1,1,2,1,2]
    print(bus(t1))
    
    a = [1,2]
    b = [3,4,1]

    print(all([i in b for i in a]))
    return 0

if __name__ == "__main__":
    main()