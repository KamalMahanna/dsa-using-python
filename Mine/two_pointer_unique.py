def remove_duplicates_sorted(arr):
    lft = 0
    unq = 1
    for i in range(1, len(arr)):
        if arr[lft] != arr[i]:
            lft += 1
            arr[lft] = arr[i]
            unq += 1
    return arr[:unq]


print(remove_duplicates_sorted([1, 1, 1, 2, 2, 3, 3]))
print(remove_duplicates_sorted([1]))
print(remove_duplicates_sorted([1, 2]))
print(remove_duplicates_sorted([1, 2, 3, 3, 3]))
print(remove_duplicates_sorted([1, 1, 2, 3, 3]))
