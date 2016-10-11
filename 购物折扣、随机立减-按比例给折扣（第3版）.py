# -*- coding: utf-8 -*-
# 国庆在机场看到支付宝、微信支付都有扫码支付立减活动，一时兴起想自己写一段同样的代码

# 首先引用随机函数，套用百分数，生成优惠比例
# 由于随机函数生成的优惠比例在小数点后有很多位，必须让程序只取小数点后两位，再进行计算
# 用笨办法解决了“代码多跑几次还是会出现优惠比例在小数点后有很多位的情况”

import random
temp1 = random.uniform(1,3)
temp2 = float('%.2f' % temp1)
temp3 = temp2 / 100
zhekoulv = float('%.4f' % temp3)

yuanjia = input('请输入购物金额:')
temp4 = float(zhekoulv) * float(yuanjia)
zhekou = float('%.2f' % temp4)

temp5 = float(yuanjia) - float(zhekou)
zhekoujia = float('%.2f' % temp5)

print ('根据您的购物金额计算，您本次享受的随机立减折扣是:',zhekou,'元')
print ('您的最终付款金额是:',zhekoujia,'元')
