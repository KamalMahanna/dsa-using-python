from numpy import inf


def threeSumClosest(nums, target) -> int:
    n = len(nums)
    nums.sort()
    diff = inf
    for i in range(n - 2):
        l, r = i + 1, n - 1
        while l < r:
            total = nums[i] + nums[l] + nums[r]
            if total == target:
                return target
            elif total > target:
                r -= 1
            else:
                l += 1
            curr_diff = abs(total - target)
            if curr_diff < diff:
                diff = curr_diff
                global_min = total
    return global_min


print(threeSumClosest([10, 20, 30, 40, 50, 60, 70, 80, 90], 1))
print(threeSumClosest([-1, 2, 1, -4], 1))
