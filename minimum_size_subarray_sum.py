def minSubArrayLen(target: int, nums: list[int]) -> int:
    sub_arr_cnt = set()
    curr_sum = nums[0]
    l, r = 0, 0
    n = len(nums)
    while l < n:
        print(l, r, [nums[i] for i in range(l, r + 1)], curr_sum)
        if l == r and nums[l] >= target:
            return 1
        elif curr_sum >= target:
            curr_sum -= nums[l]
            sub_arr_cnt.add(r - l + 1)
            l += 1
        else:
            r += 1
            if r == n:
                break
            else:
                curr_sum += nums[r]

    return min(sub_arr_cnt) if sub_arr_cnt else 0


print(minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
