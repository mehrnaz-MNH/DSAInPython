

def findMin( nums) :
    if nums[0] < nums[len(nums) - 1]:
        return nums[0]

    lo = 0
    hi = len(nums) - 1

    while lo < hi:
        mi = lo + (hi - lo) // 2
        if nums[mi] > nums[hi]:
            lo = mi + 1
        elif nums[mi] < nums[hi]:
            hi = mi

    return nums[lo]




