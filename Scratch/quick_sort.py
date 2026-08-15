def sort(arr):

    if len(arr) < 2:
        return arr

    l_arr, r_arr = [], []
    pivot_ele_idx = len(arr) // 2

    for i in range(len(arr)):
        if i == pivot_ele_idx:
            continue
        elif arr[i] >= arr[pivot_ele_idx]:
            r_arr.append(arr[i])
        else:
            l_arr.append(arr[i])
    return sort(l_arr) + [arr[pivot_ele_idx]] + sort(r_arr)


print(sort([9, 23, 123, 56, -17, -2]))
print(sort([1, 2, 3, 4, 5]))
print(sort([5, 4, 3, 2, 1]))
print(sort([7, 7, 7, 7, 7]))
print(sort(list(range(100000))))
# print(sort())
