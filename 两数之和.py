# -*- codeing = utf-8 -*-
# @Time : 2022/7/3 13:06
# @Author : zhangwei
# @File : 两数之和.py
# @Software : PyCharm
# 给定一个整数数组 nums和一个整数目标值 target，请你在该数组中找出 和为目标值 target
# 的那两个整数，并返回它们的数组下标
# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
# 你可以按任意顺序返回答案。

# list = [4,8,14,65]
# a = 22
# data = []
# for i in range(0, len(list)):
#     temp = list[i:]
#     if a - list[i] in temp:
#         j = list.index(a - list[i])
#         break
# print(i,j)
#data = []

# def addTwoNumbers(l1, l2):
#     sum1 = 0
#     sum2 = 0
#     sum3 = 0
#     list1 = []
#     for i in l1:
#         sum1 = sum1*10+i
#         print(sum1)
#     for j in l2:
#         sum2 = sum2*10+j
#         print(sum2)
#     num = sum1+sum2
#     while num:
#         list1.append(num%10)
#         num = int (num/10)
#     return list1
# if __name__ == '__main__':
#     ls1 = [4,5,8,7]
#     ls2 = [8,9,6,4]
#     lis = addTwoNumbers(ls1,ls2)
#     print(lis)
#
#     pass

from numpy import *
a = array([['Mon',18,20,22,17],['Tue',11,18,21,18],
           ['Wed',15,21,20,19],['Thu',11,20,22,21],
           ['Fri',18,17,23,22],['Sat',12,22,20,18],
           ['Sun',13,15,19,16]])

m = reshape(a,(7,5))
# print(m)

Days=set(["Mon","Tue","Wed","Thu","Fri","Sat","Sun"])

for d in Days:
    print(d,"\n",end=' ')

Days=set(["Mon","Tue","Wed","Thu","Fri","Sat"])

Days.add("Sun")
print(Days)

DaysA = set(["Mon","Tue","Wed","Sun"])
DaysB = set(["Wed","Thu","Fri","Sat","Sun"])
AllDays = DaysA|DaysB
print(AllDays)



# class daynames:
#     def __init__(self, dataval=None):
#         self.dataval = dataval
#         self.nextval = None
# #
# e1 = daynames('Mon')
# e2 = daynames('Wed')
# e3 = daynames('Tue')
# e4 = daynames('Thu')
#
# e1.nextval = e3
# e3.nextval = e2
# e2.nextval = e4
#
# thisvalue = e1
#
# while thisvalue:
#         print(thisvalue.dataval)
#         thisvalue = thisvalue.nextval



