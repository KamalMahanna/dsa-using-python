# # wrong
# def twoSum(numbers: list[int], target: int) -> list[int]:
#     n = len(numbers)
#     for i in range(n):
#         for j in range(n - 1, i, -1):
#             if numbers[i] + numbers[j] == target:
#                 return [i + 1, j + 1]
#             elif numbers[i] + numbers[j] < target:
#                 break
#     return [-1]

# # wrong
# def twoSum_(numbers: list[int], target: int) -> list[int]:
#     n = len(numbers)
#     for i in range(n - 1, 0, -1):
#         for j in range(i):
#             if numbers[i] + numbers[j] == target:
#                 return [j + 1, i + 1]
#             elif numbers[i] + numbers[j] > target:
#                 break
#     return [-1]


def twoSum(numbers: list[int], target: int) -> list[int]:
    n = len(numbers)
    left, right = 0, n - 1
    while left < right:
        if numbers[left] + numbers[right] == target:
            return [left + 1, right + 1]
        elif numbers[left] + numbers[right] > target:
            right -= 1
        else:
            left += 1
    return [-1]


print(twoSum([1, 2, 3, 5, 7], 6))
print(twoSum([1, 2, 7, 9, 13], 3))
print(twoSum([1, 2, 7, 9, 13], 11))
print(twoSum([1, 2, 7, 9, 13], 15))
