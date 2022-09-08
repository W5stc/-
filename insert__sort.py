# -*- codeing = utf-8 -*-
# @Time : 2022/6/20 16:44
# @Author : zhangwei
# @File : insert__sort.py
# @Software : PyCharm

def insertionSort(arr):
    for i in range(len(arr)):
        preIndex = i-1
        current = arr[i]
        while preIndex >= 0 and arr[preIndex] > current:
            arr[preIndex+1] = arr[preIndex]
            preIndex -= 1
        arr[preIndex+1] = current
    return arr
if __name__ == '__main__':
    arr = [1,5,4,8,9,3,6]
    res = insertionSort(arr)
    print(res)

