1. ## Cpython

   [Cython 是什么？为什么要有 Cython？为什么我们要用 Cython](https://www.cnblogs.com/traditional/p/13196509.html)

   Cython 是一门编程语言，文件的后缀是 .pyx，它是 Python 的一个超集；语法是 Python 语法和 C 语法的混血

   标准解释器 CPython 是由 C 语言实现的，除了 CPython 之外还有 Jython（java实现的 Python 解释器）、PyPy（Python 语言实现的 Python 解释器）

2. ## 全局解释器锁（[GIL](https://www.cnblogs.com/cjaaron/p/9166538.html)）

   CPython 为了解决多线程之间数据完整性和状态同步
   许多代码库依赖这种特性（即默认python内部对象是thread-safe的，无需在实现时考虑额外的内存锁和同步操作）根治难度高

3. ## CPython[的内存概念:栈、堆和引用](https://zhuanlan.zhihu.com/p/166160468)

   Python 中的对象是分配在堆(HEAP)上面的

   多个Python变量引用同一个Python对象就涉及到概念就**引用计数器**，引用计数器属于内存垃圾回收的范畴，由引用计数又会牵涉到CPython一个致命的诟病，GIL:全局解释器锁，为什么多年来CPython不能去掉GIL，很大原因跟引用计数器有关

4. ## [垃圾回收](https://blog.csdn.net/fragmentalice/article/details/84983516)

   1. [垃圾回收](https://www.cnblogs.com/sea520/p/11168522.html)是 python 自带的机制，用于自动释放不会再用到的内存空间;

   2. 引用计数是其中最简单的实现，这只是充分非必要条件，因为循环引用需要通过不可达判定，来确定是否可以回收；

   3. Python 的自动回收算法包括[标记清除](https://zhuanlan.zhihu.com/p/83251959)和分代收集，主要针对的是循环引用的垃圾收集；

      ```
      对于程序，存在一定比例的内存块的生存周期比较短；而剩下的内存块，生存周期会比较长，甚至会从程序开始一直持续到程序结束。生存期较短对象的比例通常在 80%～90% 之间，这种思想简单点说就是：对象存在时间越长，越可能不是垃圾，应该越少去收集。这样在执行标记-清除算法时可以有效减小遍历的对象数，从而提高垃圾回收的速度。
      ```

   4. 调试内存泄漏的工具：objgraph；