# -*- coding: utf-8 -*-
# 引用string自带的数字和大小写字母，再自己加上symbols变量引用特殊符号即可

import string
import random

# 参数x = 生成的密码位数
def pass_gen(x):
    symbols = '!@#$%^&*()-+=[{}]:";<>\'?\\/,.'
    password = ''.join(random.sample(string.digits + string.ascii_letters + symbols, x))
    print(password)

pass_gen(20)
