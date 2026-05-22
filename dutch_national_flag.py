def sortColors(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    n=len(nums)
    l=0
    m=0
    r=n-1
    while m<=r:
        if nums[m]==0:
            nums[l], nums[m] = nums[m], nums[l]
            l+=1
            m+=1
        elif nums[m] ==2:
            nums[r],nums[m] = nums[m],nums[r]
            r-=1
        elif nums[m]==1:
            m+=1
        print(nums)
    # print(nums)

sortColors([2,0,2,1,1,0])
sortColors([2,0,1])