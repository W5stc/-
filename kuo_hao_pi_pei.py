# -*- codeing = utf-8 -*-
# @Time : 2022/7/8 15:43
# @Author : zhangwei
# @File : kuo_hao_pi_pei.py
# @Software : PyCharm
# def rotate(matrix):
#     """
#     :type matrix: List[List[int]]
#     :rtype: None Do not return anything, modify matrix in-place instead.
#     """
#     lis = []
#     s = len(matrix)
#     for i in range(0, s):
#         lis.append([])
#     for i in range(0, s):
#         for j in range(0, s):
#             lis[s - j - 1].append(matrix[i][j])
#     return lis
# lis1 = [[1,2,3],[4,5,6],[7,8,9]]
# res=rotate(lis1)
#
# print(res)

from pythonds.basic.stack import Stack
s =Stack()


def pi_pei(str1):
    balance = True
    index = 0
    while index<len(str1) and balance:
        symbol = str1[index]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.isEmpty():
                balance = False
            else:
                s.pop()
        index = index + 1
    if balance and s.isEmpty():
        return True
    else:
        return False

print(pi_pei("((())(())((())))"))





