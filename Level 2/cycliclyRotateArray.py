arr = [1, 2, 3, 4, 5]

def cycliclyRotateArray(arr):
    n = len(arr)
    if n == 0:
        return []
    if n == 1:
        return arr
    # return arr[-1:] + arr[:-1]

    last = arr[-1]
    for i in range(n-1, 0, -1):
        arr[i] = arr[i-1]

    arr[0] = last
    return arr

print(arr, cycliclyRotateArray(arr))