# -*- codeing = utf-8 -*-
# @Time : 2022/7/18 11:08
# @Author : zhangwei
# @File : mao_pao_sort.py
# @Software : PyCharm
def bubbleSort(arr):
    n = len(arr)

    # 遍历所有数组元素
    for i in range(n-1):

        # Last i elements are already in place
        for j in range(0, n - i - 1):

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


arr = [64, 34, 25, 12, 22, 11, 90]

bubbleSort(arr)
print(arr)
