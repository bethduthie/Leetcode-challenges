def createTargetArray(nums, index):
    ans = []
    for x, y in zip(nums, index):
        ans.insert(y,x)
    return ans


print(createTargetArray([0,1,2,3,4], [0,1,2,2,1]))
