# -*- codeing = utf-8 -*-
# @Time : 2022/6/20 16:43
# @Author : zhangwei
# @File : ___init__.py.py
# @Software : PyCharm

# def findMedianSortedArrays(nums1, nums2):
#     """
#     :type nums1: List[int]
#     :type nums2: List[int]
#     :rtype: float
#     """
#     for i in nums2:
#         nums1.append(i)
#     print(nums1)
#     # for i in range(0,len(nums1)-1):
#     #     min1 = i
#     #     for j in range(i+1,len(nums1)):
#     #         if nums1[i] < nums1[min1]:
#     #             min1 = j
#     #     if i!= min1:
#     #         nums1[i],nums1[min1] = nums1[min1],nums1[i]
#     for i in range(0, len(nums1) - 1):
#         for j in range(0, len(nums1) - i - 1):
#             if nums1[j] > nums1[j + 1]:
#                 nums1[j], nums1[j + 1] = nums1[j + 1], nums1[j]
#
#     i = len(nums1)
#     print("i的值是:%d" % i)
#     print(nums1)
#     if i % 2 == 0:
#         num = float()
#         num = nums1[i / 2 - 1] + nums1[i / 2]
#         print(num / 2)
#         return num / 2
#
#     else:
#         return nums1[i / 2]
# print(findMedianSortedArrays([1,3],[2,4]))

print(5/2)
