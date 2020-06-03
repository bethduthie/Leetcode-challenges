def maxProduct(nums):
    nums.sort(reverse=True)
    i = str(nums[0])
    j = str(nums[1])
    return (int(i)-1)*(int(j)-1)
