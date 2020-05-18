def smallerNumbersThanCurrent(nums):
    how_many_smaller = []
    for i in range(len(nums)):
        count = 0
        for j in range(len(nums)):
            if i != j and nums[i] > nums[j]:
                count += 1
        how_many_smaller.append(count)
    return  how_many_smaller



print(smallerNumbersThanCurrent([8,1,2,2,3]))
