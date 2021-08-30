def createnums(n):
    nums = [9]
    new_nums = [9]
    for i in range(n):
        curr_nums = new_nums[:]
        new_nums =  []
        for k in curr_nums:
            new_nums.append(k*10)
            new_nums.append(k*10+9)
        nums.extend(new_nums)
        
    #print(nums)
    return nums
def specialm(n):
    nums = createnums(10)
    for i in nums:
        if i % n == 0:
            return i
    return 0 
def main():
    print(specialm(1))
    return 0

if __name__ == "__main__":
    main()