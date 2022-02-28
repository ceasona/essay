from functools import partial, reduce
import operator as op

# wraps 装饰修饰器，避免被装饰的函数返回其修饰器的相关内容
# partial 减少参数的传递

# 将 reduce 的第一个参数指定为加法，得到的是类似求和的函数
sum_ = partial(reduce, op.add)

# 将 reduce 的第一个参数指定为乘法，得到的是类似求连乘的函数
prod_ = partial(reduce, op.mul)

print(sum_([1, 2, 3, 4]))
print(prod_([1, 2, 3, 4]))
