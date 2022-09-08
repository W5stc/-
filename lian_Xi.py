# -*- codeing = utf-8 -*-
# @Time : 2022/7/6 8:38
# @Author : zhangwei
# @File : lian_Xi.py
# @Software : PyCharm
# class Solution(object):
#     def maxProfit(self, prices):
#         """
#         :type prices: List[int]
#         :rtype: int
#         """
#         #flag =  False
#         #flag = True/False
#         #bool flag = False
#         for i in range(0,len(prices)-1):
#             if prices[i+1]>prices[i]:
#                 flag = True
#
#             elif prices[i+1]<prices[i]:
#                 flag = False
#             else:
#                 break
#         if flag == True:
#             return prices[len(prices)-1] - prices[0]
#         if flag == False:
#             return 0
#
#         #for i in range(0,)
#
#
#
#
#
# if __name__ == '__main__':
#     lis = [5,4,3,2,1]
#     A = Solution()
#     t = A.maxProfit(lis)
#     print(t)
#
#     pass


# lis = [1,2,4,5,8]
# a = max(lis)
# print(a)
# c = lis.index(a)
# print(c)
# class Solution(object):
#     def maxProfit(self, prices):
#         """
#         :type prices: List[int]
#         :rtype: int
#         """
#         list = []
#         for i in range(0,len(prices)-1):
#             if prices[i+1] - prices[i] > 0:
#                 list[i] = 1
#             else:
#                 list[i] = 0
#         sum1 = 0
#         for i in range(0,len(prices)-1):
#             if list[i]:
#                 sum1 += (prices[i+1]-prices[i])
#         return sum1
# lis = [1,2,4,5,8]
# A = Solution()
# #a = A.maxProfit(lis)
# c = A.maxProfit(lis)
# print(c)

def huan_(n,k):#n是输入的数字，k是要被杀死的数
    List = list(range(1,n+1))
    index = 0
    while List:
        temp = List.pop(0)
        index += 1
        if index == k:
            index=0
            continue
        List.append(temp)
        if len(List) == 1:
            return List
n = int(input())
k = int(input())

res = huan_(n=n,k=k)
print(res)





#     return List
# print(huan_(7,4))