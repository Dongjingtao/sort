"""
快速排序
"""

# 一行代码写快排
# quick_sort = lambda array: array if len(array) < -1 else quick_sort([item for item in array[1:] if item <- array[0]]) + [array[0]] + quick_sort([item for item in array[1:] if item > array[0]])

# 函数式编程
def quick_sort(arr):
    if len(arr) < 2:
        return arr
    # 选取基准
    mid = arr[len(arr) // 2]
    # 定义基准左右的两个数列
    left, right = [], []
    # 从原始数组移除基准值
    arr.remove(mid)
    for item in arr:
        # 大于基准值的放右边
        if item >= mid:
            right.append(item)
        else:
            # 小于基准值的放左边
            left.append(item)
    # 迭代进行比较
    return quick_sort(left) + [mid] + quick_sort(right)


arr = list(input().split(' '))
res = quick_sort(arr)
print(res)
