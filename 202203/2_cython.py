""""
1. Cython 是什么？为什么要有 Cython？为什么我们要用 Cython？
https://www.cnblogs.com/traditional/p/13196509.html

全局解释器锁（GIL）
https://www.cnblogs.com/cjaaron/p/9166538.html
CPython 为了解决多线程之间数据完整性和状态同步
许多代码库依赖这种特性（即默认python内部对象是thread-safe的，无需在实现时考虑额外的内存锁和同步操作）根治难度高
Python 中的对象是分配在堆(HEAP)上面的
"""
from sys import getrefcount

s1 = "hello"
s2 = "hello"
s3 = 'hello'
s4 = "world"
l1 = ["hello", "hello", 1, 2]
print(id(s1), id(s2), id(s3))

print("l1", id(l1))
for i in l1:
    print(id(i))

print(getrefcount(s1))
print(getrefcount(s4))
