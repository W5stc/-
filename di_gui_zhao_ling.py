# -*- codeing = utf-8 -*-
# @Time : 2022/7/18 6:49
# @Author : zhangwei
# @File : di_gui_zhao_ling.py
# @Software : PyCharm

print(5//2)
print(5/2)


def recmc(coin_value_list,change):
    mincoins = change
    if change in coin_value_list:
        return 1
    else:
        for i in [c for c in coin_value_list if c < change]:
            numCoins = 1 + recmc(coin_value_list,change-i)
            if numCoins < mincoins:
                mincoins = numCoins
    return  mincoins
print(recmc([1,5,10,25],63))

