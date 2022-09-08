# -*- codeing = utf-8 -*-
# @Time : 2022/7/16 11:03
# @Author : zhangwei
# @File : 任意二进制转换.py
# @Software : PyCharm

def tostr(n,base):  #n是需要转换的数，base是转换的多少进制
    strs = "0123456789ABCDEF"
    if n < base:
        return strs[n]
    else:
        return tostr(n//base,base) + strs[n%base]

print(tostr(5,2))
