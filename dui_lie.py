# -*- codeing = utf-8 -*-
# @Time : 2022/7/10 16:04
# @Author : zhangwei
# @File : dui_lie.py
# @Software : PyCharm


#
# from pythonds.basic.queue import Queue
#
#
# def ps(name_list, num):
#     queue = Queue()
#     for i in name_list:
#         queue.enqueue(i)
#     while queue.size() > 1:
#         for i in range(num-1):
#             queue.enqueue(queue.dequeue())
#         queue.dequeue()
#     return queue.dequeue()
#
#
# if __name__ == '__main__':
#     a,num = map(int,input().split())
#     list = []
#     for i in range(1,a+1):
#         list.append(i)
#     print(ps(list, num))
# lis = [1,2,3,4,5,6,7]
# print(ps(lis,3))


# def maxSubArray(nums):
#     """
#     :type nums: List[int]
#     :rtype: int
#     """
#     lis = [0]
#     lis[0] = nums[0]
#     for i in range(1, len(nums)):
#         lis.append(max(lis[i - 1] + nums[i], nums[i]))
#     return max(lis)
# print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#     def addTwoNumbers(self, l1, l2):
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
#         """
#         num1 = 0
#         num2 = 0
#         while  != None:
#             num1 = num1*10 + l1.val
#             l1 = l1.next
#         while l2 != None:
#             num2 = num2*10 +l2.val
#             l2 = l2.next
#         num = num1+num2
#         #s = ListNode
#         list1 = []
#         print(num)
#         while num/10 !=0:
#             list1.append(num%10)
#             num /= 10
#         return list1.reverse()
# a = ListNode()
# a.addTwoNumbers([3,4,5],[4,6,2])

n = float()
n = 5/2
print(n)

