# -*- codeing = utf-8 -*-
# @Time : 2022/8/6 15:50
# @Author : zhangwei
# @File : quick_sort.py
# @Software : PyCharm
# def partition(arr, low, high):
#     i = (low - 1)  # 最小元素索引
#     pivot = arr[high]
#     for j in range(low, high):
#         # 当前元素小于或等于 pivot
#         if arr[j] <= pivot:
#             i = i + 1
#             arr[i], arr[j] = arr[j], arr[i]
#     arr[i + 1], arr[high] = arr[high], arr[i + 1]
#     return (i + 1)
# # arr[] --> 排序数组
# # low  --> 起始索引
# # high  --> 结束索引
# # 快速排序函数
# def quickSort(arr, low, high):
#     if low < high:
#         pi = partition(arr, low, high)
#         quickSort(arr, low, pi - 1)
#         quickSort(arr, pi + 1, high)
# arr = [10, 7, 8, 9, 1, 5]
# n = len(arr)
# quickSort(arr, 0, n - 1)
# print("排序后的数组:")
# for i in range(n):
#     print("%d" % arr[i])
def partition(alist,first,last):
    pivotvalue = alist[first]#选定中值，这里首先取列表第一个数，之后数据交换过一轮后，中值的值会发生变化，递归调用该函数
    leftmark = first + 1#左右标初值
    rightmark = last
    done = False
    while not done:
        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:#左指针往右走，直到找到比中值大的
            leftmark += 1
        while leftmark <= rightmark and alist[rightmark] >= pivotvalue:#右指针往左走，直到找到比中值小的
            rightmark -= 1
        if rightmark < leftmark:#交错时，推出while循环
            done = True
        else:
            alist[leftmark],alist[rightmark] = alist[rightmark],alist[leftmark]#交换位置
    alist[first],alist[rightmark] = alist[rightmark],alist[first]#此时右标肯定比中值小，所以将中值与右标交换位置
    return rightmark#返回返回中值下标
def quick_sort(alist):
    quick_sort_helper(alist,0,len(alist)-1)#表达方便一点
def quick_sort_helper(alist,first,last):
    if first<last:#基本结束条件
        splitpoint = partition(alist,first,last)#中值
        quick_sort_helper(alist,first,splitpoint-1)#递归调用右半部分
        quick_sort_helper(alist,splitpoint+1,last)#递归调用左半部分
# def partition(alist,first,last):
#     pivotvalue = alist[first]#选定中值，这里首先取列表第一个数，之后数据交换过一轮后，中值的值会发生变化，递归调用该函数
#     leftmark = first + 1#左右标初值
#     rightmark = last
#     done = False
#     while not done:
#         while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
#             leftmark += 1
#         while leftmark <= rightmark and alist[rightmark] >= pivotvalue:
#             rightmark -= 1
#         if rightmark < leftmark:
#             done = True
#         else:
#             alist[leftmark],alist[rightmark] = alist[rightmark],alist[leftmark]
#     alist[first],alist[rightmark] = alist[rightmark],alist[first]
#     return rightmark

alist = [54,26,32,47,8,596,45,78,6,1,64,741]
quick_sort(alist)
print(alist)










