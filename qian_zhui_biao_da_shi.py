# -*- codeing = utf-8 -*-
# @Time : 2022/7/9 18:14
# @Author : zhangwei
# @File : qian_zhui_biao_da_shi.py
# @Software : PyCharm

from pythonds.basic.stack import Stack
def qian_zhui(s):
    dict = {}
    dict["+"] = 2
    dict["-"] = 2
    dict["*"] = 3
    dict["/"] = 3
    dict["("] = 1
    opstack = Stack()
    post_list = []
    # tokenlist = s.split()
    #print(tokenlist)
    for token in s:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            post_list.append(token)
        elif token == "(":
            opstack.push(token)
        elif token == ")":
            top_token = opstack.pop()
            while top_token != '(':             # 5+8*9+(2+3)
                post_list.append(top_token)
                top_token = opstack.pop()
        else:
            print(opstack.isEmpty())
            while(not opstack.isEmpty()) and (dict[opstack.peek()]) >= dict[token]:
                        post_list.append(opstack.pop())
            opstack.push(token)
    while not opstack.isEmpty():
        post_list.append(opstack.pop())
    return post_list

a = "5+8*9+(2+3)"

for i in qian_zhui(a):
    print(i,end='')



# s = "efsfsffw3f"
# print(s.split())
# for i in s:
#     print(i,end='')
