arr = [1, 2, 3, 4 ,5]

def reverseArray(arr):
    newArr = arr.copy()
    start = 0
    end = len(newArr) - 1
    while start < end:
        newArr[start], newArr[end] = newArr[end], newArr[start]
        start += 1
        end -= 1

    return newArr

print(reverseArray(arr))