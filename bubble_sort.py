def bubbleSort(arr):
    # 生成数组下标
    n = len(arr)

    for i in range(n):

        for j in range(0, n-i-1):

            if arr[j] > arr[j+1] :
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            print(j)
            print(arr)

arr = [88, 34, 76, 12, 54, 11, 90]

bubbleSort(arr)

print(arr)
