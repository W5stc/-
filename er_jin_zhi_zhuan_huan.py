# -*- codeing = utf-8 -*-
# @Time : 2022/7/8 19:20
# @Author : zhangwei
# @File : er_jin_zhi_zhuan_huan.py
# @Software : PyCharm
from pythonds.basic.stack import Stack
def zhuan_huan(num):#十进制转换为二进制
    s = Stack()
    while num > 0:
        a = num % 2
        s.push(a)
        num = num // 2
    str1 = ""
    while not s.isEmpty():
        str1 += (s.pop())
    return str1
print(zhuan_huan(25))

