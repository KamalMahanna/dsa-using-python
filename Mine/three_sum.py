def threeSum_(nums: list[int]) -> list[list[int]]:
    nums.sort()
    a = []
    n = len(nums)
    for i in range(n - 2):
        if i != 0:
            if nums[i] == nums[i - 1]:
                continue
        print(i)
        l = i + 1
        r = n - 1
        while l < r:
            print(l, r, "bef")
            if nums[l] + nums[r] == -nums[i]:
                a.append([nums[i], nums[l], nums[r]])
                l += 1
                r -= 1
            elif nums[l] + nums[r] > -nums[i]:
                r -= 1
            else:
                l += 1
            while l < r and nums[l] == nums[l + 1]:
                l += 1
            while l < r and nums[r] == nums[r - 1]:
                r -= 1
            print(l, r, "af")

    return a


def threeSum(nums: list[int]) -> list[list[int]]:
    nums.sort()
    a = []
    n = len(nums)

    for i in range(n - 2):
        # Cleaned up outer duplicate check
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        l = i + 1
        r = n - 1

        while l < r:
            print(l, r, "bef")

            current_sum = nums[l] + nums[r]

            if current_sum == -nums[i]:
                a.append([nums[i], nums[l], nums[r]])

                # Move this duplicate skipping INSIDE the successful match block
                while l < r and nums[l] == nums[l + 1]:
                    l += 1
                while l < r and nums[r] == nums[r - 1]:
                    r -= 1

                # Advance both pointers to look for the next distinct combination
                l += 1
                r -= 1

            elif current_sum > -nums[i]:
                r -= 1
            else:
                l += 1
            print(l, r, "af")

    return a


print(threeSum([-1, 0, 1, 2, -1, -4]))
print(threeSum([1, 2, 0, 1, 0, 0, 0, 0]))
print(threeSum([0, 1, 1]))
print(threeSum([0, 0, 0, 0, 0]))
