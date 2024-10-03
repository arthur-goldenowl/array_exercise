arr1 = [2, 3, 7, 10, 12]
arr2 = [1, 5, 7, 8]

def maxSumPath(arr1, arr2):
    path, path1, path2 = [], [], []
    i, j = 0, 0

    m, n = len(arr1), len(arr2)
    result, sum1, sum2 = 0, 0, 0

    while i < m and j < n:
        if arr1[i] < arr2[j]:
            sum1 += arr1[i]
            path1.append(arr1[i])
            i += 1
        elif arr1[i] > arr2[j]:
            sum2 += arr2[j]
            path2.append(arr2[j])
            j += 1
        else:
            if sum1 > sum2:
                result += sum1
                path.extend(path1)
            else:
                result += sum2
                path.extend(path2)
            result += arr1[i]
            path.append(arr1[i])
            sum1, sum2 = 0, 0
            path1, path2 = [], []
            i += 1
            j += 1
        

    while i < m:
        sum1 += arr1[i]
        path1.append(arr1[i])
        i += 1
    
    while j < n:
        sum2 += arr2[j]
        path2.append(arr2[j])
        j += 1

    if sum1 > sum2:
        path.extend(path1)
        result += sum1
    else:
        path.extend(path2)
        result += sum2

    return result, path

maxSum, path = maxSumPath(arr1, arr2)

print(maxSum, path)