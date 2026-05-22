
def countTriplets(sum, arr):
    n=len(arr)
    arr.sort()
    # print(arr)
    cntr = 0
    for i in range(n-2):
        j,k=i+1,n-1
        while j<k:
            if arr[i]+arr[j]+arr[k] <= sum:
                cntr+=k-j
                j+=1
            else:
                k-=1
    return cntr

print(countTriplets(86,[30, 8, 23, 6, 10, 9, 31, 7, 19, 20, 1, 33, 21, 27, 28, 3, 25, 26]))