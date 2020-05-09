def pairs(arr, t):
    flag = i = 0
    j = 1
    n = len(arr)
    arr.sort()
    while j < n:
        diff = arr[j] - arr[i]
        if diff == t:
            flag += 1
            j += 1

        elif diff > t:
            i += 1

        else:
            j += 1

    return flag


n, t = map(int, input().split())
arr = list(map(int, input().split()))
print(pairs(arr, t))
