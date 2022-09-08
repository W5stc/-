# -*- codeing = utf-8 -*-
# @Time : 2022/7/8 14:58
# @Author : zhangwei
# @File : zhan_.py
# @Software : PyCharm
# 取末端为栈顶，栈的原则是先进后出
class Stack:
    def __init__(self):
        self.items = [] #构造函数，说明该类的属性
    def is_empty(self):
        return self.items==[]
    def push(self,item):
        self.items.append(item)
    def pop(self):
        self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]









# lis = [1,2,4]
# lis.pop()
# print(lis)


