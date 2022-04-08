1. ## [Hadoop MapReduce和Spark MR实现](https://www.cnblogs.com/upupfeng/p/13386631.html)

   - #### MapReduce  分而治之，并行处理

   - #### Hadoop MapReduce

     ```
     map任务负责数据的载入、解析、转换和过滤。MapReduce作业的输入是一系列储存在HDFS中的文件。reduce任务负责处理map任务输出结果的一个子集
     ```

   - #### Spark基于MapReduce实现

     ```
     Spark并行处理主要基于其内部RDD和DAG来实现。
     RDD（resilient distributed dataset弹性分布式数据集）：作为Spark基本编程模型，它是MapReduce模型的扩展和延伸。其运用高效的数据共享概念（分区）和类似MapReduce的操作方式，使得并行计算能高效的进行。
     DAG（有向无环图）：Spark使用DAG描述了RDD的依赖关系（宽/窄依赖），维护了RDD间的血缘关系，减少了迭代过程中数据的落地，提高了处理效率。
     ```

2. ## [Pyspark模块](https://spark.apache.org/docs/latest/api/python/index.html)

   - 基础模块

     Sparkcontext:是编与Spark程序的王入口 

     RDD：分布式弹性数据集，是Spark内部中最重要的抽象
     Broadcast：在各个住务task中重复使用的广播变量

     Accumulator：一个只能增加的累加器，在各个任务中都可以进行累加，最终进行全局
     累加 

     SparkConf：一个配置对象，用来对Spark中的例如资源，内核个数，提交模式等的配置
     SparkFiles：文件访API 

     StorageLevel：它提供了细粒度的对于数据的缓存、持久化级别
     Taskcontext：实验性质的API，用于获取运行中任务的上下文信息 

   - SQL

     Sparksession：SparkSQL的主入口，其内部仍然是调用SparkContex的
     DataFrame：分布式的结构化的数据集，最终的计算仍然转换为RDD上的计算 

     Column：DataFrame中的列
     Row：DataFrame中的行 

     GroupedData：这里提供聚合数据的一些方法

     DataFrameNaFunctions：处理缺失数据的方法 

     DataFrameStatFunctions：提供统计数据的一些方法
     functions：内建的可用于DataFrame的方法 

     types：可用的数据类型
     Window:提供窗口函数的支持 

   - streaming

     这个模块主要是用来处理流数据，从外部的消息中间件如kafka，fiume或者直接从网络接收数据，来进行实时的流数据处理。其内部会将接收到的数据转换为DStream，DStream
     的内部实际上就是RDD。

   - ml 基于Dataframe

   - mllib 基与RDD

3. 12







参考资料：

- [pyspark：RDD和DataFrame](https://blog.csdn.net/qq_23860475/article/details/90714117)

